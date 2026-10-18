"""
FastAPI Backend Application for AI Question Paper Generation System.
Provides endpoints for taxonomy, blueprint generation, question swapping,
PDF compilation via Typst, school branding/logo uploads, and saved paper dashboards.
"""

import os
import sys
import uuid
import base64
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

from fastapi import FastAPI, HTTPException, Response, Query, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

# Ensure ROOT_DIR in PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.database import db
from engine.assembler import ExamAssembler, BLUEPRINT_PRESETS
from engine.typesetter import generate_student_typst, generate_solution_typst, compile_to_pdf

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("api")

app = FastAPI(
    title="Autonomous Question Paper Generator API",
    version="1.0.0",
    description="Backend API for CBSE Question Paper Generation with Typst PDF Compiler, Branding, and Diagrams"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure static directories exist and mount
DIAGRAMS_DIR = ROOT_DIR / "data" / "diagrams"
LOGOS_DIR = ROOT_DIR / "data" / "logos"
DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)
LOGOS_DIR.mkdir(parents=True, exist_ok=True)

app.mount("/diagrams", StaticFiles(directory=str(DIAGRAMS_DIR)), name="diagrams")
app.mount("/logos", StaticFiles(directory=str(LOGOS_DIR)), name="logos")

# --- Pydantic Request / Response Models ---
class BlueprintRequest(BaseModel):
    grade: int = Field(..., ge=10, le=12, example=10)
    subject: str = Field(..., example="Mathematics")
    chapters: List[str] = Field(..., example=["Quadratic Equations", "Real Numbers"])
    topics: Optional[List[str]] = Field(default=None, example=["Dimensional Analysis"])
    exam_type: str = Field(default="CBSE_BOARD", example="CBSE_BOARD")
    total_marks: int = Field(default=25, example=25)
    difficulty: Optional[Dict[str, float]] = Field(default={"easy": 40, "medium": 40, "hard": 20})
    title: Optional[str] = Field(default=None, example="Unit Assessment Test")
    school_name: Optional[str] = Field(default=None, example="Delhi Public School")
    school_logo: Optional[str] = Field(default=None, example="data/logos/default_school_logo.svg")
    exclude_question_ids: Optional[List[str]] = Field(default=None, example=[])
    created_by: Optional[str] = Field(default=None, example="Dr. Ananya Sharma")

class TeacherSignupRequest(BaseModel):
    name: str = Field(..., example="Dr. Ananya Sharma")
    school: str = Field(..., example="Delhi Public School")
    city: str = Field(..., example="New Delhi")
    email: str = Field(..., example="ananya.sharma@dps.edu.in")
    whatsapp: str = Field(..., example="+919876543210")
    password: Optional[str] = Field(default="")
    primary_grade: Optional[int] = Field(default=10)
    primary_subject: Optional[str] = Field(default="Mathematics")

class TeacherLoginRequest(BaseModel):
    email_or_phone: str = Field(..., example="ananya.sharma@dps.edu.in")
    password: Optional[str] = Field(default="")

class SwapQuestionRequest(BaseModel):
    current_question_id: str
    excluded_ids: Optional[List[str]] = []

class LeadCaptureRequest(BaseModel):
    teacher_name: str = Field(..., example="Dr. Ananya Sharma")
    school_name: str = Field(..., example="Delhi Public School")
    city: str = Field(..., example="New Delhi")
    whatsapp_number: str = Field(..., example="+919876543210")
    generated_exam_id: Optional[str] = None

class ExportPdfRequest(BaseModel):
    exam: Dict[str, Any]
    target: str = Field(default="student", description="'student' or 'solution' or 'both'")

# In-memory storage for active paper previews
GENERATED_PAPERS_CACHE: Dict[str, Dict[str, Any]] = {}

@app.get("/")
def read_root():
    return {
        "system": "Autonomous AI Question Paper Generator",
        "status": "online",
        "version": "1.1.0",
        "database": "PostgreSQL (Supabase)" if db.use_supabase else "Local SQLite Engine",
        "diagrams_available": len(list(DIAGRAMS_DIR.glob("*"))),
        "logos_available": len(list(LOGOS_DIR.glob("*")))
    }

@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy", "timestamp": "2026-10-18T01:00:00Z"}

@app.get("/api/v1/taxonomy")
def get_taxonomy():
    """
    Returns grades, subjects, and available chapters with question counts and topics.
    """
    raw = db.get_taxonomy()
    response = []

    for grade_str in sorted(raw.keys(), key=lambda x: int(x)):
        grade_num = int(grade_str)
        subjects_data = raw[grade_str]
        sub_list = []

        for sub_name, chapters_dict in subjects_data.items():
            chap_list = []
            total_subj_qs = 0
            for c_name, c_info in chapters_dict.items():
                if isinstance(c_info, dict):
                    c_count = c_info.get("count", 0)
                    topics_dict = c_info.get("topics", {})
                    top_list = [{"name": t_name, "count": t_cnt} for t_name, t_cnt in sorted(topics_dict.items())]
                else:
                    c_count = int(c_info)
                    top_list = []
                total_subj_qs += c_count
                chap_list.append({
                    "name": c_name,
                    "count": c_count,
                    "topics": top_list
                })

            sub_list.append({
                "subject": sub_name,
                "total_questions": total_subj_qs,
                "chapters": chap_list
            })

        response.append({
            "grade": grade_num,
            "subjects": sub_list
        })

    return {"taxonomy": response, "presets": BLUEPRINT_PRESETS}

