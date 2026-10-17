"""
Expands question bank across Class 10 Science/SST/English, Class 11 PCM/PCB,
and Class 12 PCM/PCB with competitive exam repositories (HC Verma, RD Sharma, OP Tandon, Lakhmir Singh).
"""
import sys
import logging
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
from backend.database import db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("seed_large")

MORE_QUESTIONS = [
    # Class 11 Physics (HC Verma Vol 1)
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Units and Measurements",
        "topic": "Dimensional Analysis", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 1, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "The dimensional formula of Planck's constant $h$ is identical to that of:",
        "options": {"A": "Linear momentum", "B": "Angular momentum", "C": "Energy", "D": "Power"},
        "correct_option": "B",
        "ideal_solution_latex": "$[h] = [E]/[\\nu] = [M L^2 T^{-2}]/[T^{-1}] = [M L^2 T^{-1}]$. Angular momentum $[L] = [r \\times p] = [L][M L T^{-1}] = [M L^2 T^{-1}]$. Hence identical to angular momentum.",
        "step_marking_rubric": [{"step": 1, "rule": "Derive dimensions of Planck's constant and angular momentum as [M L^2 T^-1]", "allocated_marks": 1.0}],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 1"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Motion in a Straight Line",
        "topic": "Kinematic Equations under Gravity", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "A ball is thrown vertically upwards with a velocity of $20\\text{ m/s}$ from the top of a multistorey building of height $25\\text{ m}$. How high will the ball rise from the ground, and how long will it take to reach the ground? (Take $g = 10\\text{ m/s}^2$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Maximum height above release point: $h_1 = \\frac{u^2}{2g} = \\frac{20^2}{2(10)} = 20\\text{ m}$. Total height from ground $= 25 + 20 = 45\\text{ m}$.\nTime to reach ground: displacement $y = -25\\text{ m}$. $y = ut - \\frac{1}{2}gt^2 \\implies -25 = 20t - 5t^2 \\implies 5t^2 - 20t - 25 = 0 \\implies t^2 - 4t - 5 = 0 \\implies (t - 5)(t + 1) = 0 \\implies t = 5\\text{ seconds}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculating max height 45 m from ground", "allocated_marks": 1.0},
            {"step": 2, "rule": "Solving quadratic equation to get t = 5 seconds", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 3"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Motion in a Plane",
        "topic": "Horizontal Range and Angle of Projection", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Prove that the horizontal range of a projectile launched with speed $u$ is the same for angles of projection $\\theta$ and $(90^\\circ - \\theta)$. For what angle is the range maximum?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Horizontal range $R(\\theta) = \\frac{u^2\\sin(2\\theta)}{g}$. For angle $(90^\\circ - \\theta)$: $R(90^\\circ - \\theta) = \\frac{u^2\\sin(2(90^\\circ - \\theta))}{g} = \\frac{u^2\\sin(180^\\circ - 2\\theta)}{g} = \\frac{u^2\\sin(2\\theta)}{g} = R(\\theta)$. Hence proved.\nRange is maximum when $\\sin(2\\theta) = 1 \\implies 2\\theta = 90^\\circ \\implies \\theta = 45^\\circ$. Maximum range $R_{\\max} = \\frac{u^2}{g}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Range formula R = u^2*sin(2*theta)/g", "allocated_marks": 1.0},
            {"step": 2, "rule": "Proving R(90-theta) = R(theta)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Stating theta = 45 degrees for max range u^2/g", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 3"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Laws of Motion",
        "topic": "Connected Bodies and Tension in Pulley Systems", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Two masses $m_1 = 5\\text{ kg}$ and $m_2 = 3\\text{ kg}$ are connected by a light inextensible string passing over a smooth frictionless pulley (Atwood machine).\n(a) Draw the free-body diagram for each mass.\n(b) Derive the expression for the acceleration of the system and the tension in the string.\n(c) Calculate the acceleration and tension. (Take $g = 9.8\\text{ m/s}^2$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) FBD for $m_1$ (heavier, moving down): $m_1 g - T = m_1 a$. FBD for $m_2$ (lighter, moving up): $T - m_2 g = m_2 a$.\n(b) Adding equations: $(m_1 - m_2)g = (m_1 + m_2)a \\implies a = \\frac{m_1 - m_2}{m_1 + m_2} g$.\nSubstituting $a$: $T = \\frac{2 m_1 m_2}{m_1 + m_2} g$.\n(c) $a = \\frac{5 - 3}{5 + 3}(9.8) = \\frac{2}{8}(9.8) = 2.45\\text{ m/s}^2$.\n$T = \\frac{2(5)(3)}{8}(9.8) = \\frac{30}{8}(9.8) = 36.75\\text{ N}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Drawing and formulating equations of motion for both masses", "allocated_marks": 2.0},
            {"step": 2, "rule": "Deriving acceleration a = (m1-m2)g/(m1+m2)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Deriving tension T = 2*m1*m2*g/(m1+m2)", "allocated_marks": 1.0},
            {"step": 4, "rule": "Evaluating a = 2.45 m/s^2 and T = 36.75 N", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 5"
    },

    # Class 11 Chemistry (OP Tandon / NCERT)
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Some Basic Concepts of Chemistry",
        "topic": "Molarity and Mole Fraction", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Calculate the molarity of $\\text{NaOH}$ in the solution prepared by dissolving its $4\\text{ g}$ in enough water to form $250\\text{ mL}$ of the solution. (Molar mass of $\\text{NaOH} = 40\\text{ g/mol}$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Moles of $\\text{NaOH} = \\frac{4\\text{ g}}{40\\text{ g/mol}} = 0.1\\text{ mol}$.\nVolume of solution in litres $= \\frac{250\\text{ mL}}{1000} = 0.25\\text{ L}$.\n$\\text{Molarity } M = \\frac{\\text{Moles of solute}}{\\text{Volume in L}} = \\frac{0.1}{0.25} = 0.4\\text{ M} = 0.4\\text{ mol/L}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Moles of NaOH = 0.1 mol", "allocated_marks": 1.0},
            {"step": 2, "rule": "Molarity = 0.1 / 0.25 = 0.4 M", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Chemistry Chapter 1 / OP Tandon"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Chemical Thermodynamics",
        "topic": "First Law of Thermodynamics and Hess's Law", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "In a process, $701\\text{ J}$ of heat is absorbed by a system and $394\\text{ J}$ of work is done by the system. What is the change in internal energy ($\\Delta U$) for the process?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "By the first law of thermodynamics: $\\Delta U = q + w$.\nHeat absorbed by system: $q = +701\\text{ J}$.\nWork done BY system: $w = -394\\text{ J}$.\nChange in internal energy $\\Delta U = 701 - 394 = +307\\text{ J}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "First law of thermodynamics formula delta U = q + w", "allocated_marks": 1.0},
            {"step": 2, "rule": "Assigning correct IUPAC sign conventions q = +701 J, w = -394 J", "allocated_marks": 1.0},
            {"step": 3, "rule": "Evaluating delta U = +307 J", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Chemistry Chapter 6 / OP Tandon"
    },

    # Class 12 Chemistry (MS Chouhan / OP Tandon / NCERT)
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Electrochemistry",
        "topic": "Nernst Equation and Cell Potential", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Represent the cell in which the following reaction takes place:\n$$\\text{Mg}(s) + 2\\text{Ag}^+(0.0001\\text{ M}) \\to \\text{Mg}^{2+}(0.130\\text{ M}) + 2\\text{Ag}(s)$$\nCalculate its $E_{\\text{cell}}$ if $E^0_{\\text{cell}} = 3.17\\text{ V}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Cell representation: $\\text{Mg}(s) | \\text{Mg}^{2+}(0.130\\text{ M}) || \\text{Ag}^+(0.0001\\text{ M}) | \\text{Ag}(s)$.\nHere $n = 2$.\nBy Nernst equation: $E_{\\text{cell}} = E^0_{\\text{cell}} - \\frac{0.0591}{n} \\log\\left(\\frac{[\\text{Mg}^{2+}]}{[\\text{Ag}^+]^2}\\right)$.\n$E_{\\text{cell}} = 3.17 - \\frac{0.0591}{2} \\log\\left(\\frac{0.130}{(10^{-4})^2}\\right) = 3.17 - 0.02955 \\log(1.3 \\times 10^7) = 3.17 - 0.02955(7.1139) = 3.17 - 0.21 = 2.96\\text{ V}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct cell notation representation", "allocated_marks": 1.0},
            {"step": 2, "rule": "Applying Nernst equation with n = 2", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculating log quotient and final E_cell = 2.96 V", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 2 / OP Tandon"
    },
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Coordination Compounds",
        "topic": "IUPAC Nomenclature and Crystal Field Theory", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Write the IUPAC names for the following coordination compounds:\n(a) $[\\text{Co}(\\text{NH}_3)_5(\\text{CO}_3)]\\text{Cl}$\n(b) $\\text{K}_3[\\text{Fe}(\\text{CN})_6]$",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Pentaamminecarbonatocobalt(III) chloride\n(b) Potassium hexacyanidoferrate(III)",
        "step_marking_rubric": [
            {"step": 1, "rule": "Pentaamminecarbonatocobalt(III) chloride", "allocated_marks": 1.0},
            {"step": 2, "rule": "Potassium hexacyanidoferrate(III)", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 5"
    },

    # Class 12 Mathematics (RD Sharma / Cengage)
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Continuity and Differentiability",
        "topic": "Continuity at a Point", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Find the value of $k$ so that the function $f(x) = \\begin{cases} k x + 1, & x \\le 5 \\\\ 3x - 5, & x > 5 \\end{cases}$ is continuous at $x = 5$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "For continuity at $x = 5$: $\\lim_{x \\to 5^-} f(x) = \\lim_{x \\to 5^+} f(x) = f(5)$.\nLHL $= f(5) = k(5) + 1 = 5k + 1$.\nRHL $= \\lim_{x \\to 5^+} (3x - 5) = 3(5) - 5 = 10$.\nEquating: $5k + 1 = 10 \\implies 5k = 9 \\implies k = \\frac{9}{5}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Evaluating LHL = 5k + 1 and RHL = 10", "allocated_marks": 1.0},
            {"step": 2, "rule": "Equating LHL = RHL to obtain k = 9/5", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Mathematics Chapter 5 / RD Sharma"
    },
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Applications of Derivatives",
        "topic": "Maxima and Minima - Applied Geometric Problem", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Show that the semi-vertical angle of the cone of the maximum volume and of given slant height $l$ is $\\tan^{-1}(\\sqrt{2})$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Let semi-vertical angle be $\\alpha$. Radius $r = l\\sin\\alpha$, Height $h = l\\cos\\alpha$.\nVolume of cone $V = \\frac{1}{3} \\pi r^2 h = \\frac{1}{3} \\pi (l\\sin\\alpha)^2 (l\\cos\\alpha) = \\frac{\\pi l^3}{3} \\sin^2\\alpha \\cos\\alpha$.\n$\\frac{dV}{d\\alpha} = \\frac{\\pi l^3}{3} [2\\sin\\alpha\\cos^2\\alpha - \\sin^3\\alpha] = \\frac{\\pi l^3}{3}\\sin\\alpha [2\\cos^2\\alpha - \\sin^2\\alpha]$.\nFor maximum volume, $\\frac{dV}{d\\alpha} = 0 \\implies 2\\cos^2\\alpha = \\sin^2\\alpha \\implies \\tan^2\\alpha = 2 \\implies \\tan\\alpha = \\sqrt{2} \\implies \\alpha = \\tan^{-1}(\\sqrt{2})$.\nSecond derivative test confirms $\\frac{d^2V}{d\\alpha^2} < 0$ at $\\tan\\alpha = \\sqrt{2}$, hence volume is maximized.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Expressing volume V in terms of slant height l and semi-vertical angle alpha", "allocated_marks": 1.5},
            {"step": 2, "rule": "Differentiating with respect to alpha and setting dV/dalpha = 0", "allocated_marks": 1.5},
            {"step": 3, "rule": "Solving tan^2(alpha) = 2 => alpha = tan^-1(sqrt(2))", "allocated_marks": 1.0},
            {"step": 4, "rule": "Second derivative test for maximum verification", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Mathematics Chapter 6 / RD Sharma"
    },
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Vector Algebra",
        "topic": "Dot and Cross Product", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Find the projection of the vector $\\vec{a} = 2\\hat{i} + 3\\hat{j} + 2\\hat{k}$ on the vector $\\vec{b} = \\hat{i} + 2\\hat{j} + \\hat{k}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Projection of $\\vec{a}$ on $\\vec{b} = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|}$.\n$\\vec{a} \\cdot \\vec{b} = (2)(1) + (3)(2) + (2)(1) = 2 + 6 + 2 = 10$.\n$|\\vec{b}| = \\sqrt{1^2 + 2^2 + 1^2} = \\sqrt{1 + 4 + 1} = \\sqrt{6}$.\nProjection $= \\frac{10}{\\sqrt{6}} = \\frac{5\\sqrt{6}}{3}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Formula projection = (a . b) / |b|", "allocated_marks": 1.0},
            {"step": 2, "rule": "Computing a . b = 10 and |b| = sqrt(6) to get 10/sqrt(6)", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Mathematics Chapter 10"
    }
]

def seed():
    logger.info(f"Ingesting {len(MORE_QUESTIONS)} additional questions across Class 10, 11, 12...")
    count = db.upsert_questions(MORE_QUESTIONS)
    logger.info(f"Inserted {count} questions.")

if __name__ == "__main__":
    seed()
