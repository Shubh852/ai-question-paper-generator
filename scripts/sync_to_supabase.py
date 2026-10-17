"""
Utility script to sync local SQLite questions into Supabase PostgreSQL cloud.
Run this script after running scripts/supabase_schema.sql in your Supabase SQL Editor.
"""

import os
import sys
import json
import sqlite3
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("sync_supabase")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

ROOT_DIR = Path(__file__).resolve().parent.parent
SQLITE_DB = ROOT_DIR / "data" / "question_bank.db"

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

def sync():
    if not SUPABASE_URL or not SUPABASE_KEY:
        logger.error("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env")
        return

    from supabase import create_client
    client = create_client(SUPABASE_URL, SUPABASE_KEY)

    if not SQLITE_DB.exists():
        logger.error(f"Local database not found at {SQLITE_DB}")
        return

    conn = sqlite3.connect(SQLITE_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM master_question_bank")
    rows = cursor.fetchall()
    logger.info(f"Loaded {len(rows)} questions from local SQLite database.")

    records = []
    for r in rows:
        d = dict(r)
        if d.get("options"):
            try: d["options"] = json.loads(d["options"])
            except Exception: pass
        if d.get("applicable_exams"):
            try: d["applicable_exams"] = json.loads(d["applicable_exams"])
            except Exception: pass
        if d.get("step_marking_rubric"):
            try: d["step_marking_rubric"] = json.loads(d["step_marking_rubric"])
            except Exception: pass
        records.append(d)

    try:
        res = client.table("master_question_bank").upsert(records, on_conflict="content_hash").execute()
        count = len(res.data) if res.data else len(records)
        logger.info(f"Successfully synced {count} questions to Supabase cloud table 'master_question_bank'!")
    except Exception as e:
        logger.error(f"Sync failed: {e}")
        logger.info("Make sure you have executed scripts/supabase_schema.sql in the Supabase SQL editor.")

if __name__ == "__main__":
    sync()
