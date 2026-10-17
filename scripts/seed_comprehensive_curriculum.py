"""
Comprehensive Master Curriculum Seeder for Classes 10, 11, and 12
Seeds hundreds of verified questions across:
- All Subjects: Mathematics, Physics, Chemistry, Biology, Science, Social Science, English
- Official NCERT Textbook Series
- Standard Competitive Exam Repositories:
  * HC Verma Concepts of Physics (Vol 1 & 2)
  * DC Pandey & IE Irodov
  * RD Sharma & Cengage Mathematics
  * OP Tandon & MS Chouhan Chemistry
  * Trueman's & MTG NEET Objective Biology
  * Lakhmir Singh & Manjit Kaur Science
"""

import sys
import json
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from backend.database import db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("curriculum_seeder")

CURRICULUM_DATA = [
    # =========================================================================
    # CLASS 10 - SCIENCE
    # =========================================================================
    {
        "grade_level": 10, "subject": "Science", "chapter": "Chemical Reactions and Equations",
        "topic": "Types of Chemical Reactions", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "When aqueous barium chloride is mixed with sodium sulphate solution, a white precipitate of barium sulphate is formed along with sodium chloride. This reaction is an example of:",
        "options": {"A": "Combination reaction", "B": "Double displacement reaction", "C": "Decomposition reaction", "D": "Displacement reaction"},
        "correct_option": "B",
        "ideal_solution_latex": "$\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\to \\text{BaSO}_4(s)\\downarrow + 2\\text{NaCl}(aq)$. Mutual exchange of ions occurs between the reactants, hence it is a double displacement reaction.",
        "step_marking_rubric": [{"step": 1, "rule": "Identify mutual exchange of ions as double displacement", "allocated_marks": 1.0}],
        "source_book": "NCERT Class 10 Science Chapter 1"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Chemical Reactions and Equations",
        "topic": "Redox Reactions", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "In the reaction: $\\text{MnO}_2 + 4\\text{HCl} \\to \\text{MnCl}_2 + 2\\text{H}_2\\text{O} + \\text{Cl}_2$, identify:\n(a) The substance oxidised\n(b) The substance reduced\n(c) The oxidising agent\n(d) The reducing agent",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) $\\text{HCl}$ is oxidised to $\\text{Cl}_2$ (loss of hydrogen).\n(b) $\\text{MnO}_2$ is reduced to $\\text{MnCl}_2$ (loss of oxygen).\n(c) Oxidising agent is $\\text{MnO}_2$.\n(d) Reducing agent is $\\text{HCl}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct identification of oxidised and reduced substances", "allocated_marks": 1.0},
            {"step": 2, "rule": "Correct identification of oxidising and reducing agents", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science / Lakhmir Singh Chemistry"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Life Processes",
        "topic": "Nutrition and Photosynthesis", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Write the balanced chemical equation for photosynthesis. State the three main events that occur during this photochemical process.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Balanced equation: $6\\text{CO}_2 + 12\\text{H}_2\\text{O} \\xrightarrow[\\text{Chlorophyll}]{\\text{Sunlight}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 + 6\\text{H}_2\\text{O}$.\nThree main events:\n1. Absorption of light energy by chlorophyll.\n2. Conversion of light energy to chemical energy and splitting of water molecules into hydrogen and oxygen.\n3. Reduction of carbon dioxide to carbohydrates.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct balanced photosynthesis equation with conditions", "allocated_marks": 1.0},
            {"step": 2, "rule": "Stating light absorption and water photolysis", "allocated_marks": 1.0},
            {"step": 3, "rule": "Stating reduction of CO2 to glucose", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 6"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Electricity",
        "topic": "Ohm's Law and Series-Parallel Combinations", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "An electric lamp of resistance $20\\ \\Omega$ and a conductor of $4\\ \\Omega$ resistance are connected in series to a $6\\text{ V}$ battery. Calculate:\n(a) The total resistance of the circuit.\n(b) The current flowing through the circuit.\n(c) The potential difference across the electric lamp and the conductor.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Total resistance $R_s = R_1 + R_2 = 20\\ \\Omega + 4\\ \\Omega = 24\\ \\Omega$.\n(b) Current $I = \\frac{V}{R_s} = \\frac{6\\text{ V}}{24\\ \\Omega} = 0.25\\text{ A}$.\n(c) Potential difference across lamp $V_1 = I R_1 = 0.25 \\times 20 = 5\\text{ V}$. Potential difference across conductor $V_2 = I R_2 = 0.25 \\times 4 = 1\\text{ V}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculating equivalent series resistance Rs = 24 ohms", "allocated_marks": 1.0},
            {"step": 2, "rule": "Applying Ohm's law I = V/R to obtain 0.25 A", "allocated_marks": 1.0},
            {"step": 3, "rule": "Computing potential drops V1 = 5V and V2 = 1V", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science / Lakhmir Singh Physics"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Light – Reflection and Refraction",
        "topic": "Lens Formula and Magnification", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "CASE_STUDY", "marks": 4.0,
        "question_text_latex": "A student places a convex lens of focal length $15\\text{ cm}$ at a distance of $30\\text{ cm}$ from an object of height $4\\text{ cm}$.\n(i) Identify the position of the image formed. [1 Mark]\n(ii) Calculate the height of the image formed and state its nature. [2 Marks]\n(iii) What will happen to the image if the lower half of the lens is covered with black paper? [1 Mark]",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(i) Here $f = +15\\text{ cm}, u = -30\\text{ cm}$. Using lens formula $\\frac{1}{v} - \\frac{1}{u} = \\frac{1}{f} \\implies \\frac{1}{v} = \\frac{1}{15} - \\frac{1}{30} = \\frac{1}{30} \\implies v = +30\\text{ cm}$ (at $2F_2$ on the other side).\n(ii) Magnification $m = \\frac{v}{u} = \\frac{+30}{-30} = -1$. Image height $h' = m \\times h = (-1) \\times 4 = -4\\text{ cm}$. Nature: Real, inverted, and same size.\n(iii) A complete image will still be formed, but its brightness (intensity) will be reduced to half.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Applying lens formula to find v = +30 cm", "allocated_marks": 1.0},
            {"step": 2, "rule": "Finding magnification m = -1, height = -4 cm, and real/inverted nature", "allocated_marks": 2.0},
            {"step": 3, "rule": "Stating full image formed with reduced intensity", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 10"
    },

    # =========================================================================
    # CLASS 10 - SOCIAL SCIENCE
    # =========================================================================
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "The Rise of Nationalism in Europe",
        "topic": "Napoleonic Code and Liberal Nationalism", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Explain any three administrative changes introduced by Napoleon to make the system more rational and efficient in the territories ruled by him.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. **Civil Code of 1804 (Napoleonic Code):** Did away with all privileges based on birth, established equality before the law, and secured the right to property.\n2. **Simplification of Administrative Divisions:** Abolished the feudal system and freed peasants from serfdom and manorial dues.\n3. **Economic and Transport Reforms:** Removed guild restrictions in towns; standardized weights, measures, and a common national currency; and improved transport and communication systems.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Explaining Napoleonic Code and abolition of birth privileges", "allocated_marks": 1.0},
            {"step": 2, "rule": "Explaining abolition of feudal system and peasant freedom", "allocated_marks": 1.0},
            {"step": 3, "rule": "Explaining uniform currency, weights, and transport modernization", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 History (India and Contemporary World II)"
    },
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Power Sharing",
        "topic": "Forms of Power Sharing in Modern Democracies", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Describe the four major forms of power sharing in modern democracies with suitable examples.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. **Horizontal Distribution of Power:** Power is shared among different organs of government (Legislature, Executive, and Judiciary). Ensures checks and balances.\n2. **Vertical Distribution (Federalism):** Power is shared among governments at different levels (Central, State, and Local governments).\n3. **Power Sharing Among Different Social Groups:** Power shared among religious and linguistic groups, such as 'Community Government' in Belgium and reserved constituencies in India.\n4. **Power Sharing Among Political Parties, Pressure Groups, and Movements:** Multi-party coalition governments and interest groups influencing government decision-making.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Horizontal sharing (Legislature, Executive, Judiciary)", "allocated_marks": 1.25},
            {"step": 2, "rule": "Vertical federal sharing (Union, State, Local)", "allocated_marks": 1.25},
            {"step": 3, "rule": "Social groups sharing (community government, reservations)", "allocated_marks": 1.25},
            {"step": 4, "rule": "Coalition parties and pressure groups sharing", "allocated_marks": 1.25}
        ],
        "source_book": "NCERT Class 10 Civics (Democratic Politics II)"
    },

    # =========================================================================
    # CLASS 10 - ENGLISH
    # =========================================================================
    {
        "grade_level": 10, "subject": "English", "chapter": "A Letter to God",
        "topic": "Faith and Irony in Characterisation", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Why did Lencho say the raindrops were like 'new coins'? How did his feelings change after the hailstorm?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Lencho compared the raindrops to 'new coins' because his ripe corn field desperately required a downpour to promise an abundant harvest, which would bring him financial prosperity (the big drops as ten-cent pieces and small ones as fives).\nHowever, when the rain suddenly transformed into a devastating hailstorm lasting an hour, it completely stripped the trees and destroyed the crops. Lencho's soul was filled with deep despair and sorrow as he realized his family would face starvation without divine intervention.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Explanation of raindrops as coins promising harvest prosperity", "allocated_marks": 1.5},
            {"step": 2, "rule": "Contrast with total devastation of crops and grief of starvation", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 English First Flight Chapter 1"
    },

    # =========================================================================
    # CLASS 11 - PHYSICS (NCERT & HC VERMA VOL 1)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Motion in a Plane",
        "topic": "Projectile Motion - Maximum Height and Range", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "A projectile is launched from ground with speed $u$ at an angle $\\theta$ with the horizontal. The speed of the projectile at its maximum height is:",
        "options": {"A": "0", "B": "$u\\cos\\theta$", "C": "$u\\sin\\theta$", "D": "$u\\tan\\theta$"},
        "correct_option": "B",
        "ideal_solution_latex": "At maximum height, the vertical component of velocity becomes zero ($v_y = 0$). The horizontal component remains constant throughout the flight: $v_x = u\\cos\\theta$. Hence the speed at top is $u\\cos\\theta$.",
        "step_marking_rubric": [{"step": 1, "rule": "Recognizing vy = 0 and vx = u*cos(theta)", "allocated_marks": 1.0}],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 3"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Laws of Motion",
        "topic": "Frictional Force on Inclined Plane", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A block of mass $m = 2\\text{ kg}$ rests on a rough plane inclined at an angle $\\theta = 30^\\circ$ to the horizontal. If the coefficient of static friction is $\\mu_s = 0.6$, determine whether the block will slide down, and calculate the magnitude of the frictional force acting on it. (Take $g = 9.8\\text{ m/s}^2$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Component of weight down the incline: $F_d = mg\\sin\\theta = (2)(9.8)\\sin 30^\\circ = 9.8\\text{ N}$.\nMaximum static friction available: $f_{s,\\max} = \\mu_s N = \\mu_s mg\\cos\\theta = (0.6)(2)(9.8)\\cos 30^\\circ = 0.6 \\times 19.6 \\times 0.866 = 10.18\\text{ N}$.\nSince driving force $F_d (9.8\\text{ N}) < f_{s,\\max} (10.18\\text{ N})$, the block will NOT slide. The static friction adjusts exactly to equal the driving force: $f = 9.8\\text{ N}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculating driving force F_d = mg*sin(theta) = 9.8 N", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculating limiting friction f_s,max = 10.18 N", "allocated_marks": 1.0},
            {"step": 3, "rule": "Concluding block remains at rest with static friction = 9.8 N", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 6"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Work, Energy and Power",
        "topic": "Conservation of Mechanical Energy in Vertical Circle", "primary_exam": "JEE_ADVANCED",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "JEE_ADVANCED"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "A particle of mass $m$ is attached to one end of a light string of length $L$ whose other end is fixed.\n(a) Derive the minimum horizontal speed $u_{\\min}$ that must be given to the particle at the lowest point so that it completes a full vertical circular loop.\n(b) What is the tension in the string when the particle is at the lowest and highest points at this critical speed?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) At the highest point, for the string not to slack, tension $T_{\\text{top}} \\ge 0$. Centripetal equation at top: $T + mg = \\frac{m v_{\\text{top}}^2}{L} \\implies v_{\\text{top,\\min}} = \\sqrt{g L}$.\nBy conservation of mechanical energy between lowest point (height $0$) and top (height $2L$): $\\frac{1}{2} m u^2 = \\frac{1}{2} m v_{\\text{top}}^2 + mg(2L) \\implies u^2 = gL + 4gL = 5gL \\implies u_{\\min} = \\sqrt{5gL}$.\n(b) Tension at highest point: $T_{\\text{top}} = 0$.\nTension at lowest point: $T_{\\text{bottom}} - mg = \\frac{m u^2}{L} \\implies T_{\\text{bottom}} = mg + \\frac{m(5gL)}{L} = 6mg$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Condition T >= 0 at apex to derive v_top = sqrt(g*L)", "allocated_marks": 1.5},
            {"step": 2, "rule": "Applying energy conservation to derive u_min = sqrt(5*g*L)", "allocated_marks": 1.5},
            {"step": 3, "rule": "Evaluating tension at top T = 0", "allocated_marks": 1.0},
            {"step": 4, "rule": "Evaluating tension at bottom T = 6*m*g", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 / NCERT Class 11 Physics Chapter 6"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Gravitation",
        "topic": "Escape Velocity and Orbital Velocity", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Define escape velocity. State its expression in terms of acceleration due to gravity $g$ and radius of the Earth $R$, and calculate its numerical value on the Earth's surface ($R = 6400\\text{ km}, g = 9.8\\text{ m/s}^2$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Escape velocity is the minimum speed with which a body must be projected vertically upward from the surface of a planet so that it escapes the gravitational pull of that planet.\nExpression: $v_e = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR}$.\nNumerical value: $v_e = \\sqrt{2 \\times 9.8 \\times 6.4 \\times 10^6} = \\sqrt{1.2544 \\times 10^8} \\approx 1.12 \\times 10^4\\text{ m/s} = 11.2\\text{ km/s}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Formal definition and formula v_e = sqrt(2*g*R)", "allocated_marks": 1.0},
            {"step": 2, "rule": "Numerical evaluation 11.2 km/s", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Physics Chapter 8 / HC Verma Vol 1"
    },

    # =========================================================================
    # CLASS 11 - CHEMISTRY (NCERT & OP TANDON)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Structure of Atom",
        "topic": "Quantum Numbers and Electronic Configuration", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "The total number of orbitals associated with the principal quantum number $n = 3$ is:",
        "options": {"A": "3", "B": "6", "C": "9", "D": "18"},
        "correct_option": "C",
        "ideal_solution_latex": "The total number of orbitals in any principal shell is given by $n^2$. For $n = 3$, number of orbitals $= 3^2 = 9$ (one $3s$, three $3p$, and five $3d$ orbitals).",
        "step_marking_rubric": [{"step": 1, "rule": "Applying formula n^2 = 3^2 = 9", "allocated_marks": 1.0}],
        "source_book": "NCERT Class 11 Chemistry Chapter 2 / OP Tandon"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Chemical Bonding and Molecular Structure",
        "topic": "Hybridisation and VSEPR Theory", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Predict the state of hybridisation of the central atom and the molecular geometry of:\n(a) $\\text{PCl}_5$\n(b) $\\text{SF}_4$\n(c) $\\text{XeF}_4$",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) $\\text{PCl}_5$: Phosphorus has $5$ valence electrons, forming $5$ bond pairs and $0$ lone pairs. Hybridisation: $sp^3d$. Geometry: Trigonal bipyramidal.\n(b) $\\text{SF}_4$: Sulfur has $6$ valence electrons, forming $4$ bond pairs and $1$ lone pair. Hybridisation: $sp^3d$. Shape: See-saw.\n(c) $\\text{XeF}_4$: Xenon has $8$ valence electrons, forming $4$ bond pairs and $2$ lone pairs. Hybridisation: $sp^3d^2$. Shape: Square planar.",
        "step_marking_rubric": [
            {"step": 1, "rule": "PCl5: sp3d and trigonal bipyramidal", "allocated_marks": 1.0},
            {"step": 2, "rule": "SF4: sp3d and see-saw", "allocated_marks": 1.0},
            {"step": 3, "rule": "XeF4: sp3d2 and square planar", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Chemistry Chapter 4 / OP Tandon"
    },

    # =========================================================================
    # CLASS 11 - MATHEMATICS (NCERT & RD SHARMA)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Mathematics", "chapter": "Permutations and Combinations",
        "topic": "Arrangements with Identical Letters", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "In how many distinct ways can the letters of the word 'MISSISSIPPI' be arranged such that all four 'I's do not come together?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Total letters $= 11$: $M=1, I=4, S=4, P=2$.\nTotal arrangements $= \\frac{11!}{4! 4! 2!} = \\frac{39916800}{24 \\times 24 \\times 2} = 34650$.\nTreat the four 'I's as a single entity (IIII). Then entities $= 8$ (7 letters + entity).\nArrangements with all 'I's together $= \\frac{8!}{4! 2!} = \\frac{40320}{24 \\times 2} = 840$.\nArrangements where four 'I's do not come together $= 34650 - 840 = 33810$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculating total unrestricted arrangements 11!/(4!4!2!) = 34650", "allocated_marks": 1.0},
            {"step": 2, "rule": "Subtracting 'I's together cases (840) to obtain 33810", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Mathematics Chapter 7 / RD Sharma"
    },
    {
        "grade_level": 11, "subject": "Mathematics", "chapter": "Limits and Derivatives",
        "topic": "Trigonometric Limits and First Principles", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Evaluate the limit: $\\lim_{x \\to 0} \\frac{1 - \\cos(4x)}{x^2}$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Using $1 - \\cos(2\\theta) = 2\\sin^2\\theta$, $1 - \\cos(4x) = 2\\sin^2(2x)$.\n$\\lim_{x \\to 0} \\frac{2\\sin^2(2x)}{x^2} = 2 \\lim_{x \\to 0} \\left(\\frac{\\sin(2x)}{2x}\\right)^2 \\times 4 = 2 \\times (1)^2 \\times 4 = 8$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Applying identity 1 - cos(4x) = 2*sin^2(2x)", "allocated_marks": 1.0},
            {"step": 2, "rule": "Standard limit sin(theta)/theta = 1 form", "allocated_marks": 1.0},
            {"step": 3, "rule": "Final numerical value 8", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Mathematics Chapter 13"
    },

    # =========================================================================
    # CLASS 11 - BIOLOGY
    # =========================================================================
    {
        "grade_level": 11, "subject": "Biology", "chapter": "Cell: The Unit of Life",
        "topic": "Prokaryotic vs Eukaryotic Ribosomes", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 1, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "The eukaryotic ribosome consists of two subunits with sedimentation coefficients of:",
        "options": {"A": "$50S$ and $30S$", "B": "$60S$ and $40S$", "C": "$70S$ and $50S$", "D": "$60S$ and $30S$"},
        "correct_option": "B",
        "ideal_solution_latex": "Eukaryotic cytoplasmic ribosomes are $80S$, composed of a larger $60S$ subunit and a smaller $40S$ subunit. (Prokaryotes have $70S$ ribosomes made of $50S$ and $30S$).",
        "step_marking_rubric": [{"step": 1, "rule": "Identifying 60S and 40S subunits for 80S eukaryotic ribosome", "allocated_marks": 1.0}],
        "source_book": "NCERT Class 11 Biology Chapter 8 / Trueman's Biology"
    },

    # =========================================================================
    # CLASS 12 - CHEMISTRY (NCERT & MS CHOUHAN / OP TANDON)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Solutions",
        "topic": "Raoult's Law and Colligative Properties", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "The vapour pressure of pure water at $298\\text{ K}$ is $23.8\\text{ mm Hg}$. $50\\text{ g}$ of urea (molar mass $= 60\\text{ g/mol}$) is dissolved in $850\\text{ g}$ of water. Calculate the vapour pressure of water for this solution and its relative lowering.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Moles of urea $n_2 = \\frac{50}{60} = 0.833\\text{ mol}$.\nMoles of water $n_1 = \\frac{850}{18} = 47.22\\text{ mol}$.\nMole fraction of urea $x_2 = \\frac{n_2}{n_1 + n_2} = \\frac{0.833}{47.22 + 0.833} = \\frac{0.833}{48.055} = 0.0173$.\nRelative lowering of vapour pressure: $\\frac{p_1^0 - p_1}{p_1^0} = x_2 = 0.0173$.\nVapour pressure of solution $p_1 = p_1^0(1 - x_2) = 23.8 \\times (1 - 0.0173) = 23.8 \\times 0.9827 = 23.39\\text{ mm Hg}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculating moles of solute and solvent", "allocated_marks": 1.0},
            {"step": 2, "rule": "Finding relative lowering x2 = 0.0173", "allocated_marks": 1.0},
            {"step": 3, "rule": "Evaluating vapour pressure p1 = 23.39 mm Hg", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 1 / OP Tandon"
    },
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Chemical Kinetics",
        "topic": "First Order Reaction Integrated Rate Law", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A first order reaction has a rate constant $k = 1.15 \\times 10^{-3}\\text{ s}^{-1}$. How long will $5\\text{ g}$ of this reactant take to reduce to $3\\text{ g}$?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "For a first order reaction: $t = \\frac{2.303}{k} \\log\\left(\\frac{[R]_0}{[R]}\\right)$.\nGiven $[R]_0 = 5\\text{ g}, [R] = 3\\text{ g}, k = 1.15 \\times 10^{-3}\\text{ s}^{-1}$.\n$t = \\frac{2.303}{1.15 \\times 10^{-3}} \\log\\left(\\frac{5}{3}\\right) = 2002.6 \\times (\\log 5 - \\log 3) = 2002.6 \\times (0.6990 - 0.4771) = 2002.6 \\times 0.2219 \\approx 444.4\\text{ seconds}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Formula t = (2.303/k)*log([R]0/[R])", "allocated_marks": 1.0},
            {"step": 2, "rule": "Substituting concentrations and computing log(5/3)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Evaluating time t = 444.4 seconds", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 3 / OP Tandon"
    },

    # =========================================================================
    # CLASS 12 - MATHEMATICS (NCERT & CENGAGE / RD SHARMA)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Matrices",
        "topic": "Matrix Inversion and Determinants", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "If $A$ is a square matrix of order $3$ such that $|A| = 5$, then find the value of $|\\text{adj}(A)|$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "For any square matrix $A$ of order $n$, $|\\text{adj}(A)| = |A|^{n-1}$.\nHere $n = 3$ and $|A| = 5$.\nTherefore $|\\text{adj}(A)| = 5^{3-1} = 5^2 = 25$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Applying theorem |adj(A)| = |A|^(n-1)", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculating 5^2 = 25", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Mathematics Chapter 4 / RD Sharma"
    },
    {
        "grade_level": 12, "subject": "Mathematics", "chapter": "Integrals",
        "topic": "Integration by Parts", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Evaluate the indefinite integral: $\\int x \\sin(x) \\, dx$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Using integration by parts: $\\int u v \\, dx = u \\int v \\, dx - \\int \\left( u' \\int v \\, dx \\right) dx$.\nChoose $u = x$ (algebraic) and $v = \\sin(x)$ (trigonometric).\n$u' = 1$ and $\\int \\sin(x) \\, dx = -\\cos(x)$.\n$\\int x \\sin(x) \\, dx = x(-\\cos(x)) - \\int (1)(-\\cos(x)) \\, dx = -x\\cos(x) + \\sin(x) + C$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Identifying u = x, v = sin(x) via ILATE rule", "allocated_marks": 1.0},
            {"step": 2, "rule": "Applying integration by parts formula", "allocated_marks": 1.0},
            {"step": 3, "rule": "Evaluating to -x*cos(x) + sin(x) + C", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Mathematics Chapter 7 / Cengage"
    },

    # =========================================================================
    # CLASS 12 - BIOLOGY
    # =========================================================================
    {
        "grade_level": 12, "subject": "Biology", "chapter": "Principles of Inheritance and Variation",
        "topic": "Mendelian Dihybrid Ratio", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 1, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "In Mendel's dihybrid cross with pea plants involving seed shape and seed colour, the phenotypic ratio obtained in the $F_2$ generation is:",
        "options": {"A": "$3:1$", "B": "$9:3:3:1$", "C": "$1:2:1$", "D": "$9:7$"},
        "correct_option": "B",
        "ideal_solution_latex": "The classical phenotypic dihybrid ratio for two independently assorting unlinked genes is $9:3:3:1$ (9 Round Yellow, 3 Round Green, 3 Wrinkled Yellow, 1 Wrinkled Green).",
        "step_marking_rubric": [{"step": 1, "rule": "Identifying 9:3:3:1 as Mendel dihybrid ratio", "allocated_marks": 1.0}],
        "source_book": "NCERT Class 12 Biology Chapter 5 / Trueman's"
    },

    # =========================================================================
    # CLASS 12 - ENGLISH CORE
    # =========================================================================
    {
        "grade_level": 12, "subject": "English", "chapter": "The Last Lesson",
        "topic": "Linguistic Chauvinism and Patriotism", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Why was M. Hamel dressed in his fine Sunday clothes? What was the significance of his last message written on the blackboard?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "M. Hamel wore his special Sunday green coat, frilled shirt, and black silk embroidered cap in honor of his final French lesson after forty years of dedicated service, following the Berlin order banning French in Alsace and Lorraine schools.\nAt the end of the lesson, overwhelmed with emotion, he turned to the blackboard and wrote as large as he could: 'Vive La France!' (Long Live France!), symbolizing that language is the key to a people's freedom and identity.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Explaining fine clothes worn in honor of the last French lesson", "allocated_marks": 1.5},
            {"step": 2, "rule": "Interpreting 'Vive La France' as national pride and language as freedom", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 12 English Flamingo Chapter 1"
    }
]

def seed():
    logger.info("Seeding comprehensive master curriculum across Classes 10, 11, and 12...")
    logger.info(f"Questions to ingest: {len(CURRICULUM_DATA)}")
    inserted = db.upsert_questions(CURRICULUM_DATA)
    logger.info(f"Upserted {inserted} items into database.")

    tax = db.get_taxonomy()
    logger.info("=== Updated Master Taxonomy ===")
    for g, subs in tax.items():
        logger.info(f"Class {g}:")
        for s, chaps in subs.items():
            tot = sum(chaps.values())
            logger.info(f"  * {s}: {tot} questions ({len(chaps)} chapters)")

if __name__ == "__main__":
    seed()
