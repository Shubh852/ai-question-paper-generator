"""
Database abstraction layer supporting PostgreSQL (Supabase) with automatic
failover to local SQLite storage for standalone operation and testing.
"""

import os
import json
import uuid
import sqlite3
import hashlib
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("database")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SQLITE_DB_PATH = DATA_DIR / "question_bank.db"

SUPABASE_URL = os.getenv("SUPABASE_URL") or "https://kwlrfcogywkmrhyzusqg.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY") or "sb_publishable_74OMgqGqC1xxAN-rGY5_qg_EhyDwtEJ"

class Database:
    def __init__(self):
        self.use_supabase = False
        self.client = None
        self._init_backend()

    def _init_backend(self):
        if SUPABASE_URL and SUPABASE_KEY and SUPABASE_URL.startswith("http"):
            try:
                from supabase import create_client, Client
                client = create_client(SUPABASE_URL, SUPABASE_KEY)
                # Verify that tables are created in Supabase
                res = client.table("master_question_bank").select("id").limit(1).execute()
                self.client = client
                self.use_supabase = True
                logger.info(f"Connected to Supabase PostgreSQL at {SUPABASE_URL} (tables verified)")
                self._init_sqlite()
                return
            except Exception as e:
                logger.warning(
                    f"Supabase connection/table check: {e}. "
                    "Using local high-performance SQLite engine at data/question_bank.db. "
                    "(Tip: Execute scripts/supabase_schema.sql in Supabase SQL editor to sync to cloud)."
                )

        # Fallback to SQLite
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.use_supabase = False
        self._init_sqlite()
        logger.info(f"Initialized SQLite database at {SQLITE_DB_PATH}")

    def _init_sqlite(self):
        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS master_question_bank (
                id TEXT PRIMARY KEY,
                grade_level INTEGER NOT NULL CHECK (grade_level BETWEEN 10 AND 12),
                subject TEXT NOT NULL,
                chapter TEXT NOT NULL,
                topic TEXT NOT NULL,
                primary_exam TEXT NOT NULL,
                applicable_exams TEXT NOT NULL, -- JSON array
                difficulty_tier INTEGER CHECK (difficulty_tier BETWEEN 1 AND 5),
                question_format TEXT NOT NULL,
                marks REAL NOT NULL,
                question_text_latex TEXT NOT NULL,
                options TEXT, -- JSON object
                correct_option TEXT,
                ideal_solution_latex TEXT NOT NULL,
                step_marking_rubric TEXT NOT NULL, -- JSON array
                source_book TEXT,
                content_hash TEXT UNIQUE,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS generated_exams (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                grade_level INTEGER NOT NULL,
                subject TEXT NOT NULL,
                total_marks INTEGER NOT NULL,
                duration_minutes INTEGER NOT NULL,
                exam_type TEXT NOT NULL,
                selected_chapters TEXT NOT NULL, -- JSON array
                blueprint_breakdown TEXT NOT NULL, -- JSON object
                question_ids TEXT NOT NULL, -- JSON array
                student_pdf_url TEXT,
                solution_pdf_url TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS teacher_leads (
                id TEXT PRIMARY KEY,
                teacher_name TEXT NOT NULL,
                school_name TEXT NOT NULL,
                city TEXT NOT NULL,
                whatsapp_number TEXT NOT NULL,
                generated_exam_id TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (generated_exam_id) REFERENCES generated_exams(id)
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS teacher_accounts (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                school TEXT NOT NULL,
                city TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                whatsapp TEXT NOT NULL,
                password_hash TEXT,
                primary_grade INTEGER,
                primary_subject TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """)

            cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_qbank_selection 
            ON master_question_bank (grade_level, subject, chapter, difficulty_tier);
            """)
            conn.commit()

    @staticmethod
    def compute_hash(grade: int, subject: str, chapter: str, question_text: str) -> str:
        raw = f"{grade}:{subject.strip().lower()}:{chapter.strip().lower()}:{question_text.strip()}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def upsert_questions(self, questions: List[Dict[str, Any]]) -> int:
        """Batch upsert questions into question bank."""
        if not questions:
            return 0

        inserted_count = 0
        if self.use_supabase:
            try:
                # Deduplicate by content_hash before upserting to satisfy Postgres ON CONFLICT
                format_map = {
                    "SA_I": "SHORT_ANSWER",
                    "SA_II": "SHORT_ANSWER",
                    "SA": "SHORT_ANSWER",
                    "VSA": "SHORT_ANSWER",
                    "LA": "LONG_ANSWER",
                    "LA_I": "LONG_ANSWER",
                    "LA_II": "LONG_ANSWER",
                    "MCQ": "MCQ",
                    "ASSERTION_REASON": "ASSERTION_REASON",
                    "CASE_STUDY": "CASE_STUDY",
                    "CASE": "CASE_STUDY",
                }
                unique_map = {}
                for q in questions:
                    rec = dict(q)
                    if "id" not in rec or not rec["id"]:
                        rec["id"] = str(uuid.uuid4())
                    if "content_hash" not in rec:
                        rec["content_hash"] = self.compute_hash(
                            rec["grade_level"], rec["subject"], rec["chapter"], rec["question_text_latex"]
                        )
                    # Normalize enum for Postgres
                    fmt = str(rec.get("question_format", "SHORT_ANSWER")).upper()
                    rec["question_format"] = format_map.get(fmt, "SHORT_ANSWER")

                    # Ensure primary_exam is valid enum
                    p_exam = str(rec.get("primary_exam", "CBSE_BOARD")).upper()
                    rec["primary_exam"] = p_exam if p_exam in ["CBSE_BOARD", "JEE_MAIN", "JEE_ADVANCED", "NEET"] else "CBSE_BOARD"

                    # Ensure applicable_exams is a list of valid enums
                    if isinstance(rec.get("applicable_exams"), str):
                        try:
                            rec["applicable_exams"] = json.loads(rec["applicable_exams"])
                        except Exception:
                            rec["applicable_exams"] = ["CBSE_BOARD"]
                    elif not rec.get("applicable_exams"):
                        rec["applicable_exams"] = ["CBSE_BOARD"]

                    # Ensure options is a dict/JSON if present
                    if isinstance(rec.get("options"), str):
                        try:
                            rec["options"] = json.loads(rec["options"])
                        except Exception:
                            pass

                    # Ensure step_marking_rubric is a list if present
                    if isinstance(rec.get("step_marking_rubric"), str):
                        try:
                            rec["step_marking_rubric"] = json.loads(rec["step_marking_rubric"])
                        except Exception:
                            rec["step_marking_rubric"] = []

                    unique_map[rec["content_hash"]] = rec
                records = list(unique_map.values())
                
                # Upsert in chunks of 50 to avoid request payload limits
                chunk_size = 50
                for i in range(0, len(records), chunk_size):
                    chunk = records[i:i + chunk_size]
                    res = self.client.table("master_question_bank").upsert(
                        chunk, on_conflict="content_hash"
                    ).execute()
                    inserted_count += len(res.data) if res.data else len(chunk)
                return inserted_count
            except Exception as e:
                logger.error(f"Supabase upsert error: {e}. Falling back to SQLite.")
                self.use_supabase = False
                self._init_sqlite()

        # SQLite upsert
        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            cursor = conn.cursor()
            for q in questions:
                q_id = q.get("id") or str(uuid.uuid4())
                c_hash = q.get("content_hash") or self.compute_hash(
                    q["grade_level"], q["subject"], q["chapter"], q["question_text_latex"]
                )
                applicable_exams = json.dumps(q.get("applicable_exams", ["CBSE_BOARD"]))
                options = json.dumps(q.get("options")) if q.get("options") else None
                rubric = json.dumps(q.get("step_marking_rubric", []))

                try:
                    cursor.execute("""
                    INSERT INTO master_question_bank (
                        id, grade_level, subject, chapter, topic, primary_exam,
                        applicable_exams, difficulty_tier, question_format, marks,
                        question_text_latex, options, correct_option, ideal_solution_latex,
                        step_marking_rubric, source_book, content_hash
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(content_hash) DO UPDATE SET
                        question_text_latex=excluded.question_text_latex,
                        ideal_solution_latex=excluded.ideal_solution_latex,
                        step_marking_rubric=excluded.step_marking_rubric,
                        options=excluded.options,
                        marks=excluded.marks
                    """, (
                        q_id,
                        int(q["grade_level"]),
                        str(q["subject"]),
                        str(q["chapter"]),
                        str(q.get("topic", "General")),
                        str(q.get("primary_exam", "CBSE_BOARD")),
                        applicable_exams,
                        int(q.get("difficulty_tier", 2)),
                        str(q["question_format"]),
                        float(q["marks"]),
                        str(q["question_text_latex"]),
                        options,
                        q.get("correct_option"),
                        str(q["ideal_solution_latex"]),
                        rubric,
                        str(q.get("source_book", "NCERT")),
                        c_hash
                    ))
                    inserted_count += 1
                except Exception as e:
                    logger.warning(f"Error inserting question: {e}")
            conn.commit()

        return inserted_count

    def get_taxonomy(self) -> Dict[str, Any]:
        """Return grade -> subjects -> chapters with question counts and topics."""
        taxonomy = {}
        if self.use_supabase:
            try:
                rows = []
                page_size = 1000
                for offset in range(0, 50000, page_size):
                    res = self.client.table("master_question_bank").select(
                        "grade_level, subject, chapter, topic"
                    ).range(offset, offset + page_size - 1).execute()
                    if not res.data:
                        break
                    rows.extend(res.data)
                    if len(res.data) < page_size:
                        break

                for r in rows:
                    g = str(r["grade_level"])
                    s = r["subject"]
                    c = r["chapter"]
                    t = r.get("topic") or "General"
                    taxonomy.setdefault(g, {}).setdefault(s, {}).setdefault(c, {"count": 0, "topics": {}})
                    taxonomy[g][s][c]["count"] += 1
                    taxonomy[g][s][c]["topics"].setdefault(t, 0)
                    taxonomy[g][s][c]["topics"][t] += 1
                return taxonomy
            except Exception as e:
                logger.warning(f"Supabase taxonomy fetch failed: {e}")

        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT grade_level, subject, chapter, topic, COUNT(*) as cnt 
            FROM master_question_bank 
            GROUP BY grade_level, subject, chapter, topic
            ORDER BY grade_level, subject, chapter, topic
            """)
            for row in cursor.fetchall():
                g = str(row[0])
                s = row[1]
                c = row[2]
                t = str(row[3]) if row[3] else "General"
                cnt = row[4]
                taxonomy.setdefault(g, {}).setdefault(s, {}).setdefault(c, {"count": 0, "topics": {}})
                taxonomy[g][s][c]["count"] += cnt
                taxonomy[g][s][c]["topics"].setdefault(t, 0)
                taxonomy[g][s][c]["topics"][t] += cnt

        return taxonomy

    def query_questions(
        self,
        grade: int,
        subject: str,
        chapters: Optional[List[str]] = None,
        topics: Optional[List[str]] = None,
        exam_type: Optional[str] = None,
        difficulty_min: int = 1,
        difficulty_max: int = 5,
        question_format: Optional[str] = None,
        limit: int = 200
    ) -> List[Dict[str, Any]]:
        """Query questions matching filter criteria."""
        if self.use_supabase:
            try:
                query = self.client.table("master_question_bank").select("*")
                query = query.eq("grade_level", grade)
                query = query.ilike("subject", f"%{subject}%")
                if chapters:
                    query = query.in_("chapter", chapters)
                if topics:
                    query = query.in_("topic", topics)
                if question_format:
                    query = query.eq("question_format", question_format)
                query = query.gte("difficulty_tier", difficulty_min).lte("difficulty_tier", difficulty_max)
                query = query.limit(limit)
                res = query.execute()
                return res.data or []
            except Exception as e:
                logger.warning(f"Supabase query failed: {e}")

        # SQLite query
        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            clauses = ["grade_level = ?", "subject LIKE ?"]
            params: list = [grade, f"%{subject}%"]

            if chapters:
                placeholders = ",".join("?" for _ in chapters)
                clauses.append(f"chapter IN ({placeholders})")
                params.extend(chapters)

            if topics:
                placeholders = ",".join("?" for _ in topics)
                clauses.append(f"topic IN ({placeholders})")
                params.extend(topics)

            if question_format:
                clauses.append("question_format = ?")
                params.append(question_format)

            clauses.append("difficulty_tier BETWEEN ? AND ?")
            params.extend([difficulty_min, difficulty_max])

            where_sql = " AND ".join(clauses)
            cursor.execute(f"""
            SELECT * FROM master_question_bank 
            WHERE {where_sql}
            ORDER BY RANDOM()
            LIMIT ?
            """, (*params, limit))

            rows = cursor.fetchall()
            results = []
            for r in rows:
                item = dict(r)
                if item.get("applicable_exams"):
                    try:
                        item["applicable_exams"] = json.loads(item["applicable_exams"])
                    except Exception:
                        pass
                if item.get("options"):
                    try:
                        item["options"] = json.loads(item["options"])
                    except Exception:
                        pass
                if item.get("step_marking_rubric"):
                    try:
                        item["step_marking_rubric"] = json.loads(item["step_marking_rubric"])
                    except Exception:
                        pass
                results.append(item)
            return results

    def get_question_by_id(self, question_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a single question by UUID."""
        if self.use_supabase:
            try:
                res = self.client.table("master_question_bank").select("*").eq("id", question_id).single().execute()
                return res.data
            except Exception:
                pass

        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM master_question_bank WHERE id = ?", (question_id,))
            row = cursor.fetchone()
            if not row:
                return None
            item = dict(row)
            if item.get("options"):
                try: item["options"] = json.loads(item["options"])
                except Exception: pass
            if item.get("step_marking_rubric"):
                try: item["step_marking_rubric"] = json.loads(item["step_marking_rubric"])
                except Exception: pass
            if item.get("applicable_exams"):
                try: item["applicable_exams"] = json.loads(item["applicable_exams"])
                except Exception: pass
            return item

    def get_alternative_question(self, current_question_id: str) -> Optional[Dict[str, Any]]:
        """Find an alternative question matching the same marks, format, grade and subject."""
        curr = self.get_question_by_id(current_question_id)
        if not curr:
            return None

        candidates = self.query_questions(
            grade=curr["grade_level"],
            subject=curr["subject"],
            chapters=[curr["chapter"]],
            question_format=curr["question_format"],
            limit=10
        )
        # Filter out current
        alternatives = [c for c in candidates if c["id"] != current_question_id and float(c["marks"]) == float(curr["marks"])]
        if alternatives:
            return alternatives[0]

        # Broaden to all chapters of same grade/subject with matching marks and format
        broad_candidates = self.query_questions(
            grade=curr["grade_level"],
            subject=curr["subject"],
            question_format=curr["question_format"],
            limit=20
        )
        broad_alt = [c for c in broad_candidates if c["id"] != current_question_id and float(c["marks"]) == float(curr["marks"])]
        return broad_alt[0] if broad_alt else None

    def save_generated_exam(self, exam_data: Dict[str, Any]) -> str:
        exam_id = exam_data.get("id") or str(uuid.uuid4())
        exam_data["id"] = exam_id

        if self.use_supabase:
            try:
                supa_payload = {k: v for k, v in exam_data.items() if k not in ("created_by",)}
                self.client.table("generated_exams").insert(supa_payload).execute()
                return exam_id
            except Exception as e:
                logger.warning(f"Supabase exam insert failed: {e}")

        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO generated_exams (
                id, title, grade_level, subject, total_marks, duration_minutes,
                exam_type, selected_chapters, blueprint_breakdown, question_ids,
                student_pdf_url, solution_pdf_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                exam_id,
                exam_data["title"],
                int(exam_data["grade_level"]),
                str(exam_data["subject"]),
                int(exam_data["total_marks"]),
                int(exam_data["duration_minutes"]),
                str(exam_data["exam_type"]),
                json.dumps(exam_data["selected_chapters"]),
                json.dumps(exam_data["blueprint_breakdown"]),
                json.dumps(exam_data["question_ids"]),
                exam_data.get("student_pdf_url"),
                exam_data.get("solution_pdf_url")
            ))
            conn.commit()

        return exam_id

    def get_saved_exams(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Fetch list of previously generated exams for the teacher dashboard."""
        exams = []
        if self.use_supabase:
            try:
                res = self.client.table("generated_exams").select("*").order("created_at", desc=True).limit(limit).execute()
                for r in res.data or []:
                    item = dict(r)
                    if isinstance(item.get("selected_chapters"), str):
                        try: item["selected_chapters"] = json.loads(item["selected_chapters"])
                        except Exception: pass
                    if isinstance(item.get("blueprint_breakdown"), str):
                        try: item["blueprint_breakdown"] = json.loads(item["blueprint_breakdown"])
                        except Exception: pass
                    if isinstance(item.get("question_ids"), str):
                        try: item["question_ids"] = json.loads(item["question_ids"])
                        except Exception: pass
                    exams.append(item)
                return exams
            except Exception as e:
                logger.warning(f"Supabase get_saved_exams failed: {e}")

        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM generated_exams ORDER BY created_at DESC LIMIT ?", (limit,))
            rows = cursor.fetchall()
            for r in rows:
                item = dict(r)
                if item.get("selected_chapters"):
                    try: item["selected_chapters"] = json.loads(item["selected_chapters"])
                    except Exception: pass
                if item.get("blueprint_breakdown"):
                    try: item["blueprint_breakdown"] = json.loads(item["blueprint_breakdown"])
                    except Exception: pass
                if item.get("question_ids"):
                    try: item["question_ids"] = json.loads(item["question_ids"])
                    except Exception: pass
                exams.append(item)
        return exams

    def get_saved_exam_by_id(self, exam_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a saved exam and rehydrate its full question sections."""
        exam = None
        if self.use_supabase:
            try:
                res = self.client.table("generated_exams").select("*").eq("id", exam_id).single().execute()
                exam = res.data
            except Exception as e:
                logger.warning(f"Supabase get_saved_exam_by_id failed: {e}")

        if not exam:
            with sqlite3.connect(SQLITE_DB_PATH) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM generated_exams WHERE id = ?", (exam_id,))
                row = cursor.fetchone()
                if row:
                    exam = dict(row)

        if not exam:
            return None

        # Parse JSON fields
        for f in ["selected_chapters", "blueprint_breakdown", "question_ids"]:
            if isinstance(exam.get(f), str):
                try: exam[f] = json.loads(exam[f])
                except Exception: pass

        # Rehydrate question list and sections
        q_ids = exam.get("question_ids", [])
        sections = {"A": [], "B": [], "C": [], "D": [], "E": []}
        all_qs = []
        for qid in q_ids:
            q = self.get_question_by_id(qid)
            if q:
                all_qs.append(q)
                m = float(q.get("marks", 1))
                if m == 1.0:
                    sections["A"].append(q)
                elif m == 2.0:
                    sections["B"].append(q)
                elif m == 3.0:
                    sections["C"].append(q)
                elif m == 5.0:
                    sections["D"].append(q)
                elif m == 4.0:
                    sections["E"].append(q)
                else:
                    sections["C"].append(q)

        exam["sections"] = sections
        exam["questions"] = all_qs
        return exam

    def delete_saved_exam(self, exam_id: str) -> bool:
        """Deletes a saved exam from database."""
        deleted = False
        if self.use_supabase:
            try:
                self.client.table("generated_exams").delete().eq("id", exam_id).execute()
                deleted = True
            except Exception as e:
                logger.warning(f"Supabase delete_saved_exam failed: {e}")

        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM generated_exams WHERE id = ?", (exam_id,))
            conn.commit()
            if cursor.rowcount > 0:
                deleted = True

        return deleted

    def save_teacher_lead(self, lead_data: Dict[str, Any]) -> str:
        lead_id = lead_data.get("id") or str(uuid.uuid4())
        lead_data["id"] = lead_id

        if self.use_supabase:
            try:
                self.client.table("teacher_leads").insert(lead_data).execute()
                return lead_id
            except Exception as e:
                logger.warning(f"Supabase lead insert failed: {e}")

        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO teacher_leads (
                id, teacher_name, school_name, city, whatsapp_number, generated_exam_id
            ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                lead_id,
                lead_data["teacher_name"],
                lead_data["school_name"],
                lead_data["city"],
                lead_data["whatsapp_number"],
                lead_data.get("generated_exam_id")
            ))
            conn.commit()

        return lead_id

    def register_teacher(self, teacher_data: Dict[str, Any]) -> Dict[str, Any]:
        """Registers a new teacher account or updates profile."""
        teacher_id = teacher_data.get("id") or str(uuid.uuid4())
        pwd = teacher_data.get("password", "")
        pwd_hash = hashlib.sha256(pwd.encode()).hexdigest() if pwd else None

        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT OR REPLACE INTO teacher_accounts (
                id, name, school, city, email, whatsapp, password_hash, primary_grade, primary_subject
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                teacher_id,
                teacher_data.get("name", "Educator"),
                teacher_data.get("school", "School"),
                teacher_data.get("city", "City"),
                teacher_data.get("email", ""),
                teacher_data.get("whatsapp", ""),
                pwd_hash,
                int(teacher_data.get("primary_grade", 10)),
                str(teacher_data.get("primary_subject", "Mathematics"))
            ))
            cursor.execute("""
            INSERT OR IGNORE INTO teacher_leads (
                id, teacher_name, school_name, city, whatsapp_number
            ) VALUES (?, ?, ?, ?, ?)
            """, (
                teacher_id,
                teacher_data.get("name", "Educator"),
                teacher_data.get("school", "School"),
                teacher_data.get("city", "City"),
                teacher_data.get("whatsapp", "")
            ))
            conn.commit()

        if self.use_supabase:
            try:
                self.client.table("teacher_leads").upsert({
                    "id": teacher_id,
                    "teacher_name": teacher_data.get("name", "Educator"),
                    "school_name": teacher_data.get("school", "School"),
                    "city": teacher_data.get("city", "City"),
                    "whatsapp_number": teacher_data.get("whatsapp", "")
                }).execute()
            except Exception as e:
                logger.warning(f"Supabase teacher lead sync: {e}")

        return {
            "id": teacher_id,
            "name": teacher_data.get("name"),
            "school": teacher_data.get("school"),
            "city": teacher_data.get("city"),
            "email": teacher_data.get("email"),
            "whatsapp": teacher_data.get("whatsapp"),
            "primary_grade": int(teacher_data.get("primary_grade", 10)),
            "primary_subject": str(teacher_data.get("primary_subject", "Mathematics"))
        }

    def login_teacher(self, email_or_phone: str, password: str = "") -> Optional[Dict[str, Any]]:
        """Validates or finds existing teacher account by email or whatsapp in SQLite and Supabase."""
        term = email_or_phone.strip()
        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
            SELECT * FROM teacher_accounts 
            WHERE email = ? OR whatsapp = ? OR email LIKE ? OR whatsapp LIKE ? OR id = ?
            LIMIT 1
            """, (term, term, f"%{term}%", f"%{term}%", term))
            row = cursor.fetchone()
            if row:
                t = dict(row)
                return {
                    "id": t["id"],
                    "name": t["name"],
                    "school": t["school"],
                    "city": t["city"],
                    "email": t["email"],
                    "whatsapp": t["whatsapp"],
                    "primary_grade": t.get("primary_grade", 10),
                    "primary_subject": t.get("primary_subject", "Mathematics")
                }

        # Query Supabase cloud leads if not cached locally in SQLite
        if self.use_supabase:
            try:
                clean_phone = re.sub(r"[^\d+]", "", term)
                res = self.client.table("teacher_leads").select("*").or_(
                    f"whatsapp_number.eq.{term},whatsapp_number.eq.{clean_phone},teacher_name.ilike.%{term}%,id.eq.{term}"
                ).order("created_at", desc=True).limit(1).execute()
                if res.data:
                    lead = res.data[0]
                    lead_user = {
                        "id": lead["id"],
                        "name": lead.get("teacher_name", "Educator"),
                        "school": lead.get("school_name", "School"),
                        "city": lead.get("city", "City"),
                        "email": term if "@" in term else f"{clean_phone}@school.edu",
                        "whatsapp": lead.get("whatsapp_number", term),
                        "primary_grade": 10,
                        "primary_subject": "Mathematics"
                    }
                    # Cache in local SQLite
                    try:
                        with sqlite3.connect(SQLITE_DB_PATH) as conn:
                            cursor = conn.cursor()
                            cursor.execute("""
                            INSERT OR REPLACE INTO teacher_accounts (id, name, school, city, email, whatsapp, primary_grade, primary_subject)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """, (
                                lead_user["id"], lead_user["name"], lead_user["school"],
                                lead_user["city"], lead_user["email"], lead_user["whatsapp"],
                                lead_user["primary_grade"], lead_user["primary_subject"]
                            ))
                            conn.commit()
                    except Exception:
                        pass
                    return lead_user
            except Exception as se:
                logger.warning(f"Supabase login search failed: {se}")

        return None

    def get_teacher_stats(self, identifier: str) -> Dict[str, Any]:
        """Returns educator profile and total papers created count from Supabase & SQLite."""
        teacher = self.login_teacher(identifier)
        term = identifier.strip()
        papers_count = 0

        # Query Supabase teacher_leads for paper records created by this educator
        if self.use_supabase:
            try:
                target_whatsapp = teacher.get("whatsapp") if teacher else term
                res = self.client.table("teacher_leads").select("generated_exam_id").eq("whatsapp_number", target_whatsapp).execute()
                exam_records = [r for r in res.data or [] if r.get("generated_exam_id")]
                papers_count = len(exam_records)
            except Exception as e:
                logger.warning(f"Supabase get_teacher_stats failed: {e}")

        # Query SQLite teacher_leads
        try:
            with sqlite3.connect(SQLITE_DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                SELECT COUNT(*) FROM teacher_leads 
                WHERE (whatsapp_number = ? OR teacher_name LIKE ?) 
                AND generated_exam_id IS NOT NULL
                """, (term, f"%{term}%"))
                row = cursor.fetchone()
                if row and row[0] > papers_count:
                    papers_count = row[0]
        except Exception as e:
            logger.warning(f"SQLite teacher stats query: {e}")

        return {
            "teacher": teacher or {
                "name": term.split("@")[0].capitalize() if "@" in term else "Verified Educator",
                "school": "Delhi Public School",
                "city": "New Delhi",
                "email": term if "@" in term else "",
                "whatsapp": term if not "@" in term else ""
            },
            "total_papers_created": max(papers_count, 1 if teacher else 0)
        }

# Singleton instance
db = Database()
