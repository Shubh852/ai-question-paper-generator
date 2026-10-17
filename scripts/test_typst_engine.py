import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

import tempfile
import typst
from engine.typesetter import sanitize_typst_text, compile_to_pdf, generate_student_typst, generate_solution_typst
from engine.assembler import ExamAssembler

def run_test():
    print("Testing Assembler...")
    exam = ExamAssembler.assemble_paper(
        grade=10,
        subject="Mathematics",
        chapters=["Quadratic Equations"],
        total_marks=25
    )
    print(f"Exam assembled: {exam['title']} with {len(exam['question_ids'])} questions.")
    
    student_typ = generate_student_typst(exam, exam['sections'])
    print(f"Generated student typst ({len(student_typ)} chars). Writing to test_output.typ...")
    Path("test_output.typ").write_text(student_typ, encoding="utf-8")
    student_pdf = compile_to_pdf(student_typ, "test_student.pdf")
    print(f"Student PDF compiled successfully! Size: {len(student_pdf)} bytes.")

    solution_typ = generate_solution_typst(exam, exam['sections'])
    print(f"Generated solution typst ({len(solution_typ)} chars). Compiling...")
    solution_pdf = compile_to_pdf(solution_typ, "test_solution.pdf")
    print(f"Solution PDF compiled successfully! Size: {len(solution_pdf)} bytes.")

    # Test swap
    first_q_id = exam['question_ids'][0]
    swapped = ExamAssembler.swap_single_question(first_q_id, excluded_ids=exam['question_ids'])
    print(f"Question swap test: {first_q_id} -> {swapped['id'] if swapped else 'None'}")

if __name__ == "__main__":
    run_test()
