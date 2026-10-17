# 🎓 CBSE PaperGen: Autonomous AI Question Paper Generation System

> An autonomous, full-stack educational assessment engine that compiles print-ready CBSE Board examination question papers and step-by-step marking schemes using **FastAPI**, **Next.js (React 18 & Tailwind CSS)**, **Typst**, and **Supabase PostgreSQL**.

---

## 🚀 Key Features

* **NCERT & CBSE Blueprint Alignment:** Strictly adheres to official CBSE Board examination structures for Classes 10, 11, and 12 across Science, Mathematics, Physics, Chemistry, Biology, Social Science, and English.
* **Flexible Preset & Custom Exam Patterns:**
  * **15 Marks:** Class Test / Weekly Quiz (35 Mins) — 5 MCQs (5M) + 2 SA-I (4M) + 2 SA-II (6M).
  * **20 Marks:** Periodic Test I (45 Mins).
  * **25 Marks:** Unit Assessment Test (60 Mins).
  * **40 Marks:** Periodic Assessment II (90 Mins).
  * **50 Marks:** Mid-Term Examination (120 Mins).
  * **70 Marks:** CBSE Science Theory (180 Mins).
  * **80 Marks:** Full Board Examination (180 Mins).
  * **Custom Marks Solver:** Exact integer partition solver for any custom mark total (e.g. 10M, 30M, 100M).
* **📐 Embedded Scientific & Circuit Diagrams:**
  * Physics: Balanced Wheatstone bridge, series-parallel resistor networks, prism ray refraction, convex lens image formation, logic gates combination.
  * Chemistry: Daniell Galvanic cell, electrolytic copper refining, benzene resonance structure.
  * Biology: Human heart double circulation schematic, nephron filtration apparatus, stomatal pore.
  * Mathematics: Tangents from an external point to a circle, trigonometric heights & distances.
* **🏫 Custom School Branding & Logo Header:**
  * Teachers can upload their custom school crest/logo (PNG, JPG, SVG, WebP) or choose the default school emblem.
  * Generates branded official headers for both student question papers and evaluator marking schemes.
* **📚 "My Saved Papers" History Dashboard:**
  * Revisit, filter, search, and re-download past generated examination papers anytime.
  * One-click "Open & Customize in Editor" to load past papers directly back into the preview studio.
* **⚡ Lightning-Fast Typst PDF Compilation:**
  * Renders publication-grade A4 PDFs with native vector math and diagrams in under 200ms.
* **☁️ Dual Storage Architecture:**
  * Primary: High-performance cloud PostgreSQL on **Supabase Cloud** (2,760+ questions).
  * Fallback: Local offline SQLite database (`data/question_bank.db`).

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python 3.11), Uvicorn, Pydantic v2, Python Typst bindings (`typst`), `python-multipart`.
* **Frontend:** Next.js 14, React 18, TypeScript, Tailwind CSS, KaTeX, Lucide React icons.
* **Database:** Supabase Cloud PostgreSQL with Row-Level Security, fallback to SQLite.
* **Typesetting Engine:** Typst CLI & Native Python Bindings.

---

## 🏁 Quickstart Guide

### 1. Prerequisites
* Python 3.10+
* Node.js 18+

### 2. Environment Setup
Create a `.env` file in the root directory (see `.env.example`):
```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_ANON_KEY=your-anon-key
```

### 3. Backend Setup
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

### 4. Frontend Setup
```bash
cd frontend
npm install
npm run build
npm start
```
Frontend will be live at `http://localhost:3000`.

---

## 📁 Repository Structure

```
├── backend/
│   ├── database.py         # Database abstraction layer (Supabase + SQLite fallback)
│   └── main.py             # FastAPI REST endpoints & static file mounting
├── data/
│   ├── diagrams/           # Vector SVG scientific figures & diagrams
│   ├── logos/              # Uploaded school logos & emblems
│   └── question_bank.db    # Standalone offline SQLite database
├── engine/
│   ├── assembler.py        # Blueprint constraint solver & question picker
│   └── typesetter.py       # Typst PDF compiler for student & teacher schemes
├── frontend/
│   ├── app/                # Next.js App Router (page.tsx, layout.tsx)
│   ├── components/         # Wizard, SavedPapersDashboard, LatexRenderer
│   └── public/             # Static diagrams, logos, and web assets
├── scripts/                # Database migrations, bulk question ingestion
├── requirements.txt        # Python backend dependencies
└── README.md
```

---

## 📄 License
MIT License. Created for educators, schools, and academic institutions.
