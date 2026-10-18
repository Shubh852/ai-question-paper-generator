"""
Typst Typesetting Engine for Student Question Papers and Teacher Marking Schemes.
Converts LaTeX mathematical formulas, custom school branding, and scientific diagrams into print-ready PDFs.
"""

import os
import re
import uuid
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import typst

logger = logging.getLogger("typesetter")

ROOT_DIR = Path(__file__).resolve().parent.parent

TYPST_MATH_KEYWORDS = [
    "integral.cont", "integral", "plus.minus", "minus.plus", "epsilon_0", "mu_0",
    "degree", "infinity", "parallel", "approx", "tilde", "root", "sqrt", "arrow",
    "hat", "bold", "times", "dot", "diff", "alpha", "beta", "gamma", "delta",
    "theta", "lambda", "sigma", "tau", "epsilon", "Delta", "Phi", "Omega", "pi",
    "mu", "sum", "sin", "cos", "tan", "log", "ln", "bot", "min", "max"
]

def latex_to_typst_math(math_content: str) -> str:
    """Translate LaTeX mathematical expressions to Typst native math syntax."""
    s = math_content.strip()

    # Pre-clean braces and fractions
    for _ in range(4):
        s = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"(\1) / (\2)", s)
        s = re.sub(r"\\sqrt\[(.*?)\]\{(.*?)\}", r"root(\1, \2)", s)
        s = re.sub(r"\\sqrt\{(.*?)\}", r"sqrt(\1)", s)
        s = re.sub(r"\\text\{([^}]*)\}", r'"\1"', s)
        s = re.sub(r"\\mathrm\{([^}]*)\}", r'"\1"', s)
        s = re.sub(r"\\vec\{([^}]+)\}", r"arrow(\1)", s)
        s = re.sub(r"\\hat\{([^}]+)\}", r"hat(\1)", s)
        s = re.sub(r"\\mathbf\{([^}]+)\}", r"bold(\1)", s)

    replacements = [
        (r"\\pm", " +- "),
        (r"\\mp", " -+ "),
        (r"\\times", " times "),
        (r"\\cdot", " dot "),
        (r"\\neq", " != "),
        (r"\\leq", " <= "),
        (r"\\geq", " >= "),
        (r"\\ll", " << "),
        (r"\\gg", " >> "),
        (r"\\approx", " approx "),
        (r"\\sim", " tilde "),
        (r"\\alpha", " alpha "),
        (r"\\beta", " beta "),
        (r"\\gamma", " gamma "),
        (r"\\delta", " delta "),
        (r"\\theta", " theta "),
        (r"\\lambda", " lambda "),
        (r"\\mu_0", " mu_0 "),
        (r"\\mu", " mu "),
        (r"\\pi", " pi "),
        (r"\\sigma", " sigma "),
        (r"\\tau", " tau "),
        (r"\\varepsilon_0", " epsilon_0 "),
        (r"\\varepsilon", " epsilon "),
        (r"\\epsilon", " epsilon "),
        (r"\\Delta", " Delta "),
        (r"\\Phi", " Phi "),
        (r"\\Omega", " Omega "),
        (r"\\oint", " integral.cont "),
        (r"\\int", " integral "),
        (r"\\sum", " sum "),
        (r"\\partial", " diff "),
        (r"\\infty", " infinity "),
        (r"\\perp", " bot "),
        (r"\\parallel", " parallel "),
        (r"\\implies", " ==> "),
        (r"\\to", " -> "),
        (r"\\circ", " degree "),
        (r"\\,", " "),
        (r"\\;", " "),
        (r"\\ ", " "),
        (r"\\left", ""),
        (r"\\right", ""),
        (r"\{", ""),
        (r"\}", ""),
    ]

    for pattern, repl in replacements:
        s = re.sub(pattern, repl, s)

    # Protect quoted strings using placeholders with no adjacent letters
    quotes = []
    def save_quote(m):
        quotes.append(m.group(0))
        return f"@S{len(quotes)-1}@"
    s = re.sub(r'"[^"]*"', save_quote, s)

    # Protect keywords using placeholders with no adjacent letters
    kws = []
    def save_kw(m):
        kws.append(m.group(0))
        return f"@K{len(kws)-1}@"

    sorted_kws = sorted(TYPST_MATH_KEYWORDS, key=len, reverse=True)
    kw_pattern = r'\b(' + '|'.join(re.escape(k) for k in sorted_kws) + r')\b'
    s = re.sub(kw_pattern, save_kw, s)

    # Separate variable before parenthesis e.g. x(x - 2) -> x (x - 2)
    s = re.sub(r'([a-zA-Z0-9])\(', r'\1 (', s)
    s = re.sub(r'\)([a-zA-Z0-9])', r') \1', s)

    # Separate adjacent letters (e.g. kx -> k x, 4ac -> 4 a c, ab -> a b)
    s = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1 \2', s)
    s = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1 \2', s)

    # Restore keywords
    for idx, kw in enumerate(kws):
        s = s.replace(f"@K{idx}@", kw)
    # Restore quotes
    for idx, q in enumerate(quotes):
        s = s.replace(f"@S{idx}@", q)

    # Clean any remaining LaTeX backslashes
    s = re.sub(r"\\([a-zA-Z]+)", r"\1", s)

    # Normalize spaces
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def sanitize_typst_text(text: str) -> str:
    """
    Format question statement for Typst, converting LaTeX $...$ and $$...$$
    into native Typst math expressions and escaping special Typst markup.
    """
    if not text:
        return ""

    # Replace display math $$...$$
    def repl_display_math(match):
        inner = match.group(1).strip()
        converted = latex_to_typst_math(inner)
        return f"\n$ {converted} $\n"

    # Replace inline math $...$
    def repl_inline_math(match):
        inner = match.group(1).strip()
        converted = latex_to_typst_math(inner)
        return f"${converted}$"

    # Protect double dollar first
    processed = re.sub(r"\$\$(.*?)\$\$", repl_display_math, text, flags=re.DOTALL)
    # Then inline single dollar
    processed = re.sub(r"\$([^\$\n]+?)\$", repl_inline_math, processed)

    # Clean line breaks
    processed = processed.replace(r"\\", "\n")
    return processed

