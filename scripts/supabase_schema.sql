-- Supabase SQL Schema for AI Question Paper Generator

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ENUMS (using DO blocks to avoid errors if already existing)
DO $$ BEGIN
    CREATE TYPE target_exam AS ENUM ('CBSE_BOARD', 'JEE_MAIN', 'JEE_ADVANCED', 'NEET');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE question_format AS ENUM ('MCQ', 'ASSERTION_REASON', 'SHORT_ANSWER', 'LONG_ANSWER', 'CASE_STUDY');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- 1. CENTRAL QUESTION BANK
CREATE TABLE IF NOT EXISTS master_question_bank (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    grade_level INT NOT NULL CHECK (grade_level BETWEEN 10 AND 12),
    subject VARCHAR(100) NOT NULL,
    chapter VARCHAR(150) NOT NULL,
    topic VARCHAR(150) NOT NULL,
    primary_exam target_exam NOT NULL,
    applicable_exams target_exam[] NOT NULL,
    difficulty_tier INT CHECK (difficulty_tier BETWEEN 1 AND 5),
    question_format question_format NOT NULL,
    marks NUMERIC(4, 1) NOT NULL,
    question_text_latex TEXT NOT NULL,
    options JSONB,
    correct_option VARCHAR(5),
    ideal_solution_latex TEXT NOT NULL,
    step_marking_rubric JSONB NOT NULL,
    source_book VARCHAR(200),
    content_hash VARCHAR(64) UNIQUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. SAVED EXAM PAPERS & BLUEPRINTS
CREATE TABLE IF NOT EXISTS generated_exams (
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

-- 3. MARKETING LEADS (PLG Capture)
CREATE TABLE IF NOT EXISTS teacher_leads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    teacher_name VARCHAR(150) NOT NULL,
    school_name VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    whatsapp_number VARCHAR(20) NOT NULL,
    generated_exam_id UUID REFERENCES generated_exams(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- INDEXES
CREATE INDEX IF NOT EXISTS idx_qbank_selection ON master_question_bank (grade_level, subject, chapter, difficulty_tier);

-- Enable Row Level Security (RLS) with permissive read/write for pilot
ALTER TABLE master_question_bank ENABLE ROW LEVEL SECURITY;
ALTER TABLE generated_exams ENABLE ROW LEVEL SECURITY;
ALTER TABLE teacher_leads ENABLE ROW LEVEL SECURITY;

DO $$ BEGIN
    CREATE POLICY "Allow public read master_question_bank" ON master_question_bank FOR SELECT USING (true);
    CREATE POLICY "Allow public insert master_question_bank" ON master_question_bank FOR INSERT WITH CHECK (true);
    CREATE POLICY "Allow public update master_question_bank" ON master_question_bank FOR UPDATE USING (true);
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE POLICY "Allow public read generated_exams" ON generated_exams FOR SELECT USING (true);
    CREATE POLICY "Allow public insert generated_exams" ON generated_exams FOR INSERT WITH CHECK (true);
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE POLICY "Allow public read teacher_leads" ON teacher_leads FOR SELECT USING (true);
    CREATE POLICY "Allow public insert teacher_leads" ON teacher_leads FOR INSERT WITH CHECK (true);
EXCEPTION WHEN duplicate_object THEN null;
END $$;
