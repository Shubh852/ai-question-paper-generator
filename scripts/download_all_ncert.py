"""
Automated NCERT Scraper Catalog & Downloader
Downloads official NCERT chapter PDFs from NCERT CDN:
https://ncert.nic.in/textbook/pdf/{prefix}{chapter_2digit}.pdf
"""

import os
import sys
import time
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ncert_scraper")

NCERT_CATALOG = [
    # Class 10
    {
        "grade": 10,
        "subject": "Mathematics",
        "book": "Mathematics",
        "prefix": "jemh1",
        "start": 1,
        "end": 14,
        "folder": "Class_10_Mathematics",
    },
    {
        "grade": 10,
        "subject": "Science",
        "book": "Science",
        "prefix": "jesc1",
        "start": 1,
        "end": 13,
        "folder": "Class_10_Science",
    },
    {
        "grade": 10,
        "subject": "English",
        "book": "First Flight",
        "prefix": "jeff1",
        "start": 1,
        "end": 9,
        "folder": "Class_10_English_First_Flight",
    },
    {
        "grade": 10,
        "subject": "English",
        "book": "Footprints Without Feet",
        "prefix": "jefp1",
        "start": 1,
        "end": 9,
        "folder": "Class_10_English_Footprints",
    },
    {
        "grade": 10,
        "subject": "Social Science",
        "book": "India and the Contemporary World II (History)",
        "prefix": "jess1",
        "start": 1,
        "end": 5,
        "folder": "Class_10_SST_History",
    },
    {
        "grade": 10,
        "subject": "Social Science",
        "book": "Contemporary India II (Geography)",
        "prefix": "jess2",
        "start": 1,
        "end": 7,
        "folder": "Class_10_SST_Geography",
    },
    {
        "grade": 10,
        "subject": "Social Science",
        "book": "Democratic Politics II (Civics)",
        "prefix": "jess3",
        "start": 1,
        "end": 5,
        "folder": "Class_10_SST_Civics",
    },
    {
        "grade": 10,
        "subject": "Social Science",
        "book": "Understanding Economic Development (Economics)",
        "prefix": "jess4",
        "start": 1,
        "end": 5,
        "folder": "Class_10_SST_Economics",
    },

    # Class 11
    {
        "grade": 11,
        "subject": "Mathematics",
        "book": "Mathematics",
        "prefix": "kemh1",
        "start": 1,
        "end": 14,
        "folder": "Class_11_Mathematics",
    },
    {
        "grade": 11,
        "subject": "Physics",
        "book": "Physics Part 1",
        "prefix": "keph1",
        "start": 1,
        "end": 7,
        "folder": "Class_11_Physics_Part_1",
    },
    {
        "grade": 11,
        "subject": "Physics",
        "book": "Physics Part 2",
        "prefix": "keph2",
        "start": 1,
        "end": 7,
        "folder": "Class_11_Physics_Part_2",
    },
    {
        "grade": 11,
        "subject": "Chemistry",
        "book": "Chemistry Part 1",
        "prefix": "kech1",
        "start": 1,
        "end": 6,
        "folder": "Class_11_Chemistry_Part_1",
    },
    {
        "grade": 11,
        "subject": "Chemistry",
        "book": "Chemistry Part 2",
        "prefix": "kech2",
        "start": 1,
        "end": 6,
        "folder": "Class_11_Chemistry_Part_2",
    },
    {
        "grade": 11,
        "subject": "Biology",
        "book": "Biology",
        "prefix": "kebo1",
        "start": 1,
        "end": 19,
        "folder": "Class_11_Biology",
    },
    {
        "grade": 11,
        "subject": "English",
        "book": "Hornbill",
        "prefix": "keeh1",
        "start": 1,
        "end": 8,
        "folder": "Class_11_English_Hornbill",
    },
    {
        "grade": 11,
        "subject": "English",
        "book": "Snapshots",
        "prefix": "kees1",
        "start": 1,
        "end": 5,
        "folder": "Class_11_English_Snapshots",
    },

    # Class 12
    {
        "grade": 12,
        "subject": "Mathematics",
        "book": "Mathematics Part 1",
        "prefix": "lemh1",
        "start": 1,
        "end": 6,
        "folder": "Class_12_Mathematics_Part_1",
    },
    {
        "grade": 12,
        "subject": "Mathematics",
        "book": "Mathematics Part 2",
        "prefix": "lemh2",
        "start": 1,
        "end": 7,
        "folder": "Class_12_Mathematics_Part_2",
    },
    {
        "grade": 12,
        "subject": "Physics",
        "book": "Physics Part 1",
        "prefix": "leph1",
        "start": 1,
        "end": 8,
        "folder": "Class_12_Physics_Part_1",
    },
    {
        "grade": 12,
        "subject": "Physics",
        "book": "Physics Part 2",
        "prefix": "leph2",
        "start": 1,
        "end": 6,
        "folder": "Class_12_Physics_Part_2",
    },
    {
        "grade": 12,
        "subject": "Chemistry",
        "book": "Chemistry Part 1",
        "prefix": "lech1",
        "start": 1,
        "end": 5,
        "folder": "Class_12_Chemistry_Part_1",
    },
    {
        "grade": 12,
        "subject": "Chemistry",
        "book": "Chemistry Part 2",
        "prefix": "lech2",
        "start": 1,
        "end": 5,
        "folder": "Class_12_Chemistry_Part_2",
    },
    {
        "grade": 12,
        "subject": "Biology",
        "book": "Biology",
        "prefix": "lebo1",
        "start": 1,
        "end": 13,
        "folder": "Class_12_Biology",
    },
    {
        "grade": 12,
        "subject": "English",
        "book": "Flamingo",
        "prefix": "lefl1",
        "start": 1,
        "end": 13,
        "folder": "Class_12_English_Flamingo",
    },
    {
        "grade": 12,
        "subject": "English",
        "book": "Vistas",
        "prefix": "levi1",
        "start": 1,
        "end": 6,
        "folder": "Class_12_English_Vistas",
    },
]