@app.post("/api/v1/upload-logo")
async def upload_logo(file: UploadFile = File(...)):
    """
    Upload custom school logo for branded PDF generation.
    Supports PNG, JPG, JPEG, SVG, WebP.
    """
    allowed_exts = {".png", ".jpg", ".jpeg", ".svg", ".webp"}
    ext = Path(file.filename).suffix.lower() if file.filename else ".png"
    if ext not in allowed_exts:
        raise HTTPException(status_code=400, detail="Invalid format. Allowed: PNG, JPG, SVG, WebP.")

    safe_name = f"logo_{uuid.uuid4().hex[:8]}{ext}"
    target_data = LOGOS_DIR / safe_name
    pub_dir = ROOT_DIR / "frontend" / "public" / "logos"
    pub_dir.mkdir(parents=True, exist_ok=True)
    target_pub = pub_dir / safe_name

    contents = await file.read()
    target_data.write_bytes(contents)
    try:
        target_pub.write_bytes(contents)
    except Exception:
        pass

    logger.info(f"Uploaded school logo saved: {safe_name}")
    return {
        "status": "success",
        "filename": safe_name,
        "url": f"/logos/{safe_name}",
        "relative_path": f"data/logos/{safe_name}"
    }

@app.post("/api/v1/generate-blueprint")
def generate_blueprint(req: BlueprintRequest):
    """
    Generate a balanced question list for teacher preview matching blueprint constraints.
    """
    try:
        paper = ExamAssembler.assemble_paper(
            grade=req.grade,
            subject=req.subject,
            chapters=req.chapters,
            topics=req.topics,
            exam_type=req.exam_type,
            total_marks=req.total_marks,
            difficulty_weights=req.difficulty,
            title=req.title,
            exclude_ids=req.exclude_question_ids
        )

        paper_id = str(uuid.uuid4())
        paper["id"] = paper_id
        paper["school_name"] = req.school_name or "CENTRAL BOARD OF SECONDARY EDUCATION"
        paper["school_logo"] = req.school_logo or "data/logos/default_school_logo.svg"
        paper["created_by"] = req.created_by or "Verified Educator"

        # Save to database record
        db.save_generated_exam({
            "id": paper_id,
            "title": paper["title"],
            "grade_level": req.grade,
            "subject": req.subject,
            "total_marks": paper["total_marks"],
            "duration_minutes": paper["duration_minutes"],
            "exam_type": req.exam_type,
            "selected_chapters": req.chapters,
            "blueprint_breakdown": {s: len(qs) for s, qs in paper["sections"].items()},
            "question_ids": paper["question_ids"],
            "student_pdf_url": f"/api/v1/download-pdf/{paper_id}?doc=student",
            "solution_pdf_url": f"/api/v1/download-pdf/{paper_id}?doc=solution",
            "created_by": paper["created_by"]
        })

        GENERATED_PAPERS_CACHE[paper_id] = paper
        return paper
    except Exception as e:
        logger.error(f"Error assembling paper: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/swap-question")
def swap_question(req: SwapQuestionRequest):
    """
    Replaces a single question in the preview with an equivalent question.
    """
    new_q = ExamAssembler.swap_single_question(
        current_question_id=req.current_question_id,
        excluded_ids=req.excluded_ids
    )
    if not new_q:
        raise HTTPException(status_code=404, detail="No alternative question matching marks and format found.")
    return {"replacement": new_q}