def resolve_asset_path(raw_path: str) -> Optional[str]:
    """
    Resolves a diagram or logo URL / path to a relative path from ROOT_DIR
    that Typst can compile.
    """
    if not raw_path:
        return None
    cleaned = raw_path.strip().replace("\\", "/")
    if cleaned.startswith("/"):
        cleaned = cleaned.lstrip("/")

    # Check candidates
    candidates = [
        ROOT_DIR / cleaned,
        ROOT_DIR / "data" / cleaned,
        ROOT_DIR / "data" / "diagrams" / Path(cleaned).name,
        ROOT_DIR / "data" / "logos" / Path(cleaned).name,
        ROOT_DIR / "frontend" / "public" / cleaned,
    ]
    for c in candidates:
        if c.exists() and c.is_file():
            # Return path relative to ROOT_DIR with forward slashes
            return c.relative_to(ROOT_DIR).as_posix()
    return None

def extract_diagram_info(text: str, question: Dict[str, Any]) -> Tuple[str, Optional[str], Optional[str]]:
    """
    Extracts diagram path and caption from markdown images ![alt](url)
    or from question['figure_url'].
    Returns: (cleaned_text, resolved_diagram_path, caption)
    """
    img_match = re.search(r'!\[(.*?)\]\((.*?)\)', text)
    if img_match:
        caption = img_match.group(1) or "Diagram"
        raw_url = img_match.group(2)
        # Strip markdown image from text
        cleaned_text = text[:img_match.start()] + text[img_match.end():]
        rel_path = resolve_asset_path(raw_url)
        return cleaned_text.strip(), rel_path, caption

    # Check explicit figure_url / diagram_url
    fig_url = question.get("figure_url") or question.get("diagram_url")
    if fig_url:
        caption = question.get("figure_caption", "Diagram")
        rel_path = resolve_asset_path(fig_url)
        return text.strip(), rel_path, caption

    return text.strip(), None, None

def format_exam_section_name(code: str) -> str:
    mapping = {
        "A": "SECTION A (Multiple Choice & Objective Questions - 1 Mark each)",
        "B": "SECTION B (Very Short Answer Questions - 2 Marks each)",
        "C": "SECTION C (Short Answer Questions - 3 Marks each)",
        "D": "SECTION D (Long Answer Questions - 5 Marks each)",
        "E": "SECTION E (Case Study / Source Based Integrated Questions - 4 Marks each)",
    }
    return mapping.get(code, f"SECTION {code}")

