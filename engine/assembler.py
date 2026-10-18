"""
Paper Assembly Engine & Constraint Solver:
Selects a balanced, non-duplicate set of questions matching exact syllabus,
total marks, section distribution, and difficulty levels.
Supports question swapping and blueprint generation.
"""

import random
import logging
from typing import List, Dict, Any, Optional
from backend.database import db

logger = logging.getLogger("assembler")

# Standard CBSE & Assessment Blueprint Presets
BLUEPRINT_PRESETS = {
    15: {
        "title": "Class Test / Weekly Quiz (15 Marks)",
        "duration_minutes": 35,
        "sections": {
            "A": {"marks_per_q": 1.0, "count": 5, "formats": ["MCQ", "ASSERTION_REASON"]},
            "B": {"marks_per_q": 2.0, "count": 2, "formats": ["SHORT_ANSWER"]},
            "C": {"marks_per_q": 3.0, "count": 2, "formats": ["SHORT_ANSWER"]},
        }
    },
    20: {
        "title": "Periodic Test I (20 Marks)",
        "duration_minutes": 45,
        "sections": {
            "A": {"marks_per_q": 1.0, "count": 6, "formats": ["MCQ", "ASSERTION_REASON"]},
            "B": {"marks_per_q": 2.0, "count": 4, "formats": ["SHORT_ANSWER"]},
            "C": {"marks_per_q": 3.0, "count": 2, "formats": ["SHORT_ANSWER"]},
        }
    },
    25: {
        "title": "Unit Assessment Test (25 Marks)",
        "duration_minutes": 60,
        "sections": {
            "A": {"marks_per_q": 1.0, "count": 5, "formats": ["MCQ", "ASSERTION_REASON"]},
            "B": {"marks_per_q": 2.0, "count": 3, "formats": ["SHORT_ANSWER"]},
            "C": {"marks_per_q": 3.0, "count": 3, "formats": ["SHORT_ANSWER"]},
            "D": {"marks_per_q": 5.0, "count": 1, "formats": ["LONG_ANSWER"]},
        }
    },
    40: {
        "title": "Periodic Assessment II (40 Marks)",
        "duration_minutes": 90,
        "sections": {
            "A": {"marks_per_q": 1.0, "count": 10, "formats": ["MCQ", "ASSERTION_REASON"]},
            "B": {"marks_per_q": 2.0, "count": 4, "formats": ["SHORT_ANSWER"]},
            "C": {"marks_per_q": 3.0, "count": 4, "formats": ["SHORT_ANSWER"]},
            "D": {"marks_per_q": 5.0, "count": 2, "formats": ["LONG_ANSWER"]},
        }
    },
    50: {
        "title": "Mid-Term Examination (50 Marks)",
        "duration_minutes": 120,
        "sections": {
            "A": {"marks_per_q": 1.0, "count": 12, "formats": ["MCQ", "ASSERTION_REASON"]},
            "B": {"marks_per_q": 2.0, "count": 5, "formats": ["SHORT_ANSWER"]},
            "C": {"marks_per_q": 3.0, "count": 6, "formats": ["SHORT_ANSWER"]},
            "D": {"marks_per_q": 5.0, "count": 2, "formats": ["LONG_ANSWER"]},
        }
    },
    70: {
        "title": "CBSE Science Theory Examination (70 Marks)",
        "duration_minutes": 180,
        "sections": {
            "A": {"marks_per_q": 1.0, "count": 16, "formats": ["MCQ", "ASSERTION_REASON"]},
            "B": {"marks_per_q": 2.0, "count": 5, "formats": ["SHORT_ANSWER"]},
            "C": {"marks_per_q": 3.0, "count": 7, "formats": ["SHORT_ANSWER"]},
            "D": {"marks_per_q": 4.0, "count": 2, "formats": ["CASE_STUDY"]},
            "E": {"marks_per_q": 5.0, "count": 3, "formats": ["LONG_ANSWER"]},
        }
    },
    80: {
        "title": "CBSE Board Examination (80 Marks)",
        "duration_minutes": 180,
        "sections": {
            "A": {"marks_per_q": 1.0, "count": 20, "formats": ["MCQ", "ASSERTION_REASON"]},
            "B": {"marks_per_q": 2.0, "count": 5, "formats": ["SHORT_ANSWER"]},
            "C": {"marks_per_q": 3.0, "count": 6, "formats": ["SHORT_ANSWER"]},
            "D": {"marks_per_q": 5.0, "count": 4, "formats": ["LONG_ANSWER"]},
            "E": {"marks_per_q": 4.0, "count": 3, "formats": ["CASE_STUDY"]},
        }
    }
}