@app.post("/api/v1/export-pdf")
def export_pdf(req: ExportPdfRequest):
    """
    Compiles and returns base64 or direct binary PDF with school branding and diagrams.
    """
    try:
        exam = req.exam
        target = req.target.lower()

        if target == "student":
            typst_code = generate_student_typst(exam, exam.get("sections", {}))
            pdf_bytes = compile_to_pdf(typst_code)
            return Response(
                content=pdf_bytes,
                media_type="application/pdf",
                headers={"Content-Disposition": f"attachment; filename=Question_Paper_{exam.get('grade_level', 10)}_{exam.get('subject', 'Paper')}.pdf"}
            )
        elif target == "solution":
            typst_code = generate_solution_typst(exam, exam.get("sections", {}))
            pdf_bytes = compile_to_pdf(typst_code)
            return Response(
                content=pdf_bytes,
                media_type="application/pdf",
                headers={"Content-Disposition": f"attachment; filename=Marking_Scheme_{exam.get('grade_level', 10)}_{exam.get('subject', 'Paper')}.pdf"}
            )
        else:
            # Return both as base64
            stud_typ = generate_student_typst(exam, exam.get("sections", {}))
            sol_typ = generate_solution_typst(exam, exam.get("sections", {}))
            stud_pdf = compile_to_pdf(stud_typ)
            sol_pdf = compile_to_pdf(sol_typ)
            return {
                "student_pdf_base64": base64.b64encode(stud_pdf).decode("utf-8"),
                "solution_pdf_base64": base64.b64encode(sol_pdf).decode("utf-8")
            }
    except Exception as e:
        logger.error(f"Error compiling PDF: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"PDF compilation failed: {e}")

@app.get("/api/v1/download-pdf/{paper_id}")
def download_pdf(paper_id: str, doc: str = Query("student")):
    """
    Direct GET download endpoint for generated paper.
    Rehydrates from database if not present in memory.
    """
    paper = GENERATED_PAPERS_CACHE.get(paper_id)
    if not paper:
        paper = db.get_saved_exam_by_id(paper_id)
        if paper:
            GENERATED_PAPERS_CACHE[paper_id] = paper
        else:
            raise HTTPException(status_code=404, detail="Paper not found.")

    if doc == "solution":
        typst_code = generate_solution_typst(paper, paper.get("sections", {}))
        filename = f"Marking_Scheme_{paper.get('grade_level')}_{paper.get('subject')}.pdf"
    else:
        typst_code = generate_student_typst(paper, paper.get("sections", {}))
        filename = f"Question_Paper_{paper.get('grade_level')}_{paper.get('subject')}.pdf"

    pdf_bytes = compile_to_pdf(typst_code)
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

# --- My Saved Papers Endpoints ---
@app.get("/api/v1/saved-exams")
def list_saved_exams(limit: int = 50):
    """
    Fetches past generated exam papers for the teacher dashboard.
    """
    exams = db.get_saved_exams(limit=limit)
    return {"exams": exams, "count": len(exams)}

@app.get("/api/v1/saved-exams/{exam_id}")
def get_saved_exam_details(exam_id: str):
    """
    Retrieves full exam structure with hydrated questions and sections.
    """
    exam = db.get_saved_exam_by_id(exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Saved exam not found.")
    GENERATED_PAPERS_CACHE[exam_id] = exam
    return exam

@app.delete("/api/v1/saved-exams/{exam_id}")
def delete_saved_exam(exam_id: str):
    """
    Deletes an exam from saved history.
    """
    success = db.delete_saved_exam(exam_id)
    if not success:
        raise HTTPException(status_code=404, detail="Exam not found or could not be deleted.")
    GENERATED_PAPERS_CACHE.pop(exam_id, None)
    return {"status": "success", "message": "Exam deleted successfully."}

@app.post("/api/v1/capture-lead")
def capture_lead(req: LeadCaptureRequest):
    """
    Saves teacher contact info into teacher_leads before full download.
    """
    try:
        lead_id = db.save_teacher_lead({
            "teacher_name": req.teacher_name,
            "school_name": req.school_name,
            "city": req.city,
            "whatsapp_number": req.whatsapp_number,
            "generated_exam_id": req.generated_exam_id
        })
        return {
            "status": "success",
            "lead_id": lead_id,
            "message": "Lead captured successfully. Full unwatermarked PDF download unlocked!"
        }
    except Exception as e:
        logger.error(f"Lead capture failed: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

# --- Teacher Authentication Endpoints ---
@app.post("/api/v1/auth/signup")
def teacher_signup(req: TeacherSignupRequest):
    """
    Registers a new verified educator account and unlocks studio access.
    """
    try:
        user = db.register_teacher({
            "name": req.name,
            "school": req.school,
            "city": req.city,
            "email": req.email,
            "whatsapp": req.whatsapp,
            "password": req.password,
            "primary_grade": req.primary_grade,
            "primary_subject": req.primary_subject
        })
        return {
            "status": "success",
            "message": "Teacher account registered successfully.",
            "user": user
        }
    except Exception as e:
        logger.error(f"Signup error: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=f"Registration error: {e}")

@app.post("/api/v1/auth/login")
def teacher_login(req: TeacherLoginRequest):
    """
    Authenticates teacher by email or WhatsApp number.
    """
    user = db.login_teacher(email_or_phone=req.email_or_phone, password=req.password)
    if not user:
        # If not registered, create profile seamlessly on demand
        user = db.register_teacher({
            "name": req.email_or_phone.split("@")[0].capitalize() if "@" in req.email_or_phone else "Educator",
            "school": "Delhi Public School",
            "city": "New Delhi",
            "email": req.email_or_phone if "@" in req.email_or_phone else f"{req.email_or_phone}@school.edu",
            "whatsapp": req.email_or_phone if not "@" in req.email_or_phone else "+919876543210",
        })
    return {
        "status": "success",
        "message": "Welcome back, Educator!",
        "user": user
    }

@app.get("/api/v1/auth/demo")
def teacher_demo():
    """
    Returns instant guest teacher credentials for testing and evaluation.
    """
    return {
        "status": "success",
        "user": {
            "id": "tch_demo_dps",
            "name": "Dr. Ananya Sharma",
            "school": "Delhi Public School, R.K. Puram",
            "city": "New Delhi",
            "email": "ananya.sharma@dps.edu.in",
            "whatsapp": "+91 98765 43210",
            "primary_grade": 10,
            "primary_subject": "Mathematics"
        }
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=False)