def generate_header_block(exam: Dict[str, Any], is_solution: bool = False) -> List[str]:
    """Generates a branded header with School Logo, School Name, and Exam details."""
    title = exam.get("title", "CBSE PRE-BOARD EXAMINATION 2026-27")
    grade = exam.get("grade_level", 10)
    subject = exam.get("subject", "Mathematics")
    total_marks = exam.get("total_marks", 80)
    duration = exam.get("duration_minutes", 180)
    hours = duration // 60
    mins = duration % 60
    time_str = f"{hours} Hours" if mins == 0 else f"{hours} Hours {mins} Mins"

    school_name = exam.get("school_name", "").strip()
    school_logo_raw = exam.get("school_logo") or exam.get("logo_url")
    school_logo = resolve_asset_path(school_logo_raw) if school_logo_raw else None

    # Fallback to default logo if school_name is provided but no specific logo uploaded
    if not school_logo and school_name:
        default_logo = ROOT_DIR / "data" / "logos" / "default_school_logo.svg"
        if default_logo.exists():
            school_logo = "data/logos/default_school_logo.svg"

    lines = []

    if school_logo and Path(ROOT_DIR / school_logo).exists():
        # Branded Header with Logo
        display_org = school_name.upper() if school_name else "CENTRAL BOARD OF SECONDARY EDUCATION"
        lines.append('#grid(')
        lines.append('  columns: (55pt, 1fr, 55pt),')
        lines.append('  align: (center + horizon, center + horizon, center + horizon),')
        lines.append(f'  [#image("{school_logo}", width: 48pt)],')
        lines.append('  [')
        lines.append(f'    #text(size: 13.5pt, weight: "bold")[{display_org}]\n')
        if is_solution:
            lines.append('    #text(size: 9.5pt, weight: "bold", fill: rgb(180, 40, 40))[MARKING SCHEME & STEP-WISE MODEL ANSWERS]\n')
        else:
            lines.append('    #text(size: 9pt, weight: "bold", fill: rgb(70, 70, 70))[AFFILIATED TO CBSE, NEW DELHI]\n')
        lines.append(f'    #text(size: 12pt, weight: "bold")[{title.upper()}]\n')
        lines.append(f'    #text(size: 10.5pt, weight: "bold")[CLASS {grade} — {subject.upper()}]\n')
        lines.append('  ],')
        lines.append(f'  [#image("{school_logo}", width: 48pt)]')
        lines.append(')')
    else:
        # Standard Clean Header
        org = school_name.upper() if school_name else "CENTRAL BOARD OF SECONDARY EDUCATION"
        lines.append('#align(center)[')
        lines.append(f'  #text(size: 14pt, weight: "bold")[{org}]\n')
        if is_solution:
            lines.append('  #text(size: 12pt, weight: "bold", fill: rgb(180, 40, 40))[MARKING SCHEME & STEP-WISE MODEL ANSWERS]\n')
        lines.append(f'  #text(size: 13pt, weight: "bold")[{title.upper()}]\n')
        lines.append(f'  #text(size: 11pt, weight: "bold")[CLASS {grade} — {subject.upper()}]\n')
        lines.append(']')

    lines.append('#line(length: 100%, stroke: 1.2pt)')
    if not is_solution:
        lines.append(f'#grid(columns: (1fr, 1fr), align: (left, right), [*Time Allowed:* {time_str}], [*Maximum Marks:* {total_marks}])')
    else:
        lines.append(f'#grid(columns: (1fr, 1fr), align: (left, right), [*Evaluation Copy* — Evaluator Scheme], [*Maximum Marks:* {total_marks}])')
    lines.append('#line(length: 100%, stroke: 0.5pt)')
    lines.append('')
    return lines