class ExamAssembler:
    @staticmethod
    def get_preset_spec(total_marks: int) -> Dict[str, Any]:
        if total_marks in BLUEPRINT_PRESETS:
            return BLUEPRINT_PRESETS[total_marks]
        
        # Dynamic exact partition for any custom mark
        best_partition = None
        min_diff = 99999
        m = total_marks

        for q5 in range(m // 5 + 1):
            for q4 in range((m - 5 * q5) // 4 + 1):
                for q3 in range((m - 5 * q5 - 4 * q4) // 3 + 1):
                    rem = m - 5 * q5 - 4 * q4 - 3 * q3
                    if rem >= 0:
                        for q2 in range(rem // 2 + 1):
                            q1 = rem - 2 * q2
                            if q1 >= 0 and (5 * q5 + 4 * q4 + 3 * q3 + 2 * q2 + q1 == m):
                                score = abs(q1 * 1.0 - m * 0.3) + abs(q2 * 2.0 - m * 0.25) + abs(q3 * 3.0 - m * 0.25)
                                if score < min_diff:
                                    min_diff = score
                                    best_partition = (q1, q2, q3, q4, q5)

        sections = {}
        if best_partition:
            q1, q2, q3, q4, q5 = best_partition
            sec_idx = ord('A')
            if q1 > 0:
                sections[chr(sec_idx)] = {"marks_per_q": 1.0, "count": q1, "formats": ["MCQ", "ASSERTION_REASON"]}
                sec_idx += 1
            if q2 > 0:
                sections[chr(sec_idx)] = {"marks_per_q": 2.0, "count": q2, "formats": ["SHORT_ANSWER"]}
                sec_idx += 1
            if q3 > 0:
                sections[chr(sec_idx)] = {"marks_per_q": 3.0, "count": q3, "formats": ["SHORT_ANSWER"]}
                sec_idx += 1
            if q4 > 0:
                sections[chr(sec_idx)] = {"marks_per_q": 4.0, "count": q4, "formats": ["CASE_STUDY"]}
                sec_idx += 1
            if q5 > 0:
                sections[chr(sec_idx)] = {"marks_per_q": 5.0, "count": q5, "formats": ["LONG_ANSWER"]}
                sec_idx += 1

        if not sections:
            sections["A"] = {"marks_per_q": 1.0, "count": total_marks, "formats": ["MCQ"]}

        duration = max(30, int(total_marks * 2.2))
        return {
            "title": f"Custom Assessment ({total_marks} Marks)",
            "duration_minutes": duration,
            "sections": sections
        }

    @staticmethod
    def assemble_paper(
        grade: int,
        subject: str,
        chapters: List[str],
        topics: Optional[List[str]] = None,
        exam_type: str = "CBSE_BOARD",
        total_marks: int = 25,
        difficulty_weights: Optional[Dict[str, float]] = None,
        title: Optional[str] = None,
        exclude_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Assemble question list adhering to section blueprints, syllabus chapters,
        and difficulty distribution. Supports exclude_ids for fresh paper regeneration.
        """
        spec = ExamAssembler.get_preset_spec(total_marks)
        sections_spec = spec["sections"]

        # Fetch candidate pool
        candidates = db.query_questions(
            grade=grade,
            subject=subject,
            chapters=chapters if chapters else None,
            topics=topics if topics else None,
            limit=500
        )

        # Fallback to chapters if specific topics have insufficient questions
        if not candidates and topics:
            logger.info("Falling back from specific topics to full chapter pool")
            candidates = db.query_questions(
                grade=grade,
                subject=subject,
                chapters=chapters if chapters else None,
                limit=500
            )

        if not candidates:
            raise ValueError(f"No questions found for Grade {grade} {subject} in chapters: {chapters}")

        # Randomize candidate pool so each generation produces distinct question draws
        random.shuffle(candidates)

        selected_questions_by_sec = {}
        used_ids = set()
        excluded_set = set(exclude_ids or [])
        actual_total_marks = 0.0

        for sec_name, sec_info in sections_spec.items():
            sec_questions = []
            target_count = sec_info["count"]
            target_marks = sec_info["marks_per_q"]
            allowed_formats = sec_info["formats"]

            # Filter matching candidate pool
            pool = [
                q for q in candidates
                if q["id"] not in used_ids
                and (float(q["marks"]) == float(target_marks) or q["question_format"] in allowed_formats)
            ]

            # Prefer questions not in the excluded (previous paper) set for true regeneration
            fresh_pool = [q for q in pool if q["id"] not in excluded_set]
            working_pool = fresh_pool if len(fresh_pool) >= target_count else pool

            # Prioritize matching exact marks first
            exact_mark_pool = [q for q in working_pool if float(q["marks"]) == float(target_marks)]
            
            # Select required number
            chosen = []
            if len(exact_mark_pool) >= target_count:
                chosen = random.sample(exact_mark_pool, target_count)
            else:
                chosen = list(exact_mark_pool)
                # Fill remaining from broader pool
                remaining = [q for q in working_pool if q not in chosen]
                random.shuffle(remaining)
                needed = target_count - len(chosen)
                chosen.extend(remaining[:needed])

            # If still short, fallback to any available unused question in database
            if len(chosen) < target_count:
                extra_needed = target_count - len(chosen)
                fallback_pool = [q for q in candidates if q["id"] not in used_ids and q not in chosen]
                random.shuffle(fallback_pool)
                chosen.extend(fallback_pool[:extra_needed])

            for q in chosen:
                used_ids.add(q["id"])
                actual_total_marks += float(q["marks"])

            selected_questions_by_sec[sec_name] = chosen

        exam_title = title or f"Class {grade} {subject} {spec['title']}"

        result = {
            "title": exam_title,
            "grade_level": grade,
            "subject": subject,
            "exam_type": exam_type,
            "total_marks": int(actual_total_marks),
            "target_marks": total_marks,
            "duration_minutes": spec["duration_minutes"],
            "selected_chapters": chapters,
            "sections": selected_questions_by_sec,
            "question_ids": list(used_ids)
        }
        return result

    @staticmethod
    def swap_single_question(current_question_id: str, excluded_ids: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
        """
        Replace a single question with an equivalent question of same marks and format.
        """
        current_q = db.get_question_by_id(current_question_id)
        if not current_q:
            return None

        excluded = set(excluded_ids or [])
        excluded.add(current_question_id)

        # 1. Search in same chapter with same marks
        same_chapter_cands = db.query_questions(
            grade=current_q["grade_level"],
            subject=current_q["subject"],
            chapters=[current_q["chapter"]],
            question_format=current_q["question_format"],
            limit=30
        )
        valid = [q for q in same_chapter_cands if q["id"] not in excluded and float(q["marks"]) == float(current_q["marks"])]
        if valid:
            return random.choice(valid)

        # 2. Search across subject with same marks & format
        subject_cands = db.query_questions(
            grade=current_q["grade_level"],
            subject=current_q["subject"],
            question_format=current_q["question_format"],
            limit=50
        )
        valid_sub = [q for q in subject_cands if q["id"] not in excluded and float(q["marks"]) == float(current_q["marks"])]
        if valid_sub:
            return random.choice(valid_sub)

        # 3. Search across subject with same marks
        broad_cands = db.query_questions(
            grade=current_q["grade_level"],
            subject=current_q["subject"],
            limit=50
        )
        valid_broad = [q for q in broad_cands if q["id"] not in excluded and float(q["marks"]) == float(current_q["marks"])]
        if valid_broad:
            return random.choice(valid_broad)

        return None
