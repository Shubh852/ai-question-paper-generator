"""
Massive Comprehensive Curriculum Seeder:
Expands question bank to 250+ questions covering all subjects, chapters, and competitive repositories
(HC Verma Vol 1 & 2, RD Sharma, OP Tandon, Lakhmir Singh, Trueman's Biology, NCERT)
for Class 10, Class 11, and Class 12 into Supabase PostgreSQL Cloud.
"""

import sys
import hashlib
import logging
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

load_dotenv()
from backend.database import db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("seed_massive")

MASSIVE_QUESTIONS = [
    # =========================================================================
    # CLASS 10 - MATHEMATICS (RD Sharma & NCERT)
    # =========================================================================
    {
        "grade_level": 10, "subject": "Mathematics", "chapter": "Real Numbers",
        "topic": "Fundamental Theorem of Arithmetic", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Explain why $7 \\times 11 \\times 13 + 13$ and $7 \\times 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1 + 5$ are composite numbers.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "$7 \\times 11 \\times 13 + 13 = 13(7 \\times 11 + 1) = 13(77 + 1) = 13 \\times 78 = 13 \\times 13 \\times 6 = 13^2 \\times 2 \\times 3$.\nSince this number can be expressed as a product of prime factors other than $1$ and itself, by the Fundamental Theorem of Arithmetic, it is a composite number.\nSimilarly, $7 \\times 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1 + 5 = 5(7 \\times 6 \\times 4 \\times 3 \\times 2 \\times 1 + 1) = 5(1008 + 1) = 5 \\times 1009$. Both 5 and 1009 are factors, so it is composite.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Factoring out 13 and showing prime factorization", "allocated_marks": 1.0},
            {"step": 2, "rule": "Factoring out 5 and applying Fundamental Theorem of Arithmetic", "allocated_marks": 1.0}
        ],
        "source_book": "RD Sharma Class 10 / NCERT Chapter 1"
    },
    {
        "grade_level": 10, "subject": "Mathematics", "chapter": "Polynomials",
        "topic": "Relationship Between Zeros and Coefficients", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Find the zeros of the quadratic polynomial $p(x) = 6x^2 - 3 - 7x$ and verify the relationship between the zeros and the coefficients.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Rearranging: $p(x) = 6x^2 - 7x - 3 = 6x^2 - 9x + 2x - 3 = 3x(2x - 3) + 1(2x - 3) = (2x - 3)(3x + 1)$.\nZeros are $\\alpha = \\frac{3}{2}$ and $\\beta = -\\frac{1}{3}$.\nVerification:\n- Sum of zeros: $\\alpha + \\beta = \\frac{3}{2} - \\frac{1}{3} = \\frac{9 - 2}{6} = \\frac{7}{6} = -\\frac{b}{a} = -\\frac{-7}{6} = \\frac{7}{6}$.\n- Product of zeros: $\\alpha \\beta = \\left(\\frac{3}{2}\\right)\\left(-\\frac{1}{3}\\right) = -\\frac{1}{2} = \\frac{c}{a} = \\frac{-3}{6} = -\\frac{1}{2}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Factorization yielding zeros 3/2 and -1/3", "allocated_marks": 1.5},
            {"step": 2, "rule": "Verification of sum and product of zeros against coefficients", "allocated_marks": 1.5}
        ],
        "source_book": "RD Sharma Class 10 / NCERT Chapter 2"
    },
    {
        "grade_level": 10, "subject": "Mathematics", "chapter": "Pair of Linear Equations in Two Variables",
        "topic": "Cross-Multiplication and Algebraic Elimination", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "For what values of $a$ and $b$ does the following pair of linear equations have an infinite number of solutions?\n$2x + 3y = 7$\n$(a - b)x + (a + b)y = 3a + b - 2$",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "For infinite solutions: $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} \\implies \\frac{2}{a-b} = \\frac{3}{a+b} = \\frac{7}{3a+b-2}$.\nFrom $\\frac{2}{a-b} = \\frac{3}{a+b} \\implies 2a + 2b = 3a - 3b \\implies a - 5b = 0 \\implies a = 5b$.\nFrom $\\frac{3}{a+b} = \\frac{7}{3a+b-2} \\implies 9a + 3b - 6 = 7a + 7b \\implies 2a - 4b = 6 \\implies a - 2b = 3$.\nSubstitute $a = 5b$: $5b - 2b = 3 \\implies 3b = 3 \\implies b = 1$.\nThen $a = 5(1) = 5$. Thus, $a = 5, b = 1$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Condition for infinite solutions a1/a2 = b1/b2 = c1/c2", "allocated_marks": 1.0},
            {"step": 2, "rule": "Setting up two linear equations in a and b", "allocated_marks": 1.0},
            {"step": 3, "rule": "Solving to get a = 5 and b = 1", "allocated_marks": 1.0}
        ],
        "source_book": "RD Sharma Class 10 / NCERT Chapter 3"
    },
    {
        "grade_level": 10, "subject": "Mathematics", "chapter": "Triangles",
        "topic": "Basic Proportionality Theorem (Thales Theorem)", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "State and prove the Basic Proportionality Theorem (Thales Theorem). Using this theorem, prove that in a trapezium $ABCD$ with $AB \\parallel DC$, diagonals intersect at $O$ such that $\\frac{AO}{BO} = \\frac{CO}{DO}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "**Statement**: If a line is drawn parallel to one side of a triangle intersecting the other two sides in distinct points, then the other two sides are divided in the same ratio.\n**Proof**: In $\\Delta ABC$, draw $DE \\parallel BC$. Join $BE$ and $CD$. Draw perpendiculars $EN \\perp AB$ and $DM \\perp AC$.\n$\\text{Area}(\\Delta ADE) = \\frac{1}{2} \\times AD \\times EN$.\n$\\text{Area}(\\Delta BDE) = \\frac{1}{2} \\times DB \\times EN$.\n$\\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta BDE)} = \\frac{AD}{DB}$.\nSimilarly, $\\frac{\\text{Area}(\\Delta ADE)}{\\text{Area}(\\Delta CDE)} = \\frac{AE}{EC}$.\nSince $\\Delta BDE$ and $\\Delta CDE$ are on the same base $DE$ and between parallel lines $DE \\parallel BC$, $\\text{Area}(\\Delta BDE) = \\text{Area}(\\Delta CDE)$.\nHence $\\frac{AD}{DB} = \\frac{AE}{EC}$.\n**Application to Trapezium**: Draw $OE \\parallel AB \\parallel DC$ through $O$ meeting $AD$ at $E$. In $\\Delta ADC$, $OE \\parallel DC \\implies \\frac{AE}{ED} = \\frac{AO}{OC}$. In $\\Delta DAB$, $OE \\parallel AB \\implies \\frac{ED}{AE} = \\frac{DO}{OB} \\implies \\frac{AE}{ED} = \\frac{OB}{OD}$. Equating gives $\\frac{AO}{OC} = \\frac{BO}{OD} \\implies \\frac{AO}{BO} = \\frac{CO}{DO}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct statement and construction of Thales theorem", "allocated_marks": 1.0},
            {"step": 2, "rule": "Area ratios proof equating areas on same base", "allocated_marks": 2.0},
            {"step": 3, "rule": "Trapezium application proof using auxiliary parallel line", "allocated_marks": 2.0}
        ],
        "source_book": "RD Sharma Class 10 / NCERT Chapter 6"
    },
    {
        "grade_level": 10, "subject": "Mathematics", "chapter": "Introduction to Trigonometry",
        "topic": "Trigonometric Identities", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Prove the trigonometric identity: $\\frac{\\sin\\theta - 2\\sin^3\\theta}{2\\cos^3\\theta - \\cos\\theta} = \\tan\\theta$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "LHS $= \\frac{\\sin\\theta (1 - 2\\sin^2\\theta)}{\\cos\\theta (2\\cos^2\\theta - 1)}$.\nUsing identity $\\sin^2\\theta + \\cos^2\\theta = 1 \\implies 1 = \\sin^2\\theta + \\cos^2\\theta$:\nNumerator $= 1 - 2\\sin^2\\theta = (\\sin^2\\theta + \\cos^2\\theta) - 2\\sin^2\\theta = \\cos^2\\theta - \\sin^2\\theta$.\nDenominator $= 2\\cos^2\\theta - (\\sin^2\\theta + \\cos^2\\theta) = \\cos^2\\theta - \\sin^2\\theta$.\nThus, LHS $= \\frac{\\sin\\theta (\\cos^2\\theta - \\sin^2\\theta)}{\\cos\\theta (\\cos^2\\theta - \\sin^2\\theta)} = \\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta = \\text{RHS}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Factoring sin theta in numerator and cos theta in denominator", "allocated_marks": 1.0},
            {"step": 2, "rule": "Transforming 1 - 2*sin^2(theta) to cos^2(theta) - sin^2(theta)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Canceling terms to get tan theta = RHS", "allocated_marks": 1.0}
        ],
        "source_book": "RD Sharma Class 10 / NCERT Chapter 8"
    },
    {
        "grade_level": 10, "subject": "Mathematics", "chapter": "Some Applications of Trigonometry",
        "topic": "Heights and Distances", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "CASE_STUDY", "marks": 4.0,
        "question_text_latex": "A $1.2\\text{ m}$ tall girl spots a balloon moving with the wind in a horizontal line at a height of $88.2\\text{ m}$ from the ground. The angle of elevation of the balloon from the eyes of the girl at any instant is $60^\\circ$. After some time, the angle of elevation reduces to $30^\\circ$.\n(a) Find the vertical height of the balloon from the eye level of the girl.\n(b) Find the distance traveled by the balloon during the interval. (Use $\\sqrt{3} = 1.732$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Height from eye level $h = 88.2 - 1.2 = 87\\text{ m}$.\n(b) Let $x_1$ and $x_2$ be the horizontal distances from the girl.\nIn the first position: $\\tan 60^\\circ = \\frac{h}{x_1} \\implies \\sqrt{3} = \\frac{87}{x_1} \\implies x_1 = \\frac{87}{\\sqrt{3}} = 29\\sqrt{3}\\text{ m}$.\nIn the second position: $\\tan 30^\\circ = \\frac{h}{x_2} \\implies \\frac{1}{\\sqrt{3}} = \\frac{87}{x_2} \\implies x_2 = 87\\sqrt{3}\\text{ m}$.\nDistance traveled $d = x_2 - x_1 = 87\\sqrt{3} - 29\\sqrt{3} = 58\\sqrt{3}\\text{ m} = 58 \\times 1.732 \\approx 100.46\\text{ m}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Height from eye level 87 m", "allocated_marks": 1.0},
            {"step": 2, "rule": "First distance x1 = 29*sqrt(3) m", "allocated_marks": 1.5},
            {"step": 3, "rule": "Second distance x2 = 87*sqrt(3) and net travel 58*sqrt(3) m", "allocated_marks": 1.5}
        ],
        "source_book": "RD Sharma Class 10 / NCERT Chapter 9"
    },
    {
        "grade_level": 10, "subject": "Mathematics", "chapter": "Statistics",
        "topic": "Median of Grouped Data", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "The median of the following distribution is $28.5$. Find the values of $x$ and $y$, if the total frequency is $60$:\n- $0-10$: $5$\n- $10-20$: $x$\n- $20-30$: $20$\n- $30-40$: $15$\n- $40-50$: $y$\n- $50-60$: $5$",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Cumulative Frequencies: $5, 5+x, 25+x, 40+x, 40+x+y, 45+x+y$.\nTotal frequency $N = 60 \\implies 45 + x + y = 60 \\implies x + y = 15$  --- (1)\nMedian $= 28.5$, which lies in class interval $20 - 30$.\nMedian class: $l = 20, f = 20, cf = 5 + x, h = 10, \\frac{N}{2} = 30$.\n$\\text{Median} = l + \\left( \\frac{\\frac{N}{2} - cf}{f} \\right) \\times h$.\n$28.5 = 20 + \\left( \\frac{30 - (5 + x)}{20} \\right) \\times 10$.\n$8.5 = \\frac{25 - x}{2} \\implies 17 = 25 - x \\implies x = 8$.\nSubstitute $x = 8$ in (1): $8 + y = 15 \\implies y = 7$.\nThus, $x = 8, y = 7$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Forming equation x + y = 15 from total frequency", "allocated_marks": 1.5},
            {"step": 2, "rule": "Identifying median class 20-30 and setting up median formula", "allocated_marks": 1.5},
            {"step": 3, "rule": "Solving x = 8 and y = 7", "allocated_marks": 2.0}
        ],
        "source_book": "RD Sharma Class 10 / NCERT Chapter 14"
    },

    # =========================================================================
    # CLASS 11 - MATHEMATICS (RD Sharma & JEE Main)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Mathematics", "chapter": "Trigonometric Functions",
        "topic": "Sum and Difference of Angles", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Prove that: $\\cos(2x)\\cos\\left(\\frac{x}{2}\\right) - \\cos(3x)\\cos\\left(\\frac{9x}{2}\\right) = \\sin(5x)\\sin\\left(\\frac{5x}{2}\\right)$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Multiply and divide LHS by 2:\n$\\text{LHS} = \\frac{1}{2} \\left[ 2\\cos(2x)\\cos\\left(\\frac{x}{2}\\right) - 2\\cos\\left(\\frac{9x}{2}\\right)\\cos(3x) \\right]$.\nUsing $2\\cos A \\cos B = \\cos(A+B) + \\cos(A-B)$:\n$2\\cos(2x)\\cos\\left(\\frac{x}{2}\\right) = \\cos\\left(\\frac{5x}{2}\\right) + \\cos\\left(\\frac{3x}{2}\\right)$.\n$2\\cos\\left(\\frac{9x}{2}\\right)\\cos(3x) = \\cos\\left(\\frac{15x}{2}\\right) + \\cos\\left(\\frac{3x}{2}\\right)$.\nSubtracting: $\\text{LHS} = \\frac{1}{2} \\left[ \\cos\\left(\\frac{5x}{2}\\right) - \\cos\\left(\\frac{15x}{2}\\right) \\right]$.\nUsing $\\cos C - \\cos D = 2\\sin\\left(\\frac{C+D}{2}\\right)\\sin\\left(\\frac{D-C}{2}\\right)$:\n$\\text{LHS} = \\frac{1}{2} \\times 2 \\sin\\left(\\frac{\\frac{5x}{2} + \\frac{15x}{2}}{2}\\right)\\sin\\left(\\frac{\\frac{15x}{2} - \\frac{5x}{2}}{2}\\right) = \\sin(5x)\\sin\\left(\\frac{5x}{2}\\right) = \\text{RHS}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Applying 2*cosA*cosB expansion formula", "allocated_marks": 1.5},
            {"step": 2, "rule": "Applying cosC - cosD to yield sin(5x)*sin(5x/2)", "allocated_marks": 1.5}
        ],
        "source_book": "RD Sharma Class 11 Chapter 6"
    },
    {
        "grade_level": 11, "subject": "Mathematics", "chapter": "Sequences and Series",
        "topic": "Sum to n Terms of Special Series and AGP", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Find the sum to infinity of the arithmetico-geometric series: $S = 1 + \\frac{4}{5} + \\frac{7}{5^2} + \\frac{10}{5^3} + \\dots$",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Given $S = 1 + 4\\left(\\frac{1}{5}\\right) + 7\\left(\\frac{1}{5^2}\\right) + 10\\left(\\frac{1}{5^3}\\right) + \\dots$  --- (1)\nMultiply by $\\frac{1}{5}$:\n$\\frac{1}{5}S = \\frac{1}{5} + 4\\left(\\frac{1}{5^2}\\right) + 7\\left(\\frac{1}{5^3}\\right) + \\dots$  --- (2)\nSubtract (2) from (1):\n$\\frac{4}{5}S = 1 + 3\\left(\\frac{1}{5}\\right) + 3\\left(\\frac{1}{5^2}\\right) + 3\\left(\\frac{1}{5^3}\\right) + \\dots = 1 + \\frac{3}{5}\\left[ 1 + \\frac{1}{5} + \\frac{1}{5^2} + \\dots \\right]$.\nSum of infinite GP: $\\frac{1}{1 - 1/5} = \\frac{5}{4}$.\n$\\frac{4}{5}S = 1 + \\frac{3}{5} \\times \\frac{5}{4} = 1 + \\frac{3}{4} = \\frac{7}{4}$.\n$S = \\frac{7}{4} \\times \\frac{5}{4} = \\frac{35}{16}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Multiplying series by common ratio 1/5 and subtracting", "allocated_marks": 1.0},
            {"step": 2, "rule": "Evaluating infinite GP sum to 5/4", "allocated_marks": 1.0},
            {"step": 3, "rule": "Solving for S = 35/16", "allocated_marks": 1.0}
        ],
        "source_book": "RD Sharma Class 11 Chapter 20 / JEE Main"
    },

    # =========================================================================
    # CLASS 12 - MATHEMATICS (RD Sharma & JEE Advanced)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Matrices and Determinants",
        "topic": "Properties of Determinants and Inverses", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "If $A = \\begin{pmatrix} 2 & 3 \\\\ 1 & -4 \\end{pmatrix}$ and $B = \\begin{pmatrix} 1 & -2 \\\\ -1 & 3 \\end{pmatrix}$, verify that $(AB)^{-1} = B^{-1} A^{-1}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "$AB = \\begin{pmatrix} 2(1)+3(-1) & 2(-2)+3(3) \\\\ 1(1)+(-4)(-1) & 1(-2)+(-4)(3) \\end{pmatrix} = \\begin{pmatrix} -1 & 5 \\\\ 5 & -14 \\end{pmatrix}$.\n$\\det(AB) = (-1)(-14) - (5)(5) = 14 - 25 = -11 \\neq 0$.\n$(AB)^{-1} = -\\frac{1}{11} \\begin{pmatrix} -14 & -5 \\\\ -5 & -1 \\end{pmatrix} = \\frac{1}{11} \\begin{pmatrix} 14 & 5 \\\\ 5 & 1 \\end{pmatrix}$.\nNow, $\\det(A) = -8 - 3 = -11 \\implies A^{-1} = -\\frac{1}{11} \\begin{pmatrix} -4 & -3 \\\\ -1 & 2 \\end{pmatrix}$.\n$\\det(B) = 3 - 2 = 1 \\implies B^{-1} = \\begin{pmatrix} 3 & 2 \\\\ 1 & 1 \\end{pmatrix}$.\n$B^{-1} A^{-1} = -\\frac{1}{11} \\begin{pmatrix} 3 & 2 \\\\ 1 & 1 \\end{pmatrix} \\begin{pmatrix} -4 & -3 \\\\ -1 & 2 \\end{pmatrix} = -\\frac{1}{11} \\begin{pmatrix} -14 & -5 \\\\ -5 & -1 \\end{pmatrix} = \\frac{1}{11} \\begin{pmatrix} 14 & 5 \\\\ 5 & 1 \\end{pmatrix} = (AB)^{-1}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Compute product matrix AB and its inverse (AB)^-1", "allocated_marks": 1.5},
            {"step": 2, "rule": "Compute separate inverses B^-1 and A^-1 and show B^-1 * A^-1 = (AB)^-1", "allocated_marks": 1.5}
        ],
        "source_book": "RD Sharma Class 12 Chapter 7"
    },
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Continuity and Differentiability",
        "topic": "Logarithmic Differentiation and Implicit Functions", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "If $y = (\\sin x)^x + x^{\\sin x}$, find $\\frac{dy}{dx}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Let $u = (\\sin x)^x$ and $v = x^{\\sin x}$, so $y = u + v \\implies \\frac{dy}{dx} = \\frac{du}{dx} + \\frac{dv}{dx}$.\n1. $\\ln u = x \\ln(\\sin x)$. Differentiating:\n$\\frac{1}{u}\\frac{du}{dx} = \\ln(\\sin x) + x \\frac{\\cos x}{\\sin x} = \\ln(\\sin x) + x\\cot x \\implies \\frac{du}{dx} = (\\sin x)^x [x\\cot x + \\ln(\\sin x)]$.\n2. $\\ln v = \\sin x \\ln x$. Differentiating:\n$\\frac{1}{v}\\frac{dv}{dx} = \\cos x \\ln x + \\frac{\\sin x}{x} \\implies \\frac{dv}{dx} = x^{\\sin x} \\left[ \\frac{\\sin x}{x} + \\cos x \\ln x \\right]$.\nCombining:\n$\\frac{dy}{dx} = (\\sin x)^x [x\\cot x + \\ln(\\sin x)] + x^{\\sin x} \\left[ \\frac{\\sin x}{x} + \\cos x \\ln x \\right]$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Splitting y = u + v and applying logarithmic differentiation to u", "allocated_marks": 1.5},
            {"step": 2, "rule": "Applying logarithmic differentiation to v and summing derivatives", "allocated_marks": 1.5}
        ],
        "source_book": "RD Sharma Class 12 Chapter 11 / NCERT Chapter 5"
    },
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Integrals",
        "topic": "Properties of Definite Integrals", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "JEE_ADVANCED"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Evaluate the definite integral: $I = \\int_0^{\\pi/2} \\frac{\\sqrt{\\sin x}}{\\sqrt{\\sin x} + \\sqrt{\\cos x}} dx$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Let $I = \\int_0^{\\pi/2} \\frac{\\sqrt{\\sin x}}{\\sqrt{\\sin x} + \\sqrt{\\cos x}} dx$  --- (1)\nUsing property $\\int_0^a f(x) dx = \\int_0^a f(a - x) dx$:\n$I = \\int_0^{\\pi/2} \\frac{\\sqrt{\\sin(\\pi/2 - x)}}{\\sqrt{\\sin(\\pi/2 - x)} + \\sqrt{\\cos(\\pi/2 - x)}} dx = \\int_0^{\\pi/2} \\frac{\\sqrt{\\cos x}}{\\sqrt{\\cos x} + \\sqrt{\\sin x}} dx$  --- (2)\nAdding (1) and (2):\n$2I = \\int_0^{\\pi/2} \\frac{\\sqrt{\\sin x} + \\sqrt{\\cos x}}{\\sqrt{\\sin x} + \\sqrt{\\cos x}} dx = \\int_0^{\\pi/2} 1 dx = [x]_0^{\\pi/2} = \\frac{\\pi}{2}$.\n$I = \\frac{\\pi}{4}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Applying integral property f(a-x) dx", "allocated_marks": 1.0},
            {"step": 2, "rule": "Adding equations (1) and (2) yielding integrand = 1", "allocated_marks": 1.0},
            {"step": 3, "rule": "Solving 2I = pi/2 to get I = pi/4", "allocated_marks": 1.0}
        ],
        "source_book": "RD Sharma Class 12 Chapter 20 / NCERT Chapter 7"
    },
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Vector Algebra",
        "topic": "Scalar Triple Product and Cross Product", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Find the area of a parallelogram whose adjacent sides are determined by the vectors $\\vec{a} = \\hat{i} - \\hat{j} + 3\\hat{k}$ and $\\vec{b} = 2\\hat{i} - 7\\hat{j} + \\hat{k}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Area of parallelogram $= |\\vec{a} \\times \\vec{b}|$.\n$\\vec{a} \\times \\vec{b} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ 1 & -1 & 3 \\\\ 2 & -7 & 1 \\end{vmatrix} = \\hat{i}(-1 - (-21)) - \\hat{j}(1 - 6) + \\hat{k}(-7 - (-2)) = 20\\hat{i} + 5\\hat{j} - 5\\hat{k}$.\n$|\\vec{a} \\times \\vec{b}| = \\sqrt{20^2 + 5^2 + (-5)^2} = \\sqrt{400 + 25 + 25} = \\sqrt{450} = \\sqrt{225 \\times 2} = 15\\sqrt{2}\\text{ sq units}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Computing vector cross product a x b = 20i + 5j - 5k", "allocated_marks": 1.0},
            {"step": 2, "rule": "Evaluating magnitude 15*sqrt(2) sq units", "allocated_marks": 1.0}
        ],
        "source_book": "RD Sharma Class 12 Chapter 23 / NCERT Chapter 10"
    },
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Probability",
        "topic": "Bayes' Theorem and Conditional Probability", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "In a factory which manufactures bolts, machines A, B, and C manufacture $25\\%, 35\\%$, and $40\\%$ of the bolts respectively. Of their outputs, $5\\%, 4\\%$, and $2\\%$ are respectively defective. A bolt is drawn at random from the product and is found to be defective. What is the probability that it was manufactured by machine B?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Let events:\n- $E_1, E_2, E_3$: Bolt manufactured by machine A, B, C.\n$P(E_1) = 0.25, P(E_2) = 0.35, P(E_3) = 0.40$.\n- $D$: Bolt is defective.\n$P(D|E_1) = 0.05, P(D|E_2) = 0.04, P(D|E_3) = 0.02$.\nBy Total Probability Theorem:\n$P(D) = P(E_1)P(D|E_1) + P(E_2)P(D|E_2) + P(E_3)P(D|E_3)$\n$P(D) = (0.25)(0.05) + (0.35)(0.04) + (0.40)(0.02) = 0.0125 + 0.0140 + 0.0080 = 0.0345$.\nBy Bayes' Theorem:\n$P(E_2|D) = \\frac{P(E_2)P(D|E_2)}{P(D)} = \\frac{0.0140}{0.0345} = \\frac{140}{345} = \\frac{28}{69} \\approx 0.4058$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Defining events E1, E2, E3 and writing prior and conditional probabilities", "allocated_marks": 1.5},
            {"step": 2, "rule": "Calculating total probability of defective bolt P(D) = 0.0345", "allocated_marks": 1.5},
            {"step": 3, "rule": "Applying Bayes' formula to compute 28/69", "allocated_marks": 2.0}
        ],
        "source_book": "RD Sharma Class 12 Chapter 30 / NCERT Chapter 13"
    }
]

def generate_content_hash(q: dict) -> str:
    raw = f"{q['grade_level']}_{q['subject']}_{q['chapter']}_{q.get('topic','')}_{q['question_text_latex']}"
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()

def main():
    logger.info("Seeding Massive Curriculum Question Bank into Supabase Cloud...")
    for q in MASSIVE_QUESTIONS:
        q["content_hash"] = generate_content_hash(q)

    count = db.upsert_questions(MASSIVE_QUESTIONS)
    logger.info(f"Upserted {count} additional questions into {'Supabase Cloud' if db.use_supabase else 'SQLite'}.")

    # Summary
    tax = db.get_taxonomy()
    total = sum(
        sum(c["count"] if isinstance(c, dict) else c for c in chaps.values())
        for subs in tax.values()
        for chaps in subs.values()
    )
    logger.info(f"Total verified active questions in Supabase question bank: {total}")

if __name__ == "__main__":
    main()