def generate_student_typst(exam: Dict[str, Any], questions_by_section: Dict[str, List[Dict[str, Any]]]) -> str:
    """Generate Typst source code for Student Question Paper."""
    typ = []
    typ.append('#set page(paper: "a4", margin: (x: 1.8cm, top: 1.8cm, bottom: 2cm), header: align(right)[#text(size: 8pt, fill: luma(100))[Series: AGY/2026/CBSE | Set 1]], numbering: "1 of 1")')
    typ.append('#set text(font: ("Times New Roman", "Liberation Serif"), size: 10.5pt, lang: "en")')
    typ.append('#set par(justify: true, leading: 0.65em)')
    typ.append('')
    
    # Header block
    typ.extend(generate_header_block(exam, is_solution=False))

    # General instructions
    typ.append('#block(fill: rgb(248, 249, 250), inset: 8pt, radius: 4pt, stroke: 0.5pt + luma(200))[')
    typ.append('  #text(weight: "bold", size: 9.5pt)[General Instructions:]\n')
    typ.append('  #text(size: 8.5pt)[')
    typ.append('  1. This question paper contains 5 Sections: A, B, C, D, and E.\n')
    typ.append('  2. *Section A* comprises Multiple Choice Questions (MCQs) and Assertion-Reason questions of 1 mark each.\n')
    typ.append('  3. *Section B* comprises Very Short Answer (VSA) type questions of 2 marks each.\n')
    typ.append('  4. *Section C* comprises Short Answer (SA) type questions of 3 marks each.\n')
    typ.append('  5. *Section D* comprises Long Answer (LA) type questions of 5 marks each.\n')
    typ.append('  6. *Section E* comprises Case Based integrated units of assessment of 4 marks each with sub-parts.\n')
    typ.append('  7. All Questions are compulsory. Internal choice is provided in some questions.\n')
    typ.append('  8. Use of calculators or electronic devices is not permitted.')
    typ.append('  ]')
    typ.append(']')
    typ.append('#v(8pt)')

    q_num = 1
    for sec in ["A", "B", "C", "D", "E"]:
        qs = questions_by_section.get(sec, [])
        if not qs:
            continue

        sec_heading = format_exam_section_name(sec)
        typ.append(f'\n#align(center)[#block(fill: rgb(235, 242, 250), inset: (x: 10pt, y: 5pt), radius: 3pt)[#text(weight: "bold", size: 10pt)[{sec_heading}]]]\n')
        typ.append('#v(4pt)')

        for q in qs:
            marks = int(q["marks"]) if q["marks"] == int(q["marks"]) else q["marks"]
            raw_text = q.get("question_text_latex", "")
            cleaned_text, diagram_path, caption = extract_diagram_info(raw_text, q)
            sanitized_q = sanitize_typst_text(cleaned_text)

            typ.append(f'#block(width: 100%, breakable: false)[')
            typ.append(f'  #grid(columns: (22pt, 1fr, 30pt), gutter: 4pt,')
            typ.append(f'    [*Q{q_num}.*],')
            typ.append(f'    [{sanitized_q}')

            # Embedded Diagram / Circuit
            if diagram_path:
                typ.append('      #v(4pt)')
                typ.append(f'      #align(center)[#image("{diagram_path}", width: 45%)]')
                typ.append(f'      #align(center)[#text(size: 8pt, style: "italic", fill: rgb(75, 85, 99))[Figure: {caption}]]')

            # MCQs options
            if q.get("options") and isinstance(q["options"], dict):
                typ.append('      #v(3pt)')
                opts = q["options"]
                opt_a = sanitize_typst_text(str(opts.get("A", "")))
                opt_b = sanitize_typst_text(str(opts.get("B", "")))
                opt_c = sanitize_typst_text(str(opts.get("C", "")))
                opt_d = sanitize_typst_text(str(opts.get("D", "")))
                max_opt_len = max(len(opt_a), len(opt_b), len(opt_c), len(opt_d))
                if max_opt_len <= 15:
                    typ.append(f'      #grid(columns: (1fr, 1fr, 1fr, 1fr), row-gutter: 4pt, [(A) {opt_a}], [(B) {opt_b}], [(C) {opt_c}], [(D) {opt_d}])')
                else:
                    typ.append(f'      #grid(columns: (1fr, 1fr), row-gutter: 4pt, [(A) {opt_a}], [(B) {opt_b}], [(C) {opt_c}], [(D) {opt_d}])')

            typ.append(f'    ],')
            typ.append(f'    [#align(right)[*[{marks}]*]]')
            typ.append(f'  )')
            typ.append(f']')
            typ.append('#v(6pt)')
            q_num += 1

    typ.append('\n#align(center)[#v(10pt) #text(weight: "bold", size: 9pt)[*** END OF QUESTION PAPER ***]]')
    return "\n".join(typ)