BASE_URL = "https://ncert.nic.in/textbook/pdf/{prefix}{chapter_2digit}.pdf"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://ncert.nic.in/textbook.php",
}

def download_file_with_retry(url: str, dest_path: Path, max_retries: int = 3, timeout: int = 30) -> bool:
    """Download a file with retry and validation."""
    if dest_path.exists() and dest_path.stat().st_size > 1024:
        try:
            with open(dest_path, "rb") as f:
                header = f.read(5)
                if header.startswith(b"%PDF"):
                    logger.info(f"Already exists & valid: {dest_path.name}")
                    return True
        except Exception:
            pass

    dest_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Downloading {url} (Attempt {attempt}/{max_retries})...")
            response = requests.get(url, headers=HEADERS, timeout=timeout)
            if response.status_code == 200:
                content = response.content
                if len(content) > 1024 and content.startswith(b"%PDF"):
                    dest_path.write_bytes(content)
                    size_kb = len(content) // 1024
                    logger.info(f"Downloaded successfully: {dest_path.name} ({size_kb} KB)")
                    return True
                else:
                    logger.warning(f"Response invalid (size={len(content)}, pdf_header={content[:5]}): {url}")
            elif response.status_code == 404:
                logger.warning(f"HTTP 404 Not Found: {url}")
                return False
            else:
                logger.warning(f"HTTP {response.status_code} for {url}")
        except Exception as e:
            logger.warning(f"Error downloading {url}: {e}")
        
        time.sleep(1.5 * attempt)

    return False

def download_entry(entry: dict, base_dir: Path, chapters: Optional[List[int]] = None):
    prefix = entry["prefix"]
    folder_name = entry["folder"]
    target_dir = base_dir / folder_name
    start_ch = entry["start"]
    end_ch = entry["end"]

    logger.info(f"=== Scraping {entry['grade']} | {entry['book']} ({prefix}) ===")
    selected_chapters = chapters if chapters else list(range(start_ch, end_ch + 1))

    for ch in selected_chapters:
        ch_str = f"{ch:02d}"
        url = BASE_URL.format(prefix=prefix, chapter_2digit=ch_str)
        filename = f"{prefix}{ch_str}.pdf"
        dest_path = target_dir / filename
        download_file_with_retry(url, dest_path)
        time.sleep(0.3)

def main():
    parser = argparse.ArgumentParser(description="Download NCERT Chapter PDFs")
    parser.add_argument("--base-dir", type=str, default="./seed_materials", help="Root directory for PDFs")
    parser.add_argument("--prefix", type=str, help="Filter by specific book prefix (e.g., jemh1, leph1)")
    parser.add_argument("--grade", type=int, choices=[10, 11, 12], help="Filter by grade")
    parser.add_argument("--subject", type=str, help="Filter by subject")
    parser.add_argument("--quick-seed", action="store_true", help="Seed initial Class 10 Maths & Class 12 Physics")
    parser.add_argument("--chapters", type=int, nargs="+", help="Specific chapter numbers")
    args = parser.parse_args()

    base_dir = Path(args.base_dir).resolve()
    base_dir.mkdir(parents=True, exist_ok=True)

    if args.quick_seed:
        logger.info("Executing Quick Seed: Class 10 Maths (jemh1) and Class 12 Physics Part 1 (leph1)...")
        targets = [e for e in NCERT_CATALOG if e["prefix"] in ["jemh1", "leph1"]]
        for t in targets:
            # Download first 4 chapters for quick testing
            download_entry(t, base_dir, chapters=[1, 2, 3, 4])
        logger.info("Quick seed complete!")
        return

    targets = NCERT_CATALOG
    if args.prefix:
        targets = [e for e in targets if e["prefix"].lower() == args.prefix.lower()]
    if args.grade:
        targets = [e for e in targets if e["grade"] == args.grade]
    if args.subject:
        targets = [e for e in targets if args.subject.lower() in e["subject"].lower()]

    if not targets:
        logger.error("No catalog entries matched your filters.")
        return

    logger.info(f"Starting download for {len(targets)} book catalog entries...")
    for t in targets:
        download_entry(t, base_dir, chapters=args.chapters)

if __name__ == "__main__":
    main()
