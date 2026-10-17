# Autonomous AI Question Paper Generation System (CBSE & Competitive)
## Technical Specification & Architecture Manual

### 1. Project Overview & Scope
An automated question paper generation platform covering Classes 10, 11, and 12 for CBSE Board exams and Competitive exams (IIT-JEE Main/Advanced, NEET). The system provides teachers with an interactive 4-step wizard to create customized question papers and step-wise marking schemes compiled via Typst into print-ready PDFs.

#### Supported Grade & Subject Matrix
* **Class 10:**
  * Mathematics (`jemh1`)
  * Science (Physics, Chemistry, Biology combined) (`jesc1`)
  * Social Science (History `jess1`, Geography `jess2`, Democratic Politics `jess3`, Economics `jess4`)
  * English (First Flight `jeff1`, Footprints Without Feet `jefp1`)
* **Class 11 & Class 12:**
  * Mathematics (11: `kemh1`, 12: `lemh1`, `lemh2`)
  * Physics (11: `keph1`, `keph2`, 12: `leph1`, `leph2`)
  * Chemistry (11: `kech1`, `kech2`, 12: `lech1`, `lech2`)
  * Biology (11: `kebo1`, 12: `lebo1`)
  * English Core (11: `keeh1`, `kees1`, 12: `lefl1`, `levi1`)
* **Target Exams:**
  * CBSE Board Standard (Strict NCERT & Board Blueprint)
  * Competitive Exam (IIT-JEE Main, JEE Advanced, NEET)
  * Hybrid Mode (e.g., 60% Board Foundation + 40% JEE/NEET Application)

---

### 2. Complete NCERT Automated Scraper Catalog
Base URL: `https://ncert.nic.in/textbook/pdf/{prefix}{chapter_2digit}.pdf`

| Grade | Subject & Book Title | NCERT Code Prefix | Chapters |
| :--- | :--- | :--- | :--- |
| **Class 10** | Mathematics | `jemh1` | 01 to 14 |
| **Class 10** | Science | `jesc1` | 01 to 13 |
| **Class 10** | English: First Flight | `jeff1` | 01 to 09 |
| **Class 10** | English: Footprints Without Feet | `jefp1` | 01 to 09 |
| **Class 10** | SST: India and the Contemporary World II (History) | `jess1` | 01 to 05 |
| **Class 10** | SST: Contemporary India II (Geography) | `jess2` | 01 to 07 |
| **Class 10** | SST: Democratic Politics II (Civics) | `jess3` | 01 to 05 |
| **Class 10** | SST: Understanding Economic Development (Economics) | `jess4` | 01 to 05 |
| **Class 11** | Mathematics | `kemh1` | 01 to 14 |
| **Class 11** | Physics (Part 1) | `keph1` | 01 to 07 |
| **Class 11** | Physics (Part 2) | `keph2` | 01 to 07 |
| **Class 11** | Chemistry (Part 1) | `kech1` | 01 to 06 |
| **Class 11** | Chemistry (Part 2) | `kech2` | 01 to 06 |
| **Class 11** | Biology | `kebo1` | 01 to 19 |
| **Class 11** | English: Hornbill | `keeh1` | 01 to 08 |
| **Class 11** | English: Snapshots | `kees1` | 01 to 05 |
| **Class 12** | Mathematics (Part 1) | `lemh1` | 01 to 06 |
| **Class 12** | Mathematics (Part 2) | `lemh2` | 01 to 07 |
| **Class 12** | Physics (Part 1) | `leph1` | 01 to 08 |
| **Class 12** | Physics (Part 2) | `leph2` | 01 to 06 |
| **Class 12** | Chemistry (Part 1) | `lech1` | 01 to 05 |
| **Class 12** | Chemistry (Part 2) | `lech2` | 01 to 05 |
| **Class 12** | Biology | `lebo1` | 01 to 13 |
| **Class 12** | English: Flamingo | `lefl1` | 01 to 13 |
| **Class 12** | English: Vistas | `levi1` | 01 to 06 |

---

### 3. Database Schema (PostgreSQL on Supabase)

```sql
-- 1. EXTENSIONS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. ENUMS
CREATE TYPE target_exam AS ENUM ('CBSE_BOARD', 'JEE_MAIN', 'JEE_ADVANCED', 'NEET');
CREATE TYPE question_format AS ENUM ('MCQ', 'ASSERTION_REASON', 'SHORT_ANSWER', 'LONG_ANSWER', 'CASE_STUDY');

-- 3. CENTRAL QUESTION BANK
CREATE TABLE master_question_bank (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    grade_level INT NOT NULL CHECK (grade_level BETWEEN 10 AND 12),
    subject VARCHAR(100) NOT NULL,
    chapter VARCHAR(150) NOT NULL,
    topic VARCHAR(150) NOT NULL,
    primary_exam target_exam NOT NULL,
    applicable_exams target_exam[] NOT NULL,
    difficulty_tier INT CHECK (difficulty_tier BETWEEN 1 AND 5), -- 1=Basic Board, 5=JEE Adv
    question_format question_format NOT NULL,
    marks NUMERIC(4, 1) NOT NULL,
    question_text_latex TEXT NOT NULL,
    options JSONB, -- {"A": "...", "B": "..."} for MCQs
    correct_option VARCHAR(5),
    ideal_solution_latex TEXT NOT NULL,
    step_marking_rubric JSONB NOT NULL,
    -- Schema: [{"step": 1, "rule": "...", "allocated_marks": 1.0}]
    source_book VARCHAR(200),
    content_hash VARCHAR(64) UNIQUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. SAVED EXAM PAPERS & BLUEPRINTS
CREATE TABLE generated_exams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    grade_level INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    total_marks INT NOT NULL,
    duration_minutes INT NOT NULL,
    exam_type target_exam NOT NULL,
    selected_chapters JSONB NOT NULL,
    blueprint_breakdown JSONB NOT NULL,
    question_ids UUID[] NOT NULL,
    student_pdf_url TEXT,
    solution_pdf_url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. MARKETING LEADS (PLG Capture)
CREATE TABLE teacher_leads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    teacher_name VARCHAR(150) NOT NULL,
    school_name VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    whatsapp_number VARCHAR(20) NOT NULL,
    generated_exam_id UUID REFERENCES generated_exams(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- INDEXES
CREATE INDEX idx_qbank_selection ON master_question_bank (grade_level, subject, chapter, difficulty_tier);
```
