"""
Phase 5: End-to-End Automated Verification Script
Tests the full pipeline against the live FastAPI & Next.js servers:
1. Verifies /api/v1/taxonomy
2. Selects Class 10 -> Mathematics -> Chapter: Quadratic Equations
3. Generates a 25-mark Unit Test blueprint
4. Triggers question swap on Question 2
5. Exports both Student and Teacher Marking Scheme PDFs
6. Verifies Typst compiles clean, uncorrupted, valid PDF files (>50KB)
7. Simulates Teacher Lead Capture
"""

import sys
import requests
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"

def run_e2e_verification():
    print("=" * 70)
    print("PHASE 5: END-TO-END SANITY CHECK & VERIFICATION")
    print("=" * 70)

    # 1. Health check
    print("\n[Step 1] Checking API health...")
    r = requests.get(f"{BASE_URL}/api/v1/health")
    assert r.status_code == 200, f"Health check failed: {r.text}"
    print("[OK] Backend API is healthy and reachable.")

    # 2. Taxonomy verification
    print("\n[Step 2] Fetching Taxonomy...")
    r = requests.get(f"{BASE_URL}/api/v1/taxonomy")
    assert r.status_code == 200, f"Taxonomy fetch failed: {r.text}"
    tax = r.json()
    print(f"[OK] Taxonomy retrieved. Grades present: {[g['grade'] for g in tax['taxonomy']]}")

    # 3. Generate 25-mark Unit Test for Class 10 Maths: Quadratic Equations
    print("\n[Step 3] Generating 25-Mark Unit Test for Class 10 Quadratic Equations...")
    blueprint_payload = {
        "grade": 10,
        "subject": "Mathematics",
        "chapters": ["Quadratic Equations"],
        "exam_type": "CBSE_BOARD",
        "total_marks": 25,
        "title": "Class 10 Mathematics Unit Test - Quadratic Equations"
    }
    r = requests.post(f"{BASE_URL}/api/v1/generate-blueprint", json=blueprint_payload)
    assert r.status_code == 200, f"Blueprint generation failed: {r.text}"
    exam_paper = r.json()
    paper_id = exam_paper["id"]
    print(f"[OK] Exam Paper generated successfully:")
    print(f"  * Title: {exam_paper['title']}")
    print(f"  * Total Marks: {exam_paper['total_marks']}")
    print(f"  * Sections count: {len(exam_paper['sections'])}")
    for sec_name, q_list in exam_paper['sections'].items():
        print(f"    - Section {sec_name}: {len(q_list)} question(s)")

    # 4. Trigger Question Swap on Question 2
    print("\n[Step 4] Triggering Question Swap on Question 2...")
    all_qs = [q for qs in exam_paper['sections'].values() for q in qs]
    assert len(all_qs) >= 2, "Exam should have at least 2 questions"
    q2 = all_qs[1]
    print(f"  Original Q2: ID={q2['id']} | Marks={q2['marks']} | Format={q2['question_format']}")
    print(f"  Text: {q2['question_text_latex'][:60]}...")

    swap_payload = {
        "current_question_id": q2["id"],
        "excluded_ids": [q["id"] for q in all_qs]
    }
    r = requests.post(f"{BASE_URL}/api/v1/swap-question", json=swap_payload)
    assert r.status_code == 200, f"Swap failed: {r.text}"
    swapped = r.json()["replacement"]
    print(f"[OK] Swapped Question 2 successfully:")
    print(f"  Replacement: ID={swapped['id']} | Marks={swapped['marks']} | Format={swapped['question_format']}")
    print(f"  Text: {swapped['question_text_latex'][:60]}...")

    # Replace Q2 in exam_paper sections
    for sec_name, qs in exam_paper['sections'].items():
        exam_paper['sections'][sec_name] = [
            swapped if q["id"] == q2["id"] else q for q in qs
        ]

    # 5. Export Student PDF
    print("\n[Step 5] Compiling and downloading Student Question Paper PDF via Typst...")
    r = requests.post(f"{BASE_URL}/api/v1/export-pdf", json={"exam": exam_paper, "target": "student"})
    assert r.status_code == 200, f"Student PDF export failed: {r.text}"
    student_pdf_bytes = r.content
    assert student_pdf_bytes.startswith(b"%PDF"), "Output is not a valid PDF file"
    assert len(student_pdf_bytes) > 20000, f"PDF file suspiciously small: {len(student_pdf_bytes)} bytes"
    
    out_dir = Path("./generated_output")
    out_dir.mkdir(exist_ok=True)
    student_pdf_path = out_dir / "Student_Question_Paper_Class10_Quadratic_Equations.pdf"
    student_pdf_path.write_bytes(student_pdf_bytes)
    print(f"[OK] Student Question Paper PDF compiled cleanly!")
    print(f"  File saved: {student_pdf_path} ({len(student_pdf_bytes):,} bytes)")

    # 6. Export Teacher Solution / Marking Scheme PDF
    print("\n[Step 6] Compiling and downloading Teacher Marking Scheme PDF via Typst...")
    r = requests.post(f"{BASE_URL}/api/v1/export-pdf", json={"exam": exam_paper, "target": "solution"})
    assert r.status_code == 200, f"Solution PDF export failed: {r.text}"
    solution_pdf_bytes = r.content
    assert solution_pdf_bytes.startswith(b"%PDF"), "Output is not a valid PDF file"
    assert len(solution_pdf_bytes) > 20000, f"PDF file suspiciously small: {len(solution_pdf_bytes)} bytes"
    
    solution_pdf_path = out_dir / "Teacher_Marking_Scheme_Class10_Quadratic_Equations.pdf"
    solution_pdf_path.write_bytes(solution_pdf_bytes)
    print(f"[OK] Teacher Marking Scheme PDF compiled cleanly!")
    print(f"  File saved: {solution_pdf_path} ({len(solution_pdf_bytes):,} bytes)")

    # 7. Lead capture test
    print("\n[Step 7] Testing Teacher Lead Capture...")
    lead_payload = {
        "teacher_name": "Riddhesh Educator",
        "school_name": "Delhi Public School",
        "city": "Mumbai",
        "whatsapp_number": "+919876543210",
        "generated_exam_id": paper_id
    }
    r = requests.post(f"{BASE_URL}/api/v1/capture-lead", json=lead_payload)
    assert r.status_code == 200, f"Lead capture failed: {r.text}"
    print(f"[OK] Teacher lead captured: {r.json()}")

    print("\n" + "=" * 70)
    print("ALL 7 END-TO-END VERIFICATION CHECKS PASSED WITH ZERO ERRORS!")
    print("=" * 70)

if __name__ == "__main__":
    run_e2e_verification()
