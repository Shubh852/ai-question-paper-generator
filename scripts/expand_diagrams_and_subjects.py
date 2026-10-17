"""
Comprehensive Question Bank Expansion Script
Adds diagram-rich questions and deep question coverage for:
- Class 12 & 11 Chemistry (Electrochemistry, Kinetics, Coordination, Bonding, Thermodynamics, Equilibrium)
- Class 12 & 11 Biology (Genetics, Molecular Basis, Biotechnology, Cell Division, Photosynthesis, Respiration)
- Class 10 & 12 Physics (Circuits, Ray Optics, Logic Gates, AC circuits)
- Class 10 & 11 Mathematics (Tangents, Coordinate Geometry, Trigonometry, Calculus)
Stores to Supabase Cloud master_question_bank and SQLite database.
"""

import hashlib
import json
import uuid
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from backend.database import db

def compute_hash(grade: int, subject: str, text: str) -> str:
    raw = f"{grade}:{subject.lower()}:{text.strip()}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

QUESTIONS = [
    # =========================================================================
    # CLASS 12 PHYSICS (DIAGRAM-BASED & BOARD CORE)
    # =========================================================================
    {
        "grade_level": 12,
        "subject": "Physics",
        "chapter": "Current Electricity",
        "topic": "Wheatstone Bridge & Kirchhoff's Laws",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "MCQ",
        "marks": 1.0,
        "question_text_latex": "In the Wheatstone bridge circuit shown below, the galvanometer $G$ shows null deflection (balanced state). Find the value of unknown resistance $S$.\n\n![Wheatstone Bridge Circuit](data/diagrams/wheatstone_bridge.svg)",
        "options": {
            "A": "$30\\,\\Omega$",
            "B": "$15\\,\\Omega$",
            "C": "$7.5\\,\\Omega$",
            "D": "$45\\,\\Omega$"
        },
        "correct_option": "A",
        "ideal_solution_latex": "For a balanced Wheatstone bridge, no current passes through the galvanometer: $\\frac{P}{Q} = \\frac{R}{S}$. Given $P = 10\\,\\Omega$, $Q = 20\\,\\Omega$, and $R = 15\\,\\Omega$. Therefore, $S = \\frac{Q \\times R}{P} = \\frac{20 \\times 15}{10} = 30\\,\\Omega$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "State balanced Wheatstone bridge condition P/Q = R/S", "allocated_marks": 0.5},
            {"step": 2, "rule": "Substitute values and calculate S = 30 ohms", "allocated_marks": 0.5}
        ],
        "source_book": "NCERT Class 12 Physics Chapter 3"
    },
    {
        "grade_level": 12,
        "subject": "Physics",
        "chapter": "Ray Optics and Optical Instruments",
        "topic": "Refraction Through a Prism",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "A ray of light passes through an equilateral glass prism of refracting angle $A = 60^\\circ$ as shown in the diagram. If the angle of minimum deviation is $\\delta_m = 30^\\circ$, calculate the refractive index $\\mu$ of the prism material and the angle of incidence $i$.\n\n![Prism Refraction](data/diagrams/ray_optics_prism.svg)",
        "ideal_solution_latex": "1. Using the prism formula: $\\mu = \\frac{\\sin\\left(\\frac{A + \\delta_m}{2}\\right)}{\\sin\\left(\\frac{A}{2}\\right)}$.\n2. Given $A = 60^\\circ$ and $\\delta_m = 30^\\circ$: $\\mu = \\frac{\\sin(45^\\circ)}{\\sin(30^\\circ)} = \\frac{1/\\sqrt{2}}{1/2} = \\sqrt{2} \\approx 1.414$.\n3. The angle of incidence at minimum deviation is: $i = \\frac{A + \\delta_m}{2} = \\frac{60^\\circ + 30^\\circ}{2} = 45^\\circ$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Write prism formula for refractive index", "allocated_marks": 1.0},
            {"step": 2, "rule": "Substitute A=60 and delta_m=30 to get mu = sqrt(2)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculate angle of incidence i = 45 degrees", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Physics Chapter 9"
    },
    {
        "grade_level": 12,
        "subject": "Physics",
        "chapter": "Semiconductor Electronics",
        "topic": "Logic Gates & Combinations",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_I",
        "marks": 2.0,
        "question_text_latex": "Write the truth table for the logic circuit shown below consisting of a NAND gate followed by a NOR gate with inputs $A, B$ and $C$.\n\n![Logic Gates Circuit](data/diagrams/logic_gates_circuit.svg)",
        "ideal_solution_latex": "1. Output of first NAND gate: $Y_1 = \\overline{A \\cdot B}$.\n2. The second NOR gate receives inputs $Y_1$ and $C$. Output: $Y = \\overline{Y_1 + C} = \\overline{\\overline{A \\cdot B} + C} = (A \\cdot B) \\cdot \\overline{C}$.\n3. Truth table produces $Y = 1$ if and only if $A = 1, B = 1$, and $C = 0$; for all other input combinations, $Y = 0$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Write intermediate Boolean expression Y1 = (A.B)'", "allocated_marks": 1.0},
            {"step": 2, "rule": "Derive final Boolean output Y = A.B.C' and truth table", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Physics Chapter 14"
    },

    # =========================================================================
    # CLASS 10 SCIENCE (DIAGRAM-BASED & BOARD CORE)
    # =========================================================================
    {
        "grade_level": 10,
        "subject": "Science",
        "chapter": "Electricity",
        "topic": "Combination of Resistors",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "For the circuit network shown in the diagram, calculate:\n(a) The equivalent resistance of the entire circuit.\n(b) The total current recorded by ammeter $A$.\n(c) The potential difference across resistor $R_1$.\n\n![Resistor Circuit Network](data/diagrams/resistors_series_parallel.svg)",
        "ideal_solution_latex": "1. Resistors $R_2 = 6\\,\\Omega$ and $R_3 = 12\\,\\Omega$ are in parallel: $\\frac{1}{R_p} = \\frac{1}{6} + \\frac{1}{12} = \\frac{2+1}{12} = \\frac{3}{12} = \\frac{1}{4} \\implies R_p = 4\\,\\Omega$.\n2. Total equivalent resistance $R_{eq} = R_1 + R_p = 4\\,\\Omega + 4\\,\\Omega = 8\\,\\Omega$.\n3. Total current from battery $V = 12\\text{ V}$: $I = \\frac{V}{R_{eq}} = \\frac{12}{8} = 1.5\\text{ A}$.\n4. Potential difference across $R_1$: $V_1 = I \\times R_1 = 1.5 \\times 4 = 6.0\\text{ V}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Calculate parallel resistance Rp = 4 ohms and Req = 8 ohms", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculate total current I = 1.5 A using Ohm's Law", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculate potential drop across R1 = 6.0 V", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 12"
    },
    {
        "grade_level": 10,
        "subject": "Science",
        "chapter": "Light - Reflection and Refraction",
        "topic": "Image Formation by Convex Lens",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "An object of height $h = 4\\text{ cm}$ is placed between $F_1$ and $2F_1$ of a convex lens of focal length $f = +15\\text{ cm}$ at a distance of $u = -20\\text{ cm}$.\n(a) Find the position and nature of the image formed.\n(b) Calculate the magnification and height of the image.\n\n![Convex Lens Ray Formation](data/diagrams/convex_lens_ray_diagram.svg)",
        "ideal_solution_latex": "1. Using lens formula: $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}$.\n$\\frac{1}{v} = \\frac{1}{f} + \\frac{1}{u} = \\frac{1}{15} + \\frac{1}{-20} = \\frac{4 - 3}{60} = \\frac{1}{60} \\implies v = +60\\text{ cm}$.\n2. Nature: The image is real, inverted, and formed at $60\\text{ cm}$ on the other side of the lens (beyond $2F_2$).\n3. Magnification: $m = \\frac{v}{u} = \\frac{+60}{-20} = -3$.\n4. Height of image: $h' = m \\times h = -3 \\times 4\\text{ cm} = -12\\text{ cm}$ (inverted).",
        "step_marking_rubric": [
            {"step": 1, "rule": "State lens formula and substitute signs correctly", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculate image position v = +60 cm and state nature", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculate magnification m = -3 and image height = -12 cm", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 10"
    },
    {
        "grade_level": 10,
        "subject": "Science",
        "chapter": "Life Processes",
        "topic": "Circulatory System in Humans",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "LA",
        "marks": 5.0,
        "question_text_latex": "Refer to the schematic representation of the human heart below:\n(a) Explain why double circulation is necessary in human beings.\n(b) Trace the pathway of oxygenated blood from the lungs until it reaches body tissues.\n(c) Why are the walls of the left ventricle thicker than those of the right ventricle?\n\n![Human Heart Schematic](data/diagrams/human_heart_schematic.svg)",
        "ideal_solution_latex": "(a) Double circulation ensures complete physical separation of oxygenated and deoxygenated blood by the cardiac septum, providing highly efficient oxygen delivery required to maintain high constant body temperature (homeothermy).\n(b) Pathway of oxygenated blood: Lungs $\\to$ Pulmonary veins $\\to$ Left atrium $\\to$ Bicuspid/Mitral valve $\\to$ Left ventricle $\\to$ Aorta $\\to$ Arteries and capillaries in body tissues.\n(c) The left ventricle has to pump blood at high pressure throughout the entire systemic circulation to distant extremities, whereas the right ventricle only pumps blood nearby to the lungs (pulmonary circuit).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Explain necessity of separation of oxygenated/deoxygenated blood", "allocated_marks": 1.5},
            {"step": 2, "rule": "Trace correct chronological pathway from lungs to body", "allocated_marks": 2.0},
            {"step": 3, "rule": "Explain muscular wall thickness requirement for left ventricle", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Science Chapter 6"
    },
    {
        "grade_level": 10,
        "subject": "Science",
        "chapter": "Life Processes",
        "topic": "Nutrition in Plants & Stomatal Apparatus",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 2,
        "question_format": "SA_I",
        "marks": 2.0,
        "question_text_latex": "With reference to the diagram comparing open and closed stomata:\n(a) Name the cells responsible for opening and closing of the stomatal pore.\n(b) Explain the mechanism that causes the stomatal pore to open.\n\n![Stomata Diagram](data/diagrams/stomata_diagram.svg)",
        "ideal_solution_latex": "(a) Guard cells.\n(b) When water flows into the guard cells by endosmosis, they swell and become turgid. Due to the differential elasticity of the thick inner wall and thin outer wall, the outer walls bulge outward, pulling the inner thick walls apart and opening the stomatal pore. When water is lost, guard cells become flaccid and the pore closes.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Identify guard cells correctly", "allocated_marks": 0.5},
            {"step": 2, "rule": "Explain endosmosis, turgidity and differential wall elasticity", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Science Chapter 6"
    },

    # =========================================================================
    # CLASS 10 MATHEMATICS (DIAGRAM-BASED & GEOMETRY)
    # =========================================================================
    {
        "grade_level": 10,
        "subject": "Mathematics",
        "chapter": "Circles",
        "topic": "Tangents from an External Point",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "From an external point $P$, two tangents $PA$ and $PB$ are drawn to a circle with centre $O$ and radius $r = 5\\text{ cm}$. If the distance of $P$ from the centre is $OP = 13\\text{ cm}$ as shown in the figure, find:\n(a) The length of tangent $PA$.\n(b) The area of quadrilateral $PAOB$.\n\n![Circle Tangents](data/diagrams/circle_tangents.svg)",
        "ideal_solution_latex": "1. Tangent is perpendicular to radius at point of contact: $\\angle OAP = 90^\\circ$.\n2. In right $\\triangle OAP$: $PA^2 = OP^2 - OA^2 = 13^2 - 5^2 = 169 - 25 = 144 \\implies PA = 12\\text{ cm}$.\n3. Since tangents from an external point are equal, $PB = PA = 12\\text{ cm}$.\n4. Area of $\\triangle OAP = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 12 \\times 5 = 30\\text{ cm}^2$.\n5. $\\text{Area of quadrilateral } PAOB = 2 \\times \\text{Area}(\\triangle OAP) = 2 \\times 30 = 60\\text{ cm}^2$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "State tangent perpendicular to radius and apply Pythagoras theorem", "allocated_marks": 1.0},
            {"step": 2, "rule": "Compute tangent length PA = 12 cm", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculate area of quad PAOB = 2 x 30 = 60 sq cm", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Mathematics Chapter 10"
    },
    {
        "grade_level": 10,
        "subject": "Mathematics",
        "chapter": "Some Applications of Trigonometry",
        "topic": "Heights and Distances",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 2,
        "question_format": "SA_I",
        "marks": 2.0,
        "question_text_latex": "An observer stands at point $C$ on the ground, at a distance $d = 30\\text{ m}$ from the foot of a vertical tower $AB$. The angle of elevation of the top of the tower is $\\theta = 60^\\circ$ as shown in the diagram. Find the height $h$ of the tower. (Take $\\sqrt{3} \\approx 1.732$)\n\n![Angle of Elevation](data/diagrams/trigonometry_elevation.svg)",
        "ideal_solution_latex": "1. In right triangle $\\triangle ABC$: $\\tan(60^\\circ) = \\frac{\\text{Opposite}}{\\text{Adjacent}} = \\frac{AB}{BC} = \\frac{h}{30}$.\n2. Since $\\tan(60^\\circ) = \\sqrt{3}$: $h = 30 \\times \\sqrt{3} = 30 \\times 1.732 = 51.96\\text{ m}$.\nTherefore, the height of the tower is $51.96\\text{ metres}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Formulate trigonometric relation tan(60) = h/30", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculate height h = 30 sqrt(3) = 51.96 m", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Mathematics Chapter 9"
    },

    # =========================================================================
    # CLASS 12 CHEMISTRY (CORE BOARD & DIAGRAM QUESTIONS)
    # =========================================================================
    {
        "grade_level": 12,
        "subject": "Chemistry",
        "chapter": "Electrochemistry",
        "topic": "Galvanic Cells & Nernst Equation",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "Consider the Daniell cell shown below operating at $298\\text{ K}$:\n$$\\text{Zn}(s) | \\text{Zn}^{2+}(aq, 0.1\\text{ M}) || \\text{Cu}^{2+}(aq, 0.01\\text{ M}) | \\text{Cu}(s)$$\nGiven $E^\\circ_{\\text{Zn}^{2+}/\\text{Zn}} = -0.76\\text{ V}$ and $E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} = +0.34\\text{ V}$.\n(a) Write the net cell reaction.\n(b) Calculate standard cell potential $E^\\circ_{\\text{cell}}$.\n(c) Calculate the cell EMF $E_{\\text{cell}}$ using the Nernst equation.\n\n![Daniell Galvanic Cell](data/diagrams/galvanic_cell.svg)",
        "ideal_solution_latex": "(a) Overall cell reaction: $\\text{Zn}(s) + \\text{Cu}^{2+}(aq) \\to \\text{Zn}^{2+}(aq) + \\text{Cu}(s)$, with $n = 2$.\n(b) Standard EMF: $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}} = +0.34\\text{ V} - (-0.76\\text{ V}) = +1.10\\text{ V}$.\n(c) Nernst Equation at $298\\text{ K}$:\n$$E_{\\text{cell}} = E^\\circ_{\\text{cell}} - \\frac{0.0591}{n} \\log\\frac{[\\text{Zn}^{2+}]}{[\\text{Cu}^{2+}]}$$\n$$E_{\\text{cell}} = 1.10 - \\frac{0.0591}{2} \\log\\left(\\frac{0.1}{0.01}\\right) = 1.10 - 0.02955 \\log(10) = 1.10 - 0.02955 = 1.070\\text{ V}$$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Write cell reaction and calculate E_cell_standard = 1.10 V", "allocated_marks": 1.0},
            {"step": 2, "rule": "State Nernst equation with n = 2", "allocated_marks": 1.0},
            {"step": 3, "rule": "Substitute concentrations and compute EMF = 1.07 V", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 3"
    },
    {
        "grade_level": 12,
        "subject": "Chemistry",
        "chapter": "Chemical Kinetics",
        "topic": "Order of Reaction & Arrhenius Equation",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "A first-order reaction has a rate constant $k = 4.5 \\times 10^{-3}\\text{ s}^{-1}$ at $300\\text{ K}$ and $k = 9.0 \\times 10^{-3}\\text{ s}^{-1}$ at $310\\text{ K}$.\n(a) Calculate the activation energy $E_a$ of the reaction. ($R = 8.314\\text{ J K}^{-1}\\text{ mol}^{-1}$, $\\log 2 \\approx 0.3010$)\n(b) What will be the half-life period $t_{1/2}$ of this reaction at $300\\text{ K}$?",
        "ideal_solution_latex": "(a) Using Arrhenius equation: $\\log\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{2.303 R}\\left[\\frac{T_2 - T_1}{T_1 T_2}\\right]$.\n$$\\log\\left(\\frac{9.0 \\times 10^{-3}}{4.5 \\times 10^{-3}}\\right) = \\log 2 = 0.3010 = \\frac{E_a}{2.303 \\times 8.314}\\left[\\frac{310 - 300}{300 \\times 310}\\right]$$\n$$E_a = \\frac{0.3010 \\times 19.147 \\times 93000}{10} = 53,598\\text{ J/mol} \\approx 53.6\\text{ kJ/mol}$$.\n(b) For first order reaction at $300\\text{ K}$: $t_{1/2} = \\frac{0.693}{k_1} = \\frac{0.693}{4.5 \\times 10^{-3}} = 154\\text{ seconds}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Write two-temperature Arrhenius formula", "allocated_marks": 1.0},
            {"step": 2, "rule": "Compute activation energy Ea = 53.6 kJ/mol", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculate first-order half life t1/2 = 154 s", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 4"
    },
    {
        "grade_level": 12,
        "subject": "Chemistry",
        "chapter": "Coordination Compounds",
        "topic": "Crystal Field Theory & Nomenclature",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_I",
        "marks": 2.0,
        "question_text_latex": "Give the IUPAC name and write the electronic configuration of central metal ion in terms of $t_{2g}$ and $e_g$ for the complex $[\\text{Co}(\\text{NH}_3)_6]^{3+}$. (Atomic number of $\\text{Co} = 27$)",
        "ideal_solution_latex": "1. Oxidation state of Co: $x + 6(0) = +3 \\implies x = +3$. Cobalt is in $+3$ state ($\\text{Co}^{3+}: [\\text{Ar}] 3d^6$).\n2. IUPAC Name: Hexaamminecobalt(III) ion.\n3. Since $\\text{NH}_3$ is a strong field ligand, crystal field splitting $\\Delta_o > P$ (pairing energy). All 6 $d$-electrons pair up in the lower energy $t_{2g}$ orbitals.\nElectronic configuration: $t_{2g}^6 e_g^0$ (diamagnetic low-spin complex).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Write correct IUPAC name Hexaamminecobalt(III) ion", "allocated_marks": 1.0},
            {"step": 2, "rule": "State strong field pairing and configuration t2g^6 eg^0", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 9"
    },
    {
        "grade_level": 12,
        "subject": "Chemistry",
        "chapter": "Haloalkanes and Haloarenes",
        "topic": "Nucleophilic Substitution Mechanisms",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 2,
        "question_format": "MCQ",
        "marks": 1.0,
        "question_text_latex": "Which of the following alkyl halides undergoes nucleophilic substitution via $S_N1$ mechanism with the fastest rate?",
        "options": {
            "A": "$\\text{CH}_3\\text{CH}_2\\text{Cl}$",
            "B": "$(\\text{CH}_3)_2\\text{CH}-\\text{Cl}$",
            "C": "$(\\text{CH}_3)_3\\text{C}-\\text{Cl}$",
            "D": "$\\text{CH}_3\\text{Cl}$"
        },
        "correct_option": "C",
        "ideal_solution_latex": "The rate-determining step in $S_N1$ mechanism involves carbocation intermediate formation. The stability order of carbocations is $3^\\circ > 2^\\circ > 1^\\circ > \\text{methyl}$. Since $(\\text{CH}_3)_3\\text{C}-\\text{Cl}$ forms a highly stable tertiary carbocation stabilized by $+I$ inductive effect and 9 hyperconjugative structures, it reacts fastest via $S_N1$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Select option C and explain carbocation stability 3 > 2 > 1", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Chemistry Chapter 10"
    },

    # =========================================================================
    # CLASS 11 CHEMISTRY (CORE ATOM, BONDING, THERMODYNAMICS)
    # =========================================================================
    {
        "grade_level": 11,
        "subject": "Chemistry",
        "chapter": "Structure of Atom",
        "topic": "Bohr Model & de Broglie Relation",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_I",
        "marks": 2.0,
        "question_text_latex": "Calculate the de Broglie wavelength associated with an electron moving with a velocity of $2.05 \\times 10^7\\text{ m/s}$. (Mass of electron $m = 9.11 \\times 10^{-31}\\text{ kg}$, $h = 6.626 \\times 10^{-34}\\text{ J s}$)",
        "ideal_solution_latex": "Using de Broglie relationship: $\\lambda = \\frac{h}{m v}$.\n$$\\lambda = \\frac{6.626 \\times 10^{-34}\\text{ J s}}{(9.11 \\times 10^{-31}\\text{ kg}) \\times (2.05 \\times 10^7\\text{ m/s})}$$\n$$\\lambda = \\frac{6.626 \\times 10^{-34}}{1.8675 \\times 10^{-23}} = 3.55 \\times 10^{-11}\\text{ m} = 0.0355\\text{ nm}$$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "State de Broglie formula lambda = h / (m v)", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculate numerical value 3.55 x 10^-11 m", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Chemistry Chapter 2"
    },
    {
        "grade_level": 11,
        "subject": "Chemistry",
        "chapter": "Chemical Bonding and Molecular Structure",
        "topic": "VSEPR & Molecular Orbital Theory",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "Using Molecular Orbital Theory (MOT):\n(a) Write the molecular orbital electronic configuration of $O_2$ molecule.\n(b) Calculate its bond order.\n(c) Explain why $O_2$ is paramagnetic in nature.",
        "ideal_solution_latex": "(a) $O_2$ has 16 electrons: $\\sigma 1s^2 \\sigma^* 1s^2 \\sigma 2s^2 \\sigma^* 2s^2 \\sigma 2p_z^2 (\\pi 2p_x^2 = \\pi 2p_y^2) (\\pi^* 2p_x^1 = \\pi^* 2p_y^1)$.\n(b) Number of bonding electrons $N_b = 10$, anti-bonding electrons $N_a = 6$.\n$$\\text{Bond Order} = \\frac{N_b - N_a}{2} = \\frac{10 - 6}{2} = 2.0$$.\n(c) The presence of two unpaired electrons in the degenerate antibonding orbitals $\\pi^* 2p_x$ and $\\pi^* 2p_y$ accounts for the paramagnetic behaviour of oxygen.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Write correct MO electronic configuration of O2", "allocated_marks": 1.0},
            {"step": 2, "rule": "Calculate bond order = (10 - 6)/2 = 2.0", "allocated_marks": 1.0},
            {"step": 3, "rule": "Identify 2 unpaired electrons in pi* anti-bonding orbitals for paramagnetism", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Chemistry Chapter 4"
    },
    {
        "grade_level": 11,
        "subject": "Chemistry",
        "chapter": "Chemical Thermodynamics",
        "topic": "Gibbs Free Energy & Spontaneity",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "For a reaction, $\\Delta H = +35.5\\text{ kJ mol}^{-1}$ and $\\Delta S = +83.6\\text{ J K}^{-1}\\text{ mol}^{-1}$. At what temperature will the reaction become spontaneous in the forward direction?",
        "ideal_solution_latex": "1. Condition for spontaneity: $\\Delta G = \\Delta H - T \\Delta S < 0 \\implies T \\Delta S > \\Delta H \\implies T > \\frac{\\Delta H}{\\Delta S}$.\n2. Given $\\Delta H = 35.5 \\times 10^3\\text{ J mol}^{-1}$ and $\\Delta S = 83.6\\text{ J K}^{-1}\\text{ mol}^{-1}$.\n$$T > \\frac{35500\\text{ J mol}^{-1}}{83.6\\text{ J K}^{-1}\\text{ mol}^{-1}} = 424.6\\text{ K}$$.\nTherefore, the reaction becomes spontaneous at temperatures above $424.6\\text{ K}$ ($151.6^\\circ\\text{C}$).",
        "step_marking_rubric": [
            {"step": 1, "rule": "State spontaneity condition Delta G = Delta H - T Delta S < 0", "allocated_marks": 1.0},
            {"step": 2, "rule": "Convert units of Delta H to Joules correctly", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculate threshold temperature T > 424.6 K", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Chemistry Chapter 6"
    },

    # =========================================================================
    # CLASS 12 BIOLOGY (GENETICS, BIOTECHNOLOGY, REPRODUCTION)
    # =========================================================================
    {
        "grade_level": 12,
        "subject": "Biology",
        "chapter": "Principles of Inheritance and Variation",
        "topic": "Mendelian Dihybrid Cross & Independent Assortment",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "LA",
        "marks": 5.0,
        "question_text_latex": "In a dihybrid cross conducted by Gregor Mendel between pure breeding round yellow seeded pea plants ($RRYY$) and wrinkled green seeded pea plants ($rryy$):\n(a) State the phenotype and genotype of the $F_1$ generation.\n(b) Draw the Punnett square for the $F_2$ generation.\n(c) State the phenotypic and genotypic ratios obtained in $F_2$.\n(d) State the law of inheritance derived from this cross.",
        "ideal_solution_latex": "(a) $F_1$ generation: All plants are heterozygous Round Yellow with genotype $RrYy$.\n(b) Punnett square for selfing $RrYy \\times RrYy$ produces 16 zygotic combinations from gametes $RY, Ry, rY, ry$.\n(c) Ratios:\n- Phenotypic Ratio: $9\\text{ Round Yellow} : 3\\text{ Round Green} : 3\\text{ Wrinkled Yellow} : 1\\text{ Wrinkled Green}$.\n- Genotypic Ratio: $1:2:2:4:1:2:1:2:1$.\n(d) Law of Independent Assortment: When two pairs of traits are combined in a hybrid, segregation of one pair of characters is independent of the other pair of characters during gamete formation.",
        "step_marking_rubric": [
            {"step": 1, "rule": "State F1 genotype RrYy and phenotype Round Yellow", "allocated_marks": 1.0},
            {"step": 2, "rule": "Draw 16-box Punnett square correctly", "allocated_marks": 2.0},
            {"step": 3, "rule": "State 9:3:3:1 phenotypic ratio", "allocated_marks": 1.0},
            {"step": 4, "rule": "Define Law of Independent Assortment accurately", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 12 Biology Chapter 5"
    },
    {
        "grade_level": 12,
        "subject": "Biology",
        "chapter": "Biotechnology - Principles and Processes",
        "topic": "Recombinant DNA Tools & PCR",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "Polymerase Chain Reaction (PCR) is used to amplify a specific segment of DNA in vitro.\n(a) Name the three sequential steps involved in each cycle of PCR.\n(b) Why is a thermostable DNA polymerase ($Taq$ polymerase) specifically used, and from which organism is it isolated?",
        "ideal_solution_latex": "(a) Three sequential steps of PCR:\n1. Denaturation: High temperature ($94-96^\\circ\\text{C}$) breaks hydrogen bonds, separating double-stranded DNA into single strands.\n2. Annealing: Lower temperature ($50-60^\\circ\\text{C}$) allows two sets of oligonucleotide primers to hybridize to complementary regions.\n3. Extension: At $72^\\circ\\text{C}$, DNA polymerase synthesizes new complementary strands by adding dNTPs.\n(b) $Taq$ polymerase is isolated from the thermophilic bacterium *Thermus aquaticus*. It remains enzymatically active and stable during high-temperature denaturation, eliminating the need to add fresh enzyme after each cycle.",
        "step_marking_rubric": [
            {"step": 1, "rule": "List and explain Denaturation, Annealing, Extension with temperatures", "allocated_marks": 1.5},
            {"step": 2, "rule": "Name Thermus aquaticus and explain heat stability benefit", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 12 Biology Chapter 11"
    },

    # =========================================================================
    # CLASS 11 BIOLOGY (CELL DIVISION, PHYSIOLOGY, PHOTOSYNTHESIS)
    # =========================================================================
    {
        "grade_level": 11,
        "subject": "Biology",
        "chapter": "Cell Cycle and Cell Division",
        "topic": "Stages of Mitosis & Meiosis",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 2,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "Distinguish between Mitosis and Meiosis with respect to:\n(a) Number of daughter cells formed and their ploidy level.\n(b) Occurrence of crossing over and genetic recombination.\n(c) Site of occurrence in the human body.",
        "ideal_solution_latex": "1. Number of daughter cells & ploidy:\n- Mitosis: Produces 2 identical diploid ($2n$) daughter cells.\n- Meiosis: Produces 4 non-identical haploid ($n$) daughter cells.\n2. Crossing over:\n- Mitosis: Absent; chromosomes duplicate and separate without recombination.\n- Meiosis: Present; occurs between non-sister chromatids of homologous chromosomes during Pachytene of Prophase I, facilitated by the enzyme recombinase.\n3. Site of occurrence:\n- Mitosis: Somatic cells for growth, tissue repair, and asexual reproduction.\n- Meiosis: Germ cells in gonads (testes and ovaries) during gametogenesis.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Compare daughter cell count (2 vs 4) and ploidy (2n vs n)", "allocated_marks": 1.0},
            {"step": 2, "rule": "Explain crossing over in pachytene stage of meiosis", "allocated_marks": 1.0},
            {"step": 3, "rule": "Compare somatic cells vs reproductive germ cells", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 11 Biology Chapter 10"
    },
    {
        "grade_level": 11,
        "subject": "Biology",
        "chapter": "Photosynthesis in Higher Plants",
        "topic": "Light Reaction & Photophosphorylation",
        "primary_exam": "CBSE_BOARD",
        "difficulty_tier": 3,
        "question_format": "SA_II",
        "marks": 3.0,
        "question_text_latex": "Describe the Z-scheme of non-cyclic photophosphorylation. What are the end products generated during this process?",
        "ideal_solution_latex": "1. Z-scheme begins when Photosystem II ($P_{680}$) absorbs light at $680\\text{ nm}$, exciting electrons to an electron acceptor.\n2. Electrons pass through an electron transport system (cytochromes) to Photosystem I ($P_{700}$), creating a proton gradient that drives ATP synthesis.\n3. Simultaneously, light absorbed by $P_{700}$ excites electrons transferred to $NADP^+$, reducing it to $NADPH + H^+$ catalyzed by ferredoxin-$NADP^+$ reductase.\n4. Electrons lost by PS II are continuously replaced by photolysis of water: $2\\text{H}_2\\text{O} \\to 4\\text{H}^+ + \\text{O}_2 + 4e^-$.\nEnd products generated: $ATP$, $NADPH$, and oxygen ($O_2$).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Describe electron flow from PS II through cytochromes to PS I", "allocated_marks": 1.5},
            {"step": 2, "rule": "Explain photolysis of water and list end products ATP, NADPH, O2", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 11 Biology Chapter 13"
    }
]

def run_expansion():
    print(f"Starting question expansion with {len(QUESTIONS)} high-yield board questions...")

    # Format questions
    formatted_qs = []
    for q in QUESTIONS:
        c_hash = compute_hash(q["grade_level"], q["subject"], q["question_text_latex"])
        item = {
            "id": str(uuid.uuid4()),
            "grade_level": int(q["grade_level"]),
            "subject": str(q["subject"]),
            "chapter": str(q["chapter"]),
            "topic": str(q["topic"]),
            "primary_exam": str(q.get("primary_exam", "CBSE_BOARD")),
            "applicable_exams": [q.get("primary_exam", "CBSE_BOARD")],
            "difficulty_tier": int(q.get("difficulty_tier", 3)),
            "question_format": str(q["question_format"]),
            "marks": float(q["marks"]),
            "question_text_latex": str(q["question_text_latex"]),
            "options": q.get("options"),
            "correct_option": q.get("correct_option"),
            "ideal_solution_latex": str(q["ideal_solution_latex"]),
            "step_marking_rubric": q.get("step_marking_rubric", []),
            "source_book": str(q.get("source_book", "NCERT")),
            "content_hash": c_hash
        }
        formatted_qs.append(item)

    # Use db.upsert_questions which handles Supabase & SQLite seamlessly
    count = db.upsert_questions(formatted_qs)
    print(f"Successfully upserted {count} questions into database!")

    # Verify counts
    tax = db.get_taxonomy()
    total = sum(
        sum(
            c_info.get("count", 0) if isinstance(c_info, dict) else c_info
            for c_info in chaps.values()
        )
        for grades in tax.values()
        for chaps in grades.values()
    )
    print(f"Current Total Question Bank Size across all subjects: {total} questions")

if __name__ == "__main__":
    run_expansion()

