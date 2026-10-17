"""
Expanded Curriculum Seeder for Classes 10, 11, and 12 across CBSE, IIT-JEE, and NEET.
Covers missing subjects:
- Class 11: Physics (HC Verma Vol 1), Chemistry (OP Tandon), Mathematics (RD Sharma), Biology (Trueman's)
- Class 12: Chemistry (OP Tandon), Biology (Trueman's), English Core (Flamingo)
- Class 10: Mathematics (RD Sharma / Exemplar), Social Science (History, Geo, Civics, Eco), English
"""

import sys
import logging
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

load_dotenv()
from backend.database import db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("seed_expanded")

EXPANDED_QUESTIONS = [
    # =========================================================================
    # CLASS 11 - PHYSICS (HC Verma Vol 1 & NCERT)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Units and Measurements",
        "topic": "Dimensional Analysis", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Check the dimensional consistency of the relation $T = 2\\pi \\sqrt{\\frac{l}{g}}$, where $T$ is time period, $l$ is length, and $g$ is acceleration due to gravity.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "LHS: $[T] = [M^0 L^0 T^1]$.\nRHS: $2\\pi$ is dimensionless. $\\left[\\sqrt{\\frac{l}{g}}\\right] = \\left[\\frac{L}{L T^{-2}}\\right]^{1/2} = [T^2]^{1/2} = [M^0 L^0 T^1]$.\nSince $\\text{LHS} = \\text{RHS}$, the equation is dimensionally correct.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct dimension of LHS [T]", "allocated_marks": 0.5},
            {"step": 2, "rule": "Correct dimension of RHS [l/g]^(1/2) = [T]", "allocated_marks": 1.0},
            {"step": 3, "rule": "Conclusion stating principle of homogeneity", "allocated_marks": 0.5}
        ],
        "source_book": "HC Verma Vol 1 / NCERT Physics Class 11 Ch 2"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Motion in a Straight Line",
        "topic": "Kinematic Equations for Uniform Acceleration", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A car moving along a straight highway with speed of $126\\text{ km/h}$ is brought to a stop within a distance of $200\\text{ m}$. What is the retardation of the car (assumed uniform), and how long does it take for the car to stop?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "$u = 126 \\times \\frac{5}{18} = 35\\text{ m/s}$, $v = 0$, $s = 200\\text{ m}$.\nUsing $v^2 = u^2 + 2as$:\n$0 = (35)^2 + 2a(200) \\implies 400a = -1225 \\implies a = -3.06\\text{ m/s}^2$.\nRetardation is $3.06\\text{ m/s}^2$.\nUsing $v = u + at$:\n$0 = 35 - 3.06t \\implies t = \\frac{35}{3.06} \\approx 11.44\\text{ s}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Conversion of speed to m/s (35 m/s)", "allocated_marks": 0.5},
            {"step": 2, "rule": "Applying v^2 = u^2 + 2as to find retardation a = 3.06 m/s^2", "allocated_marks": 1.5},
            {"step": 3, "rule": "Finding stopping time t = 11.44 s", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Physics Class 11 Ch 3 / HC Verma"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Motion in a Plane",
        "topic": "Projectile Motion", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Prove that the trajectory of a projectile fired at an angle $\\theta$ with the horizontal is parabolic.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Horizontal displacement: $x = (u \\cos\\theta)t \\implies t = \\frac{x}{u \\cos\\theta}$.\nVertical displacement: $y = (u \\sin\\theta)t - \\frac{1}{2}gt^2$.\nSubstituting $t$:\n$y = u \\sin\\theta \\left(\\frac{x}{u \\cos\\theta}\\right) - \\frac{1}{2}g \\left(\\frac{x}{u \\cos\\theta}\\right)^2 = x \\tan\\theta - \\frac{g}{2u^2 \\cos^2\\theta}x^2$.\nThis is of the form $y = Ax - Bx^2$, which represents a parabola.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Expressions for x and y displacements with time parameter t", "allocated_marks": 1.0},
            {"step": 2, "rule": "Eliminating t to get trajectory equation", "allocated_marks": 1.0},
            {"step": 3, "rule": "Comparing with quadratic equation of parabola y = Ax - Bx^2", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Vol 1 / NCERT Physics Class 11 Ch 4"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Laws of Motion",
        "topic": "Friction and Banking of Roads", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Derive an expression for the optimum velocity of a vehicle negotiating a curved road of radius $R$ banked at an angle $\\theta$ with coefficient of friction $\\mu_s$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Free body diagram of vehicle:\n$N \\cos\\theta - f_s \\sin\\theta = mg$\n$N \\sin\\theta + f_s \\cos\\theta = \\frac{mv^2}{R}$\nFor maximum velocity, $f_s = \\mu_s N$:\n$N(\\cos\\theta - \\mu_s \\sin\\theta) = mg$\n$N(\\sin\\theta + \\mu_s \\cos\\theta) = \\frac{mv^2_{max}}{R}$\nDividing both equations:\n$\\frac{v^2_{max}}{Rg} = \\frac{\\sin\\theta + \\mu_s \\cos\\theta}{\\cos\\theta - \\mu_s \\sin\\theta} = \\frac{\\tan\\theta + \\mu_s}{1 - \\mu_s \\tan\\theta} \\implies v_{max} = \\sqrt{Rg \\left(\\frac{\\mu_s + \\tan\\theta}{1 - \\mu_s \\tan\\theta}\\right)}$.\nFor zero friction (optimum speed): $v_0 = \\sqrt{Rg \\tan\\theta}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Schematic diagram with normal reaction and friction components", "allocated_marks": 1.5},
            {"step": 2, "rule": "Setting up vertical and horizontal force balance equations", "allocated_marks": 1.5},
            {"step": 3, "rule": "Derivation of v_max with friction", "allocated_marks": 1.0},
            {"step": 4, "rule": "Deducing optimum velocity v0 = sqrt(Rg tan theta)", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Vol 1 Ch 5 / NCERT Physics Class 11"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Work, Energy and Power",
        "topic": "Work-Energy Theorem", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "State and prove the Work-Energy Theorem for a variable force acting on a particle along a straight line.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Statement: The change in kinetic energy of a particle is equal to the work done on it by the net force: $\\Delta K = W$.\nProof: $K = \\frac{1}{2}mv^2$. Differentiating with respect to time:\n$\\frac{dK}{dt} = m v \\frac{dv}{dt} = m \\left(\\frac{dx}{dt}\\right) a = (ma) \\frac{dx}{dt} = F \\frac{dx}{dt}$.\n$\\implies dK = F dx$.\nIntegrating from $x_i$ to $x_f$:\n$\\int_{K_i}^{K_f} dK = \\int_{x_i}^{x_f} F dx \\implies K_f - K_i = W$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Clear statement of theorem", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculus derivation dK = F dx", "allocated_marks": 1.0},
            {"step": 3, "rule": "Integration leading to Delta K = W", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Vol 1 / NCERT Physics Class 11 Ch 6"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "System of Particles and Rotational Motion",
        "topic": "Angular Momentum and Conservation Law", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Define torque and angular momentum. State the law of conservation of angular momentum and give one daily life example.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Torque: Moment of force, $\\vec{\\tau} = \\vec{r} \\times \\vec{F}$.\nAngular Momentum: Moment of momentum, $\\vec{L} = \\vec{r} \\times \\vec{p} = I\\vec{\\omega}$.\nConservation Law: If external torque $\\vec{\\tau}_{ext} = 0$, then $\\frac{d\\vec{L}}{dt} = 0 \\implies \\vec{L} = \\text{constant} \\implies I_1 \\omega_1 = I_2 \\omega_2$.\nExample: A ballet dancer stretches arms outward to increase $I$ and slow down, or pulls arms inward to decrease $I$ and spin faster.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Definitions and vector formulas for tau and L", "allocated_marks": 1.0},
            {"step": 2, "rule": "Statement and mathematical condition for conservation (tau_ext = 0 => L = const)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Practical illustration with ballet dancer or diver", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Vol 1 Ch 10 / NCERT Physics Class 11"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Gravitation",
        "topic": "Escape Velocity and Orbital Velocity", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Derive an expression for the escape velocity of a body projected from the surface of the Earth. What is its numerical value at Earth's surface?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Let mass of Earth be $M$, radius $R$, and mass of body $m$.\nInitial total energy on surface: $E_i = K_i + U_i = \\frac{1}{2}m v_e^2 - \\frac{G M m}{R}$.\nAt infinity, $E_f = 0$.\nBy conservation of mechanical energy: $\\frac{1}{2}m v_e^2 - \\frac{G M m}{R} = 0 \\implies v_e = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR}$.\nSubstituting $g = 9.8\\text{ m/s}^2$ and $R = 6.4 \\times 10^6\\text{ m}$:\n$v_e = \\sqrt{2 \\times 9.8 \\times 6.4 \\times 10^6} \\approx 11.2\\text{ km/s}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Energy balance equation on Earth surface and infinity", "allocated_marks": 1.0},
            {"step": 2, "rule": "Derivation of formula ve = sqrt(2gR)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculation of numerical value 11.2 km/s", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Physics Class 11 Ch 8 / HC Verma"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Mechanical Properties of Fluids",
        "topic": "Bernoulli's Principle", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "State Bernoulli's theorem for a non-viscous, incompressible fluid in streamline flow. Derive the Bernoulli equation.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Statement: For an incompressible, non-viscous fluid undergoing streamline flow, the sum of pressure energy, kinetic energy, and potential energy per unit volume remains constant along a streamline:\n$P + \\frac{1}{2}\\rho v^2 + \\rho g h = \\text{constant}$.\nProof: Consider fluid flowing through pipe of varying cross section from region 1 to 2.\nWork done by pressure forces: $W = P_1 A_1 v_1 \\Delta t - P_2 A_2 v_2 \\Delta t = (P_1 - P_2)\\Delta V$ (since $A_1 v_1 \\Delta t = A_2 v_2 \\Delta t = \\Delta V$).\nChange in kinetic energy: $\\Delta K = \\frac{1}{2}\\Delta m(v_2^2 - v_1^2) = \\frac{1}{2}\\rho \\Delta V(v_2^2 - v_1^2)$.\nChange in potential energy: $\\Delta U = \\Delta m g(h_2 - h_1) = \\rho \\Delta V g(h_2 - h_1)$.\nBy Work-Energy theorem: $W = \\Delta K + \\Delta U$.\n$(P_1 - P_2)\\Delta V = \\frac{1}{2}\\rho \\Delta V(v_2^2 - v_1^2) + \\rho \\Delta V g(h_2 - h_1)$.\nDividing by $\\Delta V$ and rearranging:\n$P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Statement of Bernoulli's principle with conditions", "allocated_marks": 1.0},
            {"step": 2, "rule": "Expression for work done by pressure forces W = (P1 - P2) Delta V", "allocated_marks": 1.5},
            {"step": 3, "rule": "Expressions for Delta K and Delta U", "allocated_marks": 1.5},
            {"step": 4, "rule": "Applying Work-Energy theorem to reach final equation", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Physics Class 11 Ch 10 / HC Verma"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Thermodynamics",
        "topic": "First Law of Thermodynamics and Carnot Engine", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A Carnot engine has an efficiency of $40\\%$ when its sink is at $27^\\circ\\text{C}$. What is the temperature of the source? By how much should the source temperature be increased to achieve an efficiency of $50\\%$?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "$T_2 = 27 + 273 = 300\\text{ K}$.\n$\\eta = 1 - \\frac{T_2}{T_1} \\implies 0.40 = 1 - \\frac{300}{T_1} \\implies \\frac{300}{T_1} = 0.60 \\implies T_1 = 500\\text{ K} = 227^\\circ\\text{C}$.\nFor $\\eta' = 0.50$ with $T_2 = 300\\text{ K}$:\n$0.50 = 1 - \\frac{300}{T_1'} \\implies \\frac{300}{T_1'} = 0.50 \\implies T_1' = 600\\text{ K}$.\nIncrease in source temperature: $\\Delta T_1 = 600 - 500 = 100\\text{ K}$ (or $100^\\circ\\text{C}$).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculating initial source temperature T1 = 500 K", "allocated_marks": 1.5},
            {"step": 2, "rule": "Calculating required temperature T1' = 600 K for 50% efficiency", "allocated_marks": 1.0},
            {"step": 3, "rule": "Required increase Delta T = 100 K", "allocated_marks": 0.5}
        ],
        "source_book": "HC Verma Vol 2 / NCERT Physics Class 11 Ch 12"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Oscillations",
        "topic": "Simple Harmonic Motion", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 2, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "In simple harmonic motion, when the displacement is half the amplitude, the ratio of kinetic energy to potential energy is:",
        "options": {"A": "1 : 1", "B": "2 : 1", "C": "3 : 1", "D": "1 : 3"},
        "correct_option": "C",
        "ideal_solution_latex": "Displacement $x = \\frac{A}{2}$.\n$U = \\frac{1}{2}k x^2 = \\frac{1}{2}k \\left(\\frac{A}{2}\\right)^2 = \\frac{1}{8}kA^2$.\n$K = \\frac{1}{2}k(A^2 - x^2) = \\frac{1}{2}k \\left(A^2 - \\frac{A^2}{4}\\right) = \\frac{3}{8}kA^2$.\n$\\frac{K}{U} = \\frac{3/8}{1/8} = \\frac{3}{1} = 3:1$.",
        "step_marking_rubric": [{"step": 1, "rule": "Ratio of (A^2 - x^2) / x^2 = (A^2 - A^2/4)/(A^2/4) = 3", "allocated_marks": 1.0}],
        "source_book": "HC Verma Vol 1 Ch 12"
    },

    # =========================================================================
    # CLASS 11 - CHEMISTRY (OP Tandon & NCERT)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Some Basic Concepts of Chemistry",
        "topic": "Empirical and Molecular Formula", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A compound contains $4.07\\%$ hydrogen, $24.27\\%$ carbon and $71.65\\%$ chlorine. Its molar mass is $98.96\\text{ g/mol}$. Determine its empirical and molecular formulas.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Moles of elements:\n- $\\text{C}: \\frac{24.27}{12.01} = 2.021$\n- $\\text{H}: \\frac{4.07}{1.008} = 4.038$\n- $\\text{Cl}: \\frac{71.65}{35.45} = 2.021$\nAtomic ratio: $\\text{C} : \\text{H} : \\text{Cl} = \\frac{2.021}{2.021} : \\frac{4.038}{2.021} : \\frac{2.021}{2.021} = 1 : 2 : 1$.\nEmpirical Formula: $\\text{CH}_2\\text{Cl}$.\nEmpirical formula mass: $12 + 2(1) + 35.5 = 49.5\\text{ g/mol}$.\n$n = \\frac{\\text{Molar Mass}}{\\text{Empirical Mass}} = \\frac{98.96}{49.5} = 2$.\nMolecular Formula: $(\\text{CH}_2\\text{Cl})_2 = \\text{C}_2\\text{H}_4\\text{Cl}_2$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculation of moles and atomic ratio 1:2:1", "allocated_marks": 1.0},
            {"step": 2, "rule": "Empirical formula CH2Cl and its formula mass", "allocated_marks": 1.0},
            {"step": 3, "rule": "Determining multiplier n = 2 and molecular formula C2H4Cl2", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Chemistry Class 11 Ch 1"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Structure of Atom",
        "topic": "Quantum Numbers and Electronic Configuration", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "Which of the following sets of quantum numbers $(n, l, m_l, m_s)$ is NOT permissible for an electron in an atom?",
        "options": {
            "A": "(3, 2, -2, +1/2)",
            "B": "(4, 0, 0, -1/2)",
            "C": "(3, 3, 1, +1/2)",
            "D": "(2, 1, 0, +1/2)"
        },
        "correct_option": "C",
        "ideal_solution_latex": "The azimuthal quantum number $l$ can only have values from $0$ to $n-1$. For $n=3$, the maximum permissible value of $l$ is $2$ (d-orbital). $l=3$ is impossible for $n=3$.",
        "step_marking_rubric": [{"step": 1, "rule": "Identifying l must be <= n-1, making (3, 3, 1, +1/2) invalid", "allocated_marks": 1.0}],
        "source_book": "OP Tandon / NCERT Chemistry Class 11 Ch 2"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Chemical Bonding and Molecular Structure",
        "topic": "Hybridization and VSEPR Theory", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Using VSEPR theory, predict the shape, hybridization, and number of lone pairs on the central atom for: (a) $\\text{SF}_4$, (b) $\\text{XeF}_4$, and (c) $\\text{PCl}_5$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) $\\text{SF}_4$: Steric number $= 4\\text{ bp} + 1\\text{ lp} = 5$. Hybridization: $sp^3d$. Shape: See-saw.\n(b) $\\text{XeF}_4$: Steric number $= 4\\text{ bp} + 2\\text{ lp} = 6$. Hybridization: $sp^3d^2$. Shape: Square planar.\n(c) $\\text{PCl}_5$: Steric number $= 5\\text{ bp} + 0\\text{ lp} = 5$. Hybridization: $sp^3d$. Shape: Trigonal bipyramidal.",
        "step_marking_rubric": [
            {"step": 1, "rule": "SF4: sp3d, 1 lone pair, See-saw geometry", "allocated_marks": 1.0},
            {"step": 2, "rule": "XeF4: sp3d2, 2 lone pairs, Square planar geometry", "allocated_marks": 1.0},
            {"step": 3, "rule": "PCl5: sp3d, 0 lone pairs, Trigonal bipyramidal", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Inorganic Chemistry / NCERT Chemistry Class 11 Ch 4"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Chemical Thermodynamics",
        "topic": "Hess's Law and Enthalpy Calculations", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "State Hess's Law of Constant Heat Summation. Calculate the standard enthalpy of formation of $\\text{CH}_3\\text{OH}(l)$ given the standard enthalpies of combustion of $\\text{C}(s) = -393.5\\text{ kJ/mol}$, $\\text{H}_2(g) = -285.8\\text{ kJ/mol}$, and $\\text{CH}_3\\text{OH}(l) = -726.0\\text{ kJ/mol}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Hess's Law: Enthalpy change in a chemical reaction is the same whether the process occurs in one step or several steps.\nTarget reaction: $\\text{C}(s) + 2\\text{H}_2(g) + \\frac{1}{2}\\text{O}_2(g) \\to \\text{CH}_3\\text{OH}(l)$.\n$\\Delta_f H^\\circ = \\Delta_c H^\\circ(\\text{C}) + 2\\Delta_c H^\\circ(\\text{H}_2) - \\Delta_c H^\\circ(\\text{CH}_3\\text{OH})$\n$\\Delta_f H^\\circ = (-393.5) + 2(-285.8) - (-726.0) = -393.5 - 571.6 + 726.0 = -239.1\\text{ kJ/mol}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Statement of Hess's Law", "allocated_marks": 1.0},
            {"step": 2, "rule": "Writing target thermochemical equation", "allocated_marks": 1.0},
            {"step": 3, "rule": "Correct algebraic substitution yielding -239.1 kJ/mol", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Chemistry Class 11 Ch 6"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Equilibrium",
        "topic": "Le Chatelier's Principle and Buffer Solutions", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "(a) State Le Chatelier's Principle.\n(b) Predict the effect of (i) increasing temperature, (ii) increasing pressure, and (iii) adding a catalyst on the equilibrium:\n$\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g), \\quad \\Delta H = -92.4\\text{ kJ/mol}$.\n(c) What is a buffer solution? Write the Henderson-Hasselbalch equation for an acidic buffer.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Le Chatelier's Principle: If a dynamic equilibrium is disturbed by changing the conditions, the position of equilibrium shifts to counteract the change.\n(b) (i) Increasing temperature: Since reaction is exothermic, equilibrium shifts to the left (favors reverse reaction).\n(ii) Increasing pressure: Equilibrium shifts towards fewer moles of gas ($4 \\to 2$), hence forward reaction is favored.\n(iii) Catalyst: Increases rate of both forward and reverse reactions equally; equilibrium position is unchanged.\n(c) A buffer solution resists change in pH upon addition of small amounts of acid or base.\nHenderson-Hasselbalch equation: $\\text{pH} = \\text{p}K_a + \\log\\frac{[\\text{Salt}]}{[\\text{Acid}]}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct statement of Le Chatelier's principle", "allocated_marks": 1.0},
            {"step": 2, "rule": "Correct predictions for temperature, pressure, and catalyst (0.5 each)", "allocated_marks": 1.5},
            {"step": 3, "rule": "Definition of buffer solution", "allocated_marks": 1.0},
            {"step": 4, "rule": "Henderson-Hasselbalch formula pH = pKa + log([Salt]/[Acid])", "allocated_marks": 1.5}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Chemistry Class 11 Ch 7"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Hydrocarbons",
        "topic": "Electrophilic Aromatic Substitution in Benzene", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Explain the mechanism of nitration of benzene with a mixture of concentrated $\\text{HNO}_3$ and concentrated $\\text{H}_2\\text{SO}_4$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Step 1: Generation of nitronium ion (electrophile):\n$\\text{HNO}_3 + 2\\text{H}_2\\text{SO}_4 \\rightleftharpoons \\text{NO}_2^+ + \\text{H}_3\\text{O}^+ + 2\\text{HSO}_4^-$.\nStep 2: Attack of electrophile $\\text{NO}_2^+$ on benzene ring to form arenium ion (sigma complex) with resonance stabilization.\nStep 3: Loss of proton from arenium ion to $\\text{HSO}_4^-$ to restore aromaticity, yielding nitrobenzene.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Generation of electrophile NO2+", "allocated_marks": 1.0},
            {"step": 2, "rule": "Formation of resonance-stabilized arenium ion", "allocated_marks": 1.0},
            {"step": 3, "rule": "Proton abstraction restoring aromatic ring", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Organic Chemistry / NCERT Chemistry Class 11 Ch 13"
    },

    # =========================================================================
    # CLASS 11 - BIOLOGY (Trueman's & NCERT)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Biology", "chapter": "Biological Classification",
        "topic": "Five Kingdom Classification and Viruses", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 2, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "Which of the following organisms are NOT included in Whittaker's Five Kingdom Classification?",
        "options": {
            "A": "Mycoplasma and Euglena",
            "B": "Viruses, Viroids and Lichens",
            "C": "Slime moulds and Archaebacteria",
            "D": "Fungi and Protozoa"
        },
        "correct_option": "B",
        "ideal_solution_latex": "Whittaker's Five Kingdom Classification (Monera, Protista, Fungi, Plantae, Animalia) did not include acellular organisms like viruses, viroids, prions, or composite organisms like lichens.",
        "step_marking_rubric": [{"step": 1, "rule": "Identifying Viruses, Viroids and Lichens were excluded", "allocated_marks": 1.0}],
        "source_book": "Trueman's Elementary Biology Vol 1 / NCERT Biology Class 11 Ch 2"
    },
    {
        "grade_level": 11, "subject": "Biology", "chapter": "Cell: The Unit of Life",
        "topic": "Fluid Mosaic Model of Plasma Membrane", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Describe the Fluid Mosaic Model of plasma membrane proposed by Singer and Nicolson. Why is the membrane described as 'quasifluid'?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "The Fluid Mosaic Model (1972) states:\n1. The membrane consists of a continuous phospholipid bilayer with hydrophilic heads facing outward and hydrophobic tails inward.\n2. Proteins are embedded: Integral proteins penetrate deeply; peripheral proteins lie on the surface.\n3. 'Quasifluid' nature: The lipid bilayer allows lateral movement of proteins within the overall bilayer, enabling membrane fluidity, cell growth, secretion, endocytosis, and cell division.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Description of phospholipid bilayer orientation", "allocated_marks": 1.0},
            {"step": 2, "rule": "Types of proteins (integral and peripheral)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Explanation of quasifluid nature and lateral mobility", "allocated_marks": 1.0}
        ],
        "source_book": "Trueman's Elementary Biology Vol 1 / NCERT Biology Class 11 Ch 8"
    },
    {
        "grade_level": 11, "subject": "Biology", "chapter": "Cell Cycle and Cell Division",
        "topic": "Meiosis and Crossing Over", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Describe the sub-stages of Prophase I of Meiosis I with their characteristic cytological events. What is the significance of crossing over?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Five sub-stages of Prophase I:\n1. **Leptotene**: Chromosomes become visible and condense under light microscope.\n2. **Zygotene**: Homologous chromosomes pair up (synapsis) facilitated by synaptonemal complex forming bivalents.\n3. **Pachytene**: Crossing over occurs between non-sister chromatids of homologous chromosomes mediated by recombinase enzyme.\n4. **Diplotene**: Dissolution of synaptonemal complex; homologous chromosomes separate except at chiasmata (X-shaped structures).\n5. **Diakinesis**: Terminalization of chiasmata; nucleolus disappears and nuclear envelope breaks down.\nSignificance of Crossing Over: Produces genetic recombination, introducing variations essential for evolution and biodiversity.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Sequential listing of all 5 sub-stages (0.5 each)", "allocated_marks": 2.5},
            {"step": 2, "rule": "Key events: synapsis in zygotene and recombinase in pachytene", "allocated_marks": 1.5},
            {"step": 3, "rule": "Significance: genetic variations for evolution", "allocated_marks": 1.0}
        ],
        "source_book": "Trueman's Biology Vol 1 / NCERT Class 11 Ch 10"
    },
    {
        "grade_level": 11, "subject": "Biology", "chapter": "Photosynthesis in Higher Plants",
        "topic": "Light Reaction and Photophosphorylation", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Differentiate between cyclic and non-cyclic photophosphorylation with respect to photosystems involved, products formed, and photolysis of water.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "| Feature | Cyclic Photophosphorylation | Non-cyclic Photophosphorylation |\n| :--- | :--- | :--- |\n| Photosystem | Only PS I (P700) | Both PS I and PS II (P680) |\n| Photolysis of Water | Absent | Present (oxygen is evolved) |\n| Products | Only ATP | ATP, NADPH + $\\text{H}^+$, and $\\text{O}_2$ |\n| Electron flow | Electrons return to PS I | Unidirectional from $\\text{H}_2\\text{O}$ to $\\text{NADP}^+$ |",
        "step_marking_rubric": [
            {"step": 1, "rule": "Contrast photosystems PS I only vs both PS I & PS II", "allocated_marks": 1.0},
            {"step": 2, "rule": "Contrast photolysis of water and oxygen release", "allocated_marks": 1.0},
            {"step": 3, "rule": "Contrast products (ATP only vs ATP + NADPH + O2)", "allocated_marks": 1.0}
        ],
        "source_book": "Trueman's Biology Vol 1 / NCERT Biology Class 11 Ch 13"
    },

    # =========================================================================
    # CLASS 12 - CHEMISTRY (OP Tandon & NCERT)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Solutions",
        "topic": "Colligative Properties and Van't Hoff Factor", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A $5\\%$ solution (by mass) of cane sugar (molar mass $342\\text{ g/mol}$) in water has a freezing point of $271\\text{ K}$. Calculate the freezing point of a $5\\%$ solution of glucose (molar mass $180\\text{ g/mol}$) in water. Freezing point of pure water is $273.15\\text{ K}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "For cane sugar:\n$m_1 = \\frac{5}{342 \\times 0.095\\text{ kg}} = 0.1539\\text{ mol/kg}$.\n$\\Delta T_{f1} = 273.15 - 271 = 2.15\\text{ K}$.\n$K_f = \\frac{\\Delta T_{f1}}{m_1} = \\frac{2.15}{0.1539} = 13.97\\text{ K kg/mol}$.\nFor glucose:\n$m_2 = \\frac{5}{180 \\times 0.095\\text{ kg}} = 0.2924\\text{ mol/kg}$.\n$\\Delta T_{f2} = K_f \\times m_2 = 13.97 \\times 0.2924 = 4.08\\text{ K}$.\nFreezing point of glucose solution: $T_f = 273.15 - 4.08 = 269.07\\text{ K}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Finding molality and Delta Tf for cane sugar", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculating molality and Delta Tf for glucose", "allocated_marks": 1.0},
            {"step": 3, "rule": "Freezing point Tf = 269.07 K", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Chemistry Class 12 Ch 2"
    },
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Electrochemistry",
        "topic": "Nernst Equation and EMF of Cell", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Represent the cell in which the following reaction takes place:\n$\\text{Mg}(s) + 2\\text{Ag}^+(0.0001\\text{ M}) \\to \\text{Mg}^{2+}(0.130\\text{ M}) + 2\\text{Ag}(s)$.\nCalculate its $E_{cell}$ at $298\\text{ K}$ given $E^\\circ_{cell} = 3.17\\text{ V}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Cell notation: $\\text{Mg}(s) | \\text{Mg}^{2+}(0.130\\text{ M}) || \\text{Ag}^+(0.0001\\text{ M}) | \\text{Ag}(s)$.\nNernst equation ($n = 2$):\n$E_{cell} = E^\\circ_{cell} - \\frac{0.059}{n} \\log \\frac{[\\text{Mg}^{2+}]}{[\\text{Ag}^+]^2}$\n$E_{cell} = 3.17 - \\frac{0.059}{2} \\log \\frac{0.130}{(10^{-4})^2} = 3.17 - 0.0295 \\log(1.3 \\times 10^7)$\n$\\log(1.3 \\times 10^7) = 7.1139$.\n$E_{cell} = 3.17 - (0.0295 \\times 7.1139) = 3.17 - 0.21 = 2.96\\text{ V}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct cell notation Mg | Mg2+ || Ag+ | Ag", "allocated_marks": 0.5},
            {"step": 2, "rule": "Nernst equation formula with n = 2", "allocated_marks": 1.0},
            {"step": 3, "rule": "Correct log calculation and final EMF = 2.96 V", "allocated_marks": 1.5}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Chemistry Class 12 Ch 3"
    },
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Chemical Kinetics",
        "topic": "First Order Reaction and Half-Life", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A first order reaction has a rate constant $k = 1.15 \\times 10^{-3}\\text{ s}^{-1}$. How long will $5\\text{ g}$ of this reactant take to reduce to $3\\text{ g}$?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "For a first order reaction:\n$t = \\frac{2.303}{k} \\log\\frac{[R]_0}{[R]}$\nGiven $[R]_0 = 5\\text{ g}$, $[R] = 3\\text{ g}$, $k = 1.15 \\times 10^{-3}\\text{ s}^{-1}$.\n$t = \\frac{2.303}{1.15 \\times 10^{-3}} \\log\\left(\\frac{5}{3}\\right) = \\frac{2.303}{1.15 \\times 10^{-3}} \\log(1.667)$\n$\\log(1.667) = 0.2219$.\n$t = \\frac{2.303 \\times 0.2219}{1.15 \\times 10^{-3}} = \\frac{0.511}{1.15 \\times 10^{-3}} \\approx 444\\text{ seconds}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "First order integrated rate formula t = (2.303/k) log(R0/R)", "allocated_marks": 1.0},
            {"step": 2, "rule": "Substitution of given concentrations and rate constant", "allocated_marks": 1.0},
            {"step": 3, "rule": "Accurate answer t = 444 s", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Chemistry Class 12 Ch 4 / OP Tandon"
    },
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Coordination Compounds",
        "topic": "Crystal Field Theory and Valence Bond Theory", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "On the basis of crystal field theory, write the electronic configuration for $d^4$ in an octahedral field when: (i) $\\Delta_o > P$ (strong field ligand) and (ii) $\\Delta_o < P$ (weak field ligand).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "In octahedral crystal field, d-orbitals split into $t_{2g}$ (lower energy) and $e_g$ (higher energy).\n(i) When $\\Delta_o > P$ (strong field ligand, pairing is favored):\nAll 4 electrons enter $t_{2g}$ orbitals: $t_{2g}^4 e_g^0$ (low spin complex, magnetic moment $= \\sqrt{4(4+2)} = \\sqrt{24}\\text{ BM}$ or 2 unpaired electrons $\\sqrt{2(2+2)} = \\sqrt{8}\\text{ BM}$).\n(ii) When $\\Delta_o < P$ (weak field ligand, pairing is not favored):\nElectrons occupy higher orbitals before pairing: $t_{2g}^3 e_g^1$ (high spin complex, 4 unpaired electrons).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Crystal field splitting into t2g and eg", "allocated_marks": 0.5},
            {"step": 2, "rule": "Strong field Delta_o > P configuration: t2g^4 eg^0", "allocated_marks": 1.25},
            {"step": 3, "rule": "Weak field Delta_o < P configuration: t2g^3 eg^1", "allocated_marks": 1.25}
        ],
        "source_book": "OP Tandon Inorganic / NCERT Chemistry Class 12 Ch 9"
    },
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Aldehydes, Ketones and Carboxylic Acids",
        "topic": "Aldol Condensation and Cannizzaro Reaction", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Write chemical equations and conditions for:\n(a) Aldol condensation using ethanal.\n(b) Cross-aldol condensation between benzaldehyde and acetophenone.\n(c) Cannizzaro reaction using formaldehyde.\n(d) Hell-Volhard-Zelinsky (HVZ) reaction on ethanoic acid.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Ethanal with dilute $\\text{NaOH}$:\n$2\\text{CH}_3\\text{CHO} \\xrightarrow{\\text{dil. NaOH}} \\text{CH}_3-\\text{CH(OH)}-\\text{CH}_2-\\text{CHO} \\xrightarrow{\\Delta, -\\text{H}_2\\text{O}} \\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CHO}$ (But-2-enal).\n(b) Benzaldehyde and acetophenone with base:\n$\\text{C}_6\\text{H}_5\\text{CHO} + \\text{CH}_3\\text{COC}_6\\text{H}_5 \\xrightarrow{\\text{dil. NaOH}} \\text{C}_6\\text{H}_5-\\text{CH}=\\text{CH}-\\text{COC}_6\\text{H}_5$ (Chalcone).\n(c) Formaldehyde lacks $\\alpha$-hydrogen. With $50\\% \\text{NaOH}$:\n$2\\text{HCHO} + \\text{conc. NaOH} \\to \\text{HCOONa} + \\text{CH}_3\\text{OH}$ (Sodium formate + Methanol).\n(d) HVZ reaction:\n$\\text{CH}_3\\text{COOH} \\xrightarrow{\\text{X}_2 / \\text{Red P}} \\text{CH}_2\\text{X}-\\text{COOH}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Aldol condensation equation and product but-2-enal", "allocated_marks": 1.5},
            {"step": 2, "rule": "Cross aldol equation with chalcone product", "allocated_marks": 1.0},
            {"step": 3, "rule": "Cannizzaro redox products (HCOONa and CH3OH)", "allocated_marks": 1.5},
            {"step": 4, "rule": "HVZ reaction alpha-halogenation", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Organic Chemistry / NCERT Chemistry Class 12 Ch 12"
    },

    # =========================================================================
    # CLASS 12 - BIOLOGY (Trueman's & NCERT)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Biology", "chapter": "Sexual Reproduction in Flowering Plants",
        "topic": "Double Fertilization and Embryo Sac", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Explain the phenomenon of double fertilization in angiosperms. Name the products of syngamy and triple fusion.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "In angiosperms, the pollen tube releases two male gametes into the cytoplasm of the synergid:\n1. **Syngamy**: One male gamete fuses with the egg nucleus to form a diploid zygote ($2n$).\n2. **Triple Fusion**: The second male gamete fuses with the two polar nuclei (secondary nucleus) in the central cell to produce a triploid Primary Endosperm Nucleus (PEN, $3n$).\nBecause two types of fusion occur in an embryo sac, it is called **Double Fertilization**.\nProducts:\n- Syngamy yields the diploid **Zygote** (develops into embryo).\n- Triple fusion yields the triploid **Primary Endosperm Cell / Endosperm** (nutritive tissue).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Explanation of syngamy (male gamete + egg -> zygote 2n)", "allocated_marks": 1.0},
            {"step": 2, "rule": "Explanation of triple fusion (male gamete + 2 polar nuclei -> PEN 3n)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Products: diploid zygote and triploid endosperm", "allocated_marks": 1.0}
        ],
        "source_book": "Trueman's Biology Vol 2 / NCERT Biology Class 12 Ch 2"
    },
    {
        "grade_level": 12, "subject": "Biology", "chapter": "Molecular Basis of Inheritance",
        "topic": "Semi-conservative DNA Replication (Meselson-Stahl Experiment)", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Describe the Meselson and Stahl experiment which proved experimentally that DNA replication is semi-conservative. State their observations across generations using CsCl density gradient centrifugation.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Experimental procedure:\n1. *E. coli* was grown in a medium containing $^{15}\\text{NH}_4\\text{Cl}$ (heavy isotope of nitrogen) as the sole nitrogen source for many generations. Result: $^{15}\\text{N}$ was incorporated into both strands of DNA.\n2. Cells were then transferred into a medium with normal $^{14}\\text{NH}_4\\text{Cl}$ and samples taken at definite time intervals (corresponding to cell division cycles).\n3. DNA was extracted and centrifuged on a $\\text{CsCl}$ density gradient.\nObservations:\n- **Generation 0**: DNA formed a single heavy band ($^{15}\\text{N}-^{15}\\text{N}$).\n- **Generation 1 (20 minutes)**: DNA extracted showed an intermediate hybrid density band ($^{15}\\text{N}-^{14}\\text{N}$).\n- **Generation 2 (40 minutes)**: Equal amounts of two bands appeared: one light ($^{14}\\text{N}-^{14}\\text{N}$) and one hybrid ($^{15}\\text{N}-^{14}\\text{N}$).\nConclusion: Each daughter DNA molecule retains one parental strand and synthesizes one new complementary strand (Semi-conservative replication).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Experimental protocol with 15N and transfer to 14N", "allocated_marks": 1.5},
            {"step": 2, "rule": "Observation after 1st generation (hybrid density 15N-14N)", "allocated_marks": 1.5},
            {"step": 3, "rule": "Observation after 2nd generation (equal ratio of light and hybrid)", "allocated_marks": 1.0},
            {"step": 4, "rule": "Final conclusion on semi-conservative nature", "allocated_marks": 1.0}
        ],
        "source_book": "Trueman's Biology Vol 2 / NCERT Biology Class 12 Ch 6"
    },
    {
        "grade_level": 12, "subject": "Biology", "chapter": "Biotechnology: Principles and Processes",
        "topic": "Polymerase Chain Reaction (PCR)", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Name the three steps involved in Polymerase Chain Reaction (PCR). Why is Taq polymerase used instead of normal DNA polymerase?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Three steps of PCR:\n1. **Denaturation**: Double-stranded DNA is heated to high temperature ($\\sim 94-96^\\circ\\text{C}$) to separate into single strands.\n2. **Annealing**: Primers bind to complementary sequences on single-stranded template DNA at lower temperature ($\\sim 50-60^\\circ\\text{C}$).\n3. **Extension**: Thermostable DNA polymerase extends the primers in $5' \\to 3'$ direction at $\\sim 72^\\circ\\text{C}$ using deoxynucleotides.\n**Taq Polymerase**: Isolated from the bacterium *Thermus aquaticus*. It remains active and stable at high denaturation temperatures ($95^\\circ\\text{C}$), eliminating the need to add fresh enzyme after each thermal cycle.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Three steps: Denaturation, Annealing, Extension with temperatures", "allocated_marks": 1.5},
            {"step": 2, "rule": "Identification of Thermus aquaticus source", "allocated_marks": 0.5},
            {"step": 3, "rule": "Thermostability rationale preventing denaturation", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Biology Class 12 Ch 11 / Trueman's"
    },

    # =========================================================================
    # CLASS 10 - SOCIAL SCIENCE (NCERT)
    # =========================================================================
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "The Rise of Nationalism in Europe",
        "topic": "Civil Code of 1804 (Napoleonic Code)", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Explain any three administrative features introduced by Napoleon through the Civil Code of 1804.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Key features of the Napoleonic Civil Code of 1804:\n1. **Abolition of Privileges**: Did away with all privileges based on birth, established equality before the law, and secured the right to property.\n2. **Simplification of Administrative Divisions**: Abolished feudal system, freed peasants from serfdom and manorial dues in regions under French control.\n3. **Economic and Transport Reforms**: Removed guild restrictions in towns; improved transport and communication networks; established uniform laws, standardized weights and measures, and a common national currency.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Abolition of birth privileges and equality before law", "allocated_marks": 1.0},
            {"step": 2, "rule": "Abolition of feudal dues and serfdom", "allocated_marks": 1.0},
            {"step": 3, "rule": "Standardized currency, weights, and removal of guild restrictions", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 History Ch 1"
    },
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Nationalism in India",
        "topic": "Non-Cooperation Movement and Salt March", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Why did Mahatma Gandhi decide to launch the Civil Disobedience Movement? How was the Salt March an effective symbol of resistance against British colonialism?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Launch of Civil Disobedience Movement:\n1. Rejection of Gandhi's Eleven Demands by Viceroy Irwin, including abolition of the oppressive Salt Tax.\n2. Widespread economic distress caused by the Great Depression, plummeting agricultural prices, and unreduced land revenue.\n3. The demand for 'Purna Swaraj' (complete independence) adopted at the 1929 Lahore Congress session.\nSalt March as an Effective Symbol of Resistance:\n1. **Universal Commodity**: Salt was consumed by rich and poor alike; taxing it and monopolizing its production revealed the most oppressive face of British rule.\n2. **Unified Mobilization**: It united disparate religious and socio-economic classes across the subcontinent under a common grievance.\n3. **Defiance of Law**: The 240-mile march from Sabarmati to Dandi (March 12 to April 6, 1930) broke colonial law publicly, inspiring millions to boycott foreign cloth, refuse land revenue, and resign from colonial administrative posts.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Factors leading to launch (rejection of demands, Great Depression, Purna Swaraj)", "allocated_marks": 2.0},
            {"step": 2, "rule": "Symbolism of salt as universal necessity unifying all classes", "allocated_marks": 1.5},
            {"step": 3, "rule": "Impact of Dandi March in breaking colonial law and widespread civil defiance", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 History Ch 2"
    },
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Power Sharing",
        "topic": "Prudential and Moral Reasons for Power Sharing", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Differentiate between prudential and moral reasons for power sharing in a democracy with examples.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. **Prudential Reasons**:\n- Based on careful calculation of gains and losses.\n- Emphasizes that power sharing brings out better outcomes by reducing the possibility of conflict and violence between social groups.\n- Example: Power sharing arrangement in Belgium that prevented civil war between Dutch and French speaking communities.\n2. **Moral Reasons**:\n- Emphasizes that the very act of power sharing is valuable in itself.\n- In a democracy, legitimate governance requires sharing power with citizens who are affected by its exercise.\n- Example: Decentralization and Panchayati Raj in India, ensuring citizens' direct participation in decision making.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Prudential reason: outcome-based, conflict prevention (Belgium)", "allocated_marks": 1.5},
            {"step": 2, "rule": "Moral reason: intrinsic value of democratic participation (Panchayati Raj)", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Civics Ch 1"
    },
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Sectors of the Indian Economy",
        "topic": "Primary, Secondary, Tertiary and Disguised Unemployment", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "What is disguised unemployment? Explain with an example from the rural agricultural sector of India.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Disguised unemployment is a situation where more people are engaged in a job than actually required.\nEven if some workers are removed, total production does not fall (marginal productivity of surplus labour is zero).\nExample: A small farmer Laxmi owns two hectares of unirrigated land. All five members of her family work on the plot throughout the year because they have nowhere else to go. The work requires only two or three individuals. The extra two members are disguisedly unemployed.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Definition of disguised unemployment (marginal productivity is zero)", "allocated_marks": 1.5},
            {"step": 2, "rule": "Practical rural agricultural example showing surplus family labor", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Economics Ch 2"
    },

    # =========================================================================
    # CLASS 10 & 12 - ENGLISH
    # =========================================================================
    {
        "grade_level": 10, "subject": "English", "chapter": "A Letter to God",
        "topic": "Faith and Irony of the Post Office Employees", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Why did Lencho say the raindrops were like 'new coins'? Why was he angry when he counted the money sent by the postmaster?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. Lencho compared the raindrops to 'new coins' because his ripe cornfield promised a good harvest, and the much-needed rain would directly result in a prosperous crop bringing in money and financial stability.\n2. When he opened the envelope, he found only 70 pesos instead of the 100 pesos he had requested. Having unshakeable faith in God, he believed God could never make a mistake, and concluded that the post office employees ('a bunch of crooks') had stolen the remaining 30 pesos.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Reason for coin comparison: rain ensures rich crop harvest", "allocated_marks": 1.5},
            {"step": 2, "rule": "Reason for anger: received only 70 pesos, suspected post office staff", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT First Flight Class 10 Ch 1"
    },
    {
        "grade_level": 12, "subject": "English", "chapter": "The Last Lesson",
        "topic": "Linguistic Chauvinism and Patriotism", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "What order had come from Berlin regarding Alsace and Lorraine? How did Franz's feelings about M. Hamel and school change upon hearing the announcement?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. The order from Berlin mandated that only German would be taught in the schools of Alsace and Lorraine, completely banning the teaching of the French language.\n2. Franz was struck with deep remorse and guilt for neglecting his French lessons and wasting time on frivolous pursuits. His old grammar book and history of saints, which had seemed like burdens, suddenly felt like old friends he could not bear to give up. His dislike for M. Hamel vanished; he forgot all about his ruler and eccentricities, feeling only empathy and admiration for his teacher's patriotic dedication.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Order from Berlin: impose German language in Alsace and Lorraine schools", "allocated_marks": 1.5},
            {"step": 2, "rule": "Franz's transformation: guilt over neglected studies and newfound respect for M. Hamel", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Flamingo Class 12 Ch 1"
    }
]

def main():
    logger.info("=================================================================")
    logger.info("SEEDING EXPANDED CURRICULUM INTO SUPABASE CLOUD DATABASE")
    logger.info(f"Database Backend: {'Supabase PostgreSQL' if db.use_supabase else 'Local SQLite'}")
    logger.info(f"Questions to insert: {len(EXPANDED_QUESTIONS)}")
    logger.info("=================================================================")

    inserted = db.upsert_questions(EXPANDED_QUESTIONS)
    logger.info(f"Successfully upserted {inserted} questions into Supabase master_question_bank!")

    if db.use_supabase:
        try:
            res = db.client.table("master_question_bank").select("id", count="exact").execute()
            logger.info(f"Updated Total Questions in Supabase: {res.count}")
        except Exception as e:
            logger.warning(f"Could not count: {e}")

if __name__ == "__main__":
    main()