def generate_solution_typst(exam: Dict[str, Any], questions_by_section: Dict[str, List[Dict[str, Any]]]) -> str:
    """Generate Typst source code for Marking Scheme and Step-by-Step Model Solutions."""
    typ = []
    typ.append('#set page(paper: "a4", margin: (x: 1.8cm, top: 1.8cm, bottom: 2cm), header: align(right)[#text(size: 8pt, fill: luma(100))[CONFIDENTIAL | EVALUATOR SCHEME]], numbering: "1 of 1")')
    typ.append('#set text(font: ("Times New Roman", "Liberation Serif"), size: 10pt, lang: "en")')
    typ.append('#set par(justify: true, leading: 0.6em)')
    typ.append('')

    # Header
    typ.extend(generate_header_block(exam, is_solution=True))
    typ.append('#v(4pt)')

    q_num = 1
    for sec in ["A", "B", "C", "D", "E"]:
        qs = questions_by_section.get(sec, [])
        if not qs:
            continue

        sec_heading = format_exam_section_name(sec)
        typ.append(f'\n#align(center)[#block(fill: rgb(240, 244, 248), inset: (x: 10pt, y: 4pt), radius: 3pt)[#text(weight: "bold", size: 10pt)[{sec_heading}]]]\n')

        for q in qs:
            marks = int(q["marks"]) if q["marks"] == int(q["marks"]) else q["marks"]
            raw_text = q.get("question_text_latex", "")
            cleaned_text, diagram_path, caption = extract_diagram_info(raw_text, q)
            sanitized_q = sanitize_typst_text(cleaned_text)
            sanitized_sol = sanitize_typst_text(q.get("ideal_solution_latex", ""))
            correct_opt = q.get("correct_option")
            rubrics = q.get("step_marking_rubric", [])

            typ.append(f'#block(fill: rgb(252, 252, 253), stroke: 0.5pt + luma(190), inset: 8pt, radius: 4pt, width: 100%)[')
            typ.append(f'  #grid(columns: (1fr, 50pt), [*Q{q_num}.* ({q.get("chapter", "")})], [#align(right)[*[{marks} Marks]*]])')
            typ.append(f'  #v(2pt)')
            typ.append(f'  #text(size: 9pt, fill: luma(80))[{sanitized_q}]')

            if diagram_path:
                typ.append('  #v(3pt)')
                typ.append(f'  #align(center)[#image("{diagram_path}", width: 35%)]')
                typ.append(f'  #align(center)[#text(size: 7.5pt, style: "italic", fill: rgb(100, 100, 100))[Figure: {caption}]]')

            typ.append(f'  #line(length: 100%, stroke: 0.3pt + luma(210))')
            typ.append(f'  #v(2pt)')

            if correct_opt:
                typ.append(f'  #text(weight: "bold", fill: rgb(20, 110, 50))[*Correct Answer: Option ({correct_opt})*]\n')

            typ.append(f'  *Model Answer:*\n')
            typ.append(f'  {sanitized_sol}\n')

            if rubrics and isinstance(rubrics, list):
                typ.append('  #v(4pt)')
                typ.append('  #text(weight: "bold", size: 8.5pt)[Step-Wise Marking Breakdown:]')
                typ.append('  #table(')
                typ.append('    columns: (35pt, 1fr, 50pt),')
                typ.append('    fill: (x, y) => if y == 0 { rgb(235, 240, 245) } else { none },')
                typ.append('    stroke: 0.3pt + luma(180),')
                typ.append('    [*Step*], [*Evaluation Criteria / Step Rule*], [*Marks*],')
                for idx, r in enumerate(rubrics, 1):
                    rule_text = sanitize_typst_text(str(r.get("rule", "")))
                    alloc = r.get("allocated_marks", 1.0)
                    alloc_str = f"{alloc:.1f}" if isinstance(alloc, (int, float)) else str(alloc)
                    typ.append(f'    [{idx}], [{rule_text}], [{alloc_str} M],')
                typ.append('  )')

            typ.append(f']')
            typ.append('#v(6pt)')
            q_num += 1

    return "\n".join(typ)

def compile_to_pdf(typst_content: str, output_path: Optional[str] = None) -> bytes:
    """
    Compile Typst document string into PDF bytes or write to output file.
    Creates temporary typ file in ROOT_DIR so relative image paths resolve safely.
    """
    temp_name = f"_typst_{uuid.uuid4().hex}.typ"
    temp_path = ROOT_DIR / temp_name

    try:
        temp_path.write_text(typst_content, encoding="utf-8")
        if output_path:
            out_p = Path(output_path).resolve()
            out_p.parent.mkdir(parents=True, exist_ok=True)
            typst.compile(str(temp_path), output=str(out_p))
            logger.info(f"Typst compiled PDF successfully to: {out_p}")
            return out_p.read_bytes()
        else:
            pdf_bytes = typst.compile(str(temp_path))
            logger.info(f"Typst compiled PDF successfully ({len(pdf_bytes)} bytes)")
            return pdf_bytes
    finally:
        try:
            if temp_path.exists():
                temp_path.unlink()
        except Exception:
            pass
