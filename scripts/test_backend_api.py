import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_endpoints():
    print("Testing GET /api/v1/taxonomy...")
    res = client.get("/api/v1/taxonomy")
    assert res.status_code == 200, res.text
    tax = res.json()["taxonomy"]
    print(f"Taxonomy contains {len(tax)} grade levels.")

    print("\nTesting POST /api/v1/generate-blueprint (25 Marks)...")
    payload = {
        "grade": 10,
        "subject": "Mathematics",
        "chapters": ["Quadratic Equations"],
        "exam_type": "CBSE_BOARD",
        "total_marks": 25,
        "title": "Class 10 Unit Test - Quadratic Equations"
    }
    res = client.post("/api/v1/generate-blueprint", json=payload)
    assert res.status_code == 200, res.text
    paper = res.json()
    print(f"Blueprint generated: '{paper['title']}' with total marks: {paper['total_marks']}")

    sec_a = paper["sections"]["A"]
    assert len(sec_a) > 0, "Section A should have questions"
    target_q_id = sec_a[0]["id"]

    print(f"\nTesting POST /api/v1/swap-question for Q ID: {target_q_id}...")
    swap_res = client.post("/api/v1/swap-question", json={
        "current_question_id": target_q_id,
        "excluded_ids": [q["id"] for qs in paper["sections"].values() for q in qs]
    })
    assert swap_res.status_code == 200, swap_res.text
    swapped_q = swap_res.json()["replacement"]
    print(f"Swapped successfully: new question marks: {swapped_q['marks']}, format: {swapped_q['question_format']}")

    print("\nTesting POST /api/v1/export-pdf (Student PDF)...")
    export_stud = client.post("/api/v1/export-pdf", json={"exam": paper, "target": "student"})
    assert export_stud.status_code == 200, export_stud.text
    assert export_stud.headers["content-type"] == "application/pdf"
    print(f"Student PDF bytes received: {len(export_stud.content)} bytes.")

    print("\nTesting POST /api/v1/export-pdf (Solution PDF)...")
    export_sol = client.post("/api/v1/export-pdf", json={"exam": paper, "target": "solution"})
    assert export_sol.status_code == 200, export_sol.text
    assert export_sol.headers["content-type"] == "application/pdf"
    print(f"Solution PDF bytes received: {len(export_sol.content)} bytes.")

    print("\nTesting POST /api/v1/capture-lead...")
    lead_res = client.post("/api/v1/capture-lead", json={
        "teacher_name": "Riddhesh",
        "school_name": "Kendriya Vidyalaya",
        "city": "Mumbai",
        "whatsapp_number": "+919876543210",
        "generated_exam_id": paper["id"]
    })
    assert lead_res.status_code == 200, lead_res.text
    print("Lead captured:", lead_res.json())

    print("\nALL BACKEND API TESTS PASSED SUCCESSFULLY! Phase 3 complete!")

if __name__ == "__main__":
    test_endpoints()
