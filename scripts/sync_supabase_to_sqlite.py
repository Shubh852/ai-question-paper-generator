import os
import sqlite3
import json
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_ROLE_KEY"))

all_questions = []
page_size = 1000
start = 0

print("Fetching all questions from Supabase...")
while True:
    res = client.table("master_question_bank").select("*").range(start, start + page_size - 1).execute()
    batch = res.data
    if not batch:
        break
    all_questions.extend(batch)
    print(f"Fetched {len(all_questions)} questions so far...")
    if len(batch) < page_size:
        break
    start += page_size

print(f"\nTotal questions fetched from Supabase: {len(all_questions)}")

conn = sqlite3.connect("data/question_bank.db")
cur = conn.cursor()

# Temporarily remove unique index if needed or use INSERT OR IGNORE / INSERT OR REPLACE
cur.execute("DROP INDEX IF EXISTS idx_content_hash")

inserted = 0
for q in all_questions:
    opts = q.get("options")
    opts_str = json.dumps(opts) if isinstance(opts, (dict, list)) else (opts or "{}")

    rubric = q.get("step_marking_rubric")
    rubric_str = json.dumps(rubric) if isinstance(rubric, (dict, list)) else (rubric or "[]")

    applicable = q.get("applicable_exams")
    applicable_str = json.dumps(applicable) if isinstance(applicable, (dict, list)) else (applicable or '["CBSE_BOARD"]')

    cur.execute("""
        INSERT OR REPLACE INTO master_question_bank (
            id, grade_level, subject, chapter, topic, primary_exam, applicable_exams,
            difficulty_tier, question_format, marks, question_text_latex, options,
            correct_option, ideal_solution_latex, step_marking_rubric, source_book,
            content_hash, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        q.get("id"),
        q.get("grade_level"),
        q.get("subject"),
        q.get("chapter"),
        q.get("topic"),
        q.get("primary_exam", "CBSE_BOARD"),
        applicable_str,
        q.get("difficulty_tier", 2),
        q.get("question_format", "SHORT_ANSWER"),
        q.get("marks", 2.0),
        q.get("question_text_latex", ""),
        opts_str,
        q.get("correct_option"),
        q.get("ideal_solution_latex", ""),
        rubric_str,
        q.get("source_book"),
        q.get("content_hash"),
        q.get("created_at")
    ))
    inserted += 1

conn.commit()
print(f"Successfully synced {inserted} questions to SQLite!")

cur.execute("SELECT grade_level, subject, COUNT(*) FROM master_question_bank GROUP BY grade_level, subject")
rows = cur.fetchall()
print("\n--- UPDATED SQLITE BREAKDOWN ---")
for r in rows:
    print(f"Grade {r[0]} | {r[1]}: {r[2]} questions")
cur.execute("SELECT COUNT(*) FROM master_question_bank")
print(f"\nTOTAL QUESTIONS IN SQLITE NOW: {cur.fetchone()[0]}")
conn.close()
