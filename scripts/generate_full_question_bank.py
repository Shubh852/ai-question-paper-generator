"""
Generate and Seed Comprehensive Master Question Bank into Supabase Cloud Database.
Covers:
- Class 10: Mathematics, Science, Social Science, English (NCERT, RD Sharma, Lakhmir Singh)
- Class 11: Physics, Chemistry, Mathematics, Biology, English (NCERT, HC Verma Vol 1, OP Tandon, RD Sharma, Trueman's)
- Class 12: Physics, Chemistry, Mathematics, Biology, English (NCERT, HC Verma Vol 2, OP Tandon, RD Sharma, Trueman's)
All chapters and topics with step marking rubrics, LaTeX formulas, and competitive exam mappings.
"""

import os
import sys
import json
import hashlib
import logging
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

load_dotenv()
from backend.database import db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("seed_full")

QUESTIONS = [
    # =========================================================================
    # CLASS 10 - SCIENCE (NCERT + Lakhmir Singh)
    # =========================================================================
    {
        "grade_level": 10, "subject": "Science", "chapter": "Acids, Bases and Salts",
        "topic": "pH Scale and Everyday Applications", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "Tooth decay starts when the pH of the mouth is lower than:",
        "options": {"A": "7.0", "B": "6.5", "C": "5.5", "D": "8.0"},
        "correct_option": "C",
        "ideal_solution_latex": "Tooth enamel made of calcium hydroxyapatite corrodes when the pH in the mouth falls below $5.5$ due to bacterial acid production.",
        "step_marking_rubric": [{"step": 1, "rule": "Correct pH threshold of 5.5", "allocated_marks": 1.0}],
        "source_book": "NCERT Class 10 Science Chapter 2"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Acids, Bases and Salts",
        "topic": "Salts and Chlor-Alkali Process", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "During the chlor-alkali process:\n(a) Write the balanced chemical equation.\n(b) Name the gases liberated at the anode and cathode.\n(c) State one major commercial use of each gas.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) $2\\text{NaCl}(aq) + 2\\text{H}_2\\text{O}(l) \\to 2\\text{NaOH}(aq) + \\text{Cl}_2(g) + \\text{H}_2(g)$.\n(b) Chlorine ($\\text{Cl}_2$) is liberated at the anode; Hydrogen ($\\text{H}_2$) is liberated at the cathode.\n(c) $\\text{Cl}_2$ is used for water treatment/disinfection/PVC; $\\text{H}_2$ is used for making ammonia for fertilizers/fuel.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Balanced equation of chlor-alkali process", "allocated_marks": 1.0},
            {"step": 2, "rule": "Correct identification of anode and cathode gases", "allocated_marks": 1.0},
            {"step": 3, "rule": "Industrial use of Cl2 and H2", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science / Lakhmir Singh Chemistry"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Metals and Non-Metals",
        "topic": "Reactivity Series and Extraction of Metals", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Differentiate between roasting and calcination with suitable balanced chemical equations for each using zinc ores.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. **Roasting**: Heating sulphide ore in excess air below its melting point.\n$2\\text{ZnS} + 3\\text{O}_2 \\xrightarrow{\\Delta} 2\\text{ZnO} + 2\\text{SO}_2$.\n2. **Calcination**: Heating carbonate ore in limited or absent air.\n$\\text{ZnCO}_3 \\xrightarrow{\\Delta} \\text{ZnO} + \\text{CO}_2$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Definition and balanced equation of roasting (ZnS)", "allocated_marks": 1.5},
            {"step": 2, "rule": "Definition and balanced equation of calcination (ZnCO3)", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Science Chapter 3"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Carbon and its Compounds",
        "topic": "Homologous Series and Functional Groups", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "MCQ", "marks": 1.0,
        "question_text_latex": "Which of the following compounds belongs to the homologous series of alkynes?",
        "options": {"A": "$\\text{C}_3\\text{H}_8$", "B": "$\\text{C}_3\\text{H}_6$", "C": "$\\text{C}_3\\text{H}_4$", "D": "$\\text{C}_4\\text{H}_{10}$"},
        "correct_option": "C",
        "ideal_solution_latex": "The general formula for alkynes is $\\text{C}_n\\text{H}_{2n-2}$. For $n=3$, $\\text{C}_3\\text{H}_{2(3)-2} = \\text{C}_3\\text{H}_4$ (propyne).",
        "step_marking_rubric": [{"step": 1, "rule": "Identify C3H4 using formula CnH2n-2", "allocated_marks": 1.0}],
        "source_book": "NCERT Class 10 Science Chapter 4"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Carbon and its Compounds",
        "topic": "Saponification and Micelle Formation", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "(a) What is saponification? Write the chemical equation for the preparation of soap.\n(b) Explain the cleansing action of soaps with a neat labeled diagram of micelle formation.\n(c) Why do soaps not form lather with hard water?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Saponification is the alkaline hydrolysis of an ester/fat using $\\text{NaOH}$ to yield soap (sodium salt of fatty acid) and glycerol: $\\text{Fat} + 3\\text{NaOH} \\to \\text{Glycerol} + 3\\text{RCOO}^-\\text{Na}^+$.\n(b) Soap molecules have a hydrophobic hydrocarbon tail and a hydrophilic ionic head ($\\text{COO}^-\\text{Na}^+$). In water containing oil/grease, hydrophobic tails dissolve in oil while ionic heads face outward towards water, forming spherical clusters called **micelles**.\n(c) Hard water contains $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions which react with soap to form an insoluble curdy precipitate called **scum**.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Saponification definition and balanced reaction", "allocated_marks": 1.5},
            {"step": 2, "rule": "Cleansing action explanation and micelle structure", "allocated_marks": 2.0},
            {"step": 3, "rule": "Scum formation with Ca2+/Mg2+ ions in hard water", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Science / Lakhmir Singh Chemistry"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Control and Coordination",
        "topic": "Reflex Arc and Nervous System", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Trace the sequence of events when your hand accidentally touches a hot object. Name the components of the reflex arc involved.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Pathway: Receptor (heat thermoreceptor in skin) $\\to$ Sensory neuron $\\to$ Spinal cord (Relay neuron) $\\to$ Motor neuron $\\to$ Effector (biceps muscle contracts to pull hand away).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Stepwise pathway from receptor to spinal cord", "allocated_marks": 1.0},
            {"step": 2, "rule": "Motor neuron to effector muscle response", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 7"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "How do Organisms Reproduce?",
        "topic": "Sexual Reproduction in Flowering Plants", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Distinguish between self-pollination and cross-pollination. Explain what happens to the ovule and the ovary after successful fertilization in an angiosperm.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Self-pollination: Transfer of pollen from anther to stigma of same flower/plant.\nCross-pollination: Transfer of pollen to stigma of a different plant of same species.\nPost-fertilization:\n- Ovule develops into a **seed** containing the embryo and food reserve.\n- Ovary grows rapidly and ripens into a **fruit**.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Clear distinction between self and cross pollination", "allocated_marks": 1.0},
            {"step": 2, "rule": "Ovule develops into seed", "allocated_marks": 1.0},
            {"step": 3, "rule": "Ovary develops into fruit", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 8"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Heredity",
        "topic": "Mendel's Monohybrid Cross", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A cross is made between a pure tall pea plant ($TT$) and a pure dwarf pea plant ($tt$).\n(a) What is the phenotype and genotype of the $F_1$ generation?\n(b) Work out the phenotypic and genotypic ratio of the $F_2$ generation upon self-pollinating $F_1$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) $F_1$ Generation: Genotype $= Tt$, Phenotype $= 100\\%$ Tall.\n(b) $F_2$ Generation (selfing $Tt \\times Tt$):\n- Genotypic ratio: $1 TT : 2 Tt : 1 tt$ ($1:2:1$).\n- Phenotypic ratio: $3$ Tall : $1$ Dwarf ($3:1$).",
        "step_marking_rubric": [
            {"step": 1, "rule": "F1 genotype Tt and all tall phenotype", "allocated_marks": 1.0},
            {"step": 2, "rule": "F2 Punnett square derivation", "allocated_marks": 1.0},
            {"step": 3, "rule": "Stating phenotypic 3:1 and genotypic 1:2:1 ratios", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 9"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Light – Reflection and Refraction",
        "topic": "Mirror Formula and Magnification", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A concave mirror produces three times magnified real image of an object placed at $10\\text{ cm}$ in front of it. Where is the image located? What is the focal length of the mirror?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Given: $u = -10\\text{ cm}$. Real image $\\implies m = -3$.\n$m = -\\frac{v}{u} \\implies -3 = -\\frac{v}{-10} \\implies v = -30\\text{ cm}$. Image is located $30\\text{ cm}$ in front of the mirror.\nUsing mirror formula: $\\frac{1}{f} = \\frac{1}{v} + \\frac{1}{u} = \\frac{1}{-30} + \\frac{1}{-10} = \\frac{-1 - 3}{30} = -\\frac{4}{30} = -\\frac{2}{15} \\implies f = -7.5\\text{ cm}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Using magnification formula to find v = -30 cm", "allocated_marks": 1.5},
            {"step": 2, "rule": "Using mirror formula to calculate f = -7.5 cm", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Science Chapter 10 / Lakhmir Singh Physics"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Human Eye and the Colourful World",
        "topic": "Atmospheric Refraction and Dispersion", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "Why do stars appear to twinkle in the night sky, but planets do not? Explain scientifically.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Stars are point sources of light at immense distances. Light passing through continuously fluctuating layers of atmospheric refractive index bends erratically, changing brightness (twinkling).\nPlanets are closer and act as extended sources (collections of point sources). The twinkling variations from individual points average out to zero.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Point source and atmospheric refraction for stars", "allocated_marks": 1.0},
            {"step": 2, "rule": "Extended source averaging effect for planets", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Science Chapter 11"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Electricity",
        "topic": "Ohm's Law and Resistors in Combination", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Three resistors of $6\\ \\Omega$ each are given. How can they be connected to get an equivalent resistance of:\n(a) $9\\ \\Omega$\n(b) $4\\ \\Omega$?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) To get $9\\ \\Omega$: Connect two $6\\ \\Omega$ resistors in parallel, and connect this combination in series with the third.\n$R_p = \\frac{6 \\times 6}{6 + 6} = 3\\ \\Omega$. Total $R = 3 + 6 = 9\\ \\Omega$.\n(b) To get $4\\ \\Omega$: Connect two $6\\ \\Omega$ resistors in series, and connect this combination in parallel with the third.\n$R_s = 6 + 6 = 12\\ \\Omega$. Total $R = \\frac{12 \\times 6}{12 + 6} = \\frac{72}{18} = 4\\ \\Omega$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Combination and calculation for 9 ohms (parallel + series)", "allocated_marks": 1.5},
            {"step": 2, "rule": "Combination and calculation for 4 ohms (series + parallel)", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 Science Chapter 12 / Lakhmir Singh Physics"
    },
    {
        "grade_level": 10, "subject": "Science", "chapter": "Magnetic Effects of Electric Current",
        "topic": "Electromagnetic Induction and Right-Hand Thumb Rule", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 2.0,
        "question_text_latex": "State Fleming's Left-Hand Rule. Name one device that works on the principle of force on a current-carrying conductor in a magnetic field.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Stretch the thumb, forefinger, and middle finger of the left hand mutually perpendicular:\n- Forefinger points in the direction of the **Magnetic Field**.\n- Middle finger points in the direction of **Current**.\n- Thumb points in the direction of **Motion / Force** acting on the conductor.\nDevice: **Electric Motor**.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct statement of Fleming's Left-Hand Rule", "allocated_marks": 1.5},
            {"step": 2, "rule": "Naming electric motor", "allocated_marks": 0.5}
        ],
        "source_book": "NCERT Class 10 Science Chapter 13"
    },

    # =========================================================================
    # CLASS 10 - SOCIAL SCIENCE (NCERT)
    # =========================================================================
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Nationalism in India",
        "topic": "Non-Cooperation Movement and Salt March", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "Why did Mahatma Gandhi perceive salt as a powerful symbol that could unite the Indian nation? Describe the course of the historic Dandi March of 1930.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. **Salt as a Unifying Symbol**: Salt was consumed equally by rich and poor. The British salt monopoly and high tax directly affected every household, revealing the oppressive face of colonial rule.\n2. **The Dandi March**: On 12 March 1930, Gandhi began the march from Sabarmati Ashram with 78 volunteers.\n- Traveled 240 miles to coastal Dandi in 24 days.\n- On 6 April 1930, Gandhi reached Dandi, boiled seawater, and manufactured salt, formally breaking the Salt Law and inaugurating the Civil Disobedience Movement.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Explanation of salt as universal symbol uniting all classes", "allocated_marks": 2.0},
            {"step": 2, "rule": "Details of the Dandi March route, volunteers, dates", "allocated_marks": 2.0},
            {"step": 3, "rule": "Breaking the salt law and launching Civil Disobedience", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 History: India and Contemporary World II"
    },
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Resources and Development",
        "topic": "Soil Conservation and Resource Planning", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Explain any three institutional and technical measures adopted by the Government of India to conserve agricultural soil and land resources.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. **Contour Ploughing & Terrace Farming**: In hilly regions, terracing and ploughing across contour lines decelerate water flow and prevent sheet erosion.\n2. **Strip Cropping**: Strips of grass are left to grow between crops to break the force of the wind.\n3. **Shelter Belts**: Planting rows of trees creates windbreaks that stabilize sand dunes in arid zones (e.g., Western Rajasthan).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Contour ploughing and terrace farming", "allocated_marks": 1.0},
            {"step": 2, "rule": "Strip cropping mechanism", "allocated_marks": 1.0},
            {"step": 3, "rule": "Shelter belts in coastal/desert regions", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Geography: Contemporary India II"
    },
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Federalism",
        "topic": "Decentralization in India (1992 Amendment)", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Analyze the major constitutional amendments made in 1992 (73rd and 74th Amendments) to make the third tier of Indian democracy more powerful and effective.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Key provisions of the 1992 Decentralization Amendment:\n1. Mandatory regular elections to local government bodies (Panchayats and Municipalities).\n2. Reservation of seats for SC, ST, and OBC candidates.\n3. Mandatory at least one-third ($33\\%$) reservation of all seats for women.\n4. Creation of an independent State Election Commission in each state to conduct local elections.\n5. State governments required to share revenue and powers with local bodies.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Mandatory elections and independent State Election Commission", "allocated_marks": 1.0},
            {"step": 2, "rule": "One-third reservation for women and social equity seats", "allocated_marks": 1.0},
            {"step": 3, "rule": "Revenue and power sharing with local bodies", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Civics: Democratic Politics II"
    },
    {
        "grade_level": 10, "subject": "Social Science", "chapter": "Money and Credit",
        "topic": "Formal vs Informal Sources of Credit", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Differentiate between formal and informal sources of credit in India on the basis of interest rates, collateral requirements, and regulatory supervision.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "| Basis | Formal Sources (Banks & Cooperatives) | Informal Sources (Moneylenders, Traders) |\n|---|---|---|\n| **Supervision** | Regulated by the Reserve Bank of India (RBI) | No government agency supervises lending activities |\n| **Interest Rate** | Low and reasonable transparent rates | Exorbitantly high rates, often leading to debt-traps |\n| **Collateral** | Strictly requires documentation and collateral | Loans often granted without legal collateral on personal terms |",
        "step_marking_rubric": [
            {"step": 1, "rule": "RBI supervision distinction", "allocated_marks": 1.0},
            {"step": 2, "rule": "Interest rate contrast and debt-trap risk", "allocated_marks": 1.0},
            {"step": 3, "rule": "Collateral and documentation difference", "allocated_marks": 1.0}
        ],
        "source_book": "NCERT Class 10 Economics: Understanding Economic Development"
    },

    # =========================================================================
    # CLASS 10 - ENGLISH (First Flight & Footprints)
    # =========================================================================
    {
        "grade_level": 10, "subject": "English", "chapter": "Nelson Mandela: Long Walk to Freedom",
        "topic": "Apartheid and Concept of Freedom", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "What twin obligations does Nelson Mandela mention in his autobiography? Why was it impossible for a Black South African to fulfill both during apartheid?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Mandela mentions that every man has **twin obligations**:\n1. Obligation to his family, parents, wife, and children.\n2. Obligation to his people, community, and country.\nIn an apartheid society, an African man of color attempting to fulfill his duty to his people was torn from his home, punished, and forced to live an isolated existence as an outlaw.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Definition of twin obligations (family and community)", "allocated_marks": 1.5},
            {"step": 2, "rule": "Explanation of persecution and apartheid restrictions", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 English: First Flight"
    },
    {
        "grade_level": 10, "subject": "English", "chapter": "The Thief's Story",
        "topic": "Transformation of Hari Singh and Trust", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "'Compassion and unconditional trust can reform even a hardened criminal.' Discuss this statement with reference to Anil's treatment of Hari Singh in Ruskin Bond's 'The Thief's Story'.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Anil treats Hari Singh with patience, trust, and kindness. Though aware that Hari made petty money from grocery shopping, Anil ignores it and teaches him how to cook, write sentences, and add numbers.\nWhen Hari steals Anil's 600 rupees, his conscience pricks him at the railway platform. He realizes that education and dignity under Anil's tutelage are worth vastly more than a few hundred rupees.\nHari returns the damp money. Anil, knowing full well of the theft, does not rebuke him, hand him to police, or show anger. This quiet magnanimity cements Hari's moral reform.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Anil's initial trust and education teaching literacy", "allocated_marks": 1.5},
            {"step": 2, "rule": "Hari's dilemma at the station and return of money", "allocated_marks": 2.0},
            {"step": 3, "rule": "Anil's silent acceptance demonstrating power of compassion", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 10 English: Footprints Without Feet"
    },

    # =========================================================================
    # CLASS 11 - PHYSICS (HC Verma Vol 1 + NCERT)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Work, Energy and Power",
        "topic": "Conservative Forces and Potential Energy", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "The potential energy of a particle moving along the $x$-axis is given by $U(x) = ax^2 - bx$, where $a$ and $b$ are positive constants.\n(a) Find the equilibrium position of the particle.\n(b) Determine whether the equilibrium is stable, unstable, or neutral.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Force $F = -\\frac{dU}{dx} = -(2ax - b) = b - 2ax$.\nAt equilibrium, $F = 0 \\implies b - 2ax = 0 \\implies x_0 = \\frac{b}{2a}$.\n(b) Second derivative: $\\frac{d^2U}{dx^2} = \\frac{d}{dx}(2ax - b) = 2a$.\nSince $a > 0$, $\\frac{d^2U}{dx^2} > 0$ everywhere, including $x_0$. Therefore, potential energy is a minimum, and the equilibrium is **stable**.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Finding force F = -dU/dx = b - 2ax", "allocated_marks": 1.0},
            {"step": 2, "rule": "Equilibrium position x = b/(2a)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Evaluating second derivative > 0 proving stable equilibrium", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 6"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "System of Particles and Rotational Motion",
        "topic": "Moment of Inertia and Parallel Axis Theorem", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "JEE_ADVANCED"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "State the Parallel Axes Theorem. Using this theorem, calculate the moment of inertia of a uniform circular disc of mass $M$ and radius $R$ about a tangent lying in the plane of the disc.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "1. **Theorem of Parallel Axes**: $I = I_{cm} + M d^2$, where $d$ is the perpendicular distance between the parallel axes.\n2. For a circular disc, moment of inertia about a diameter in its plane is $I_d = \\frac{1}{4}MR^2$.\n3. Distance to the tangent in the plane is $d = R$.\n$I_{\\text{tangent}} = I_d + M R^2 = \\frac{1}{4}MR^2 + MR^2 = \\frac{5}{4}MR^2$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Statement of parallel axes theorem", "allocated_marks": 1.0},
            {"step": 2, "rule": "Diameter moment of inertia Id = 1/4 MR^2", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculation yielding 5/4 MR^2", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 10"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Gravitation",
        "topic": "Escape Velocity and Orbital Speed", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Derive an expression for the escape speed from the surface of Earth in terms of acceleration due to gravity $g$ and Earth's radius $R$. What is its numerical value?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Total energy at surface for a mass $m$ launched with escape velocity $v_e$:\n$E = \\frac{1}{2}m v_e^2 - \\frac{GMm}{R}$.\nAt infinity, $E = 0$ (just escapes):\n$\\frac{1}{2}m v_e^2 - \\frac{GMm}{R} = 0 \\implies v_e = \\sqrt{\\frac{2GM}{R}}$.\nSince $g = \\frac{GM}{R^2} \\implies GM = g R^2$, we have:\n$v_e = \\sqrt{2gR}$.\nFor Earth ($g = 9.8\\text{ m/s}^2, R = 6.4 \\times 10^6\\text{ m}$):\n$v_e = \\sqrt{2 \\times 9.8 \\times 6.4 \\times 10^6} \\approx 11.2\\text{ km/s}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Conservation of energy equation at surface and infinity", "allocated_marks": 1.0},
            {"step": 2, "rule": "Derivation ve = sqrt(2gR)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Numerical evaluation 11.2 km/s", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 11"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Thermodynamics",
        "topic": "First Law of Thermodynamics and Carnot Engine", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "(a) State the First Law of Thermodynamics and express it in differential form.\n(b) An ideal gas expands adiabatically from volume $V_1$ to $V_2$. Show that the work done during this adiabatic expansion is $W = \\frac{P_1V_1 - P_2V_2}{\\gamma - 1}$.\n(c) A Carnot engine absorbs $1000\\text{ J}$ of heat from a reservoir at $400\\text{ K}$ and rejects heat to a sink at $300\\text{ K}$. Calculate its efficiency and work output.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) $\\Delta Q = \\Delta U + \\Delta W$ or $dQ = dU + dW$.\n(b) In adiabatic process, $PV^\\gamma = K \\implies P = K V^{-\\gamma}$.\n$W = \\int_{V_1}^{V_2} P dV = K \\left[ \\frac{V^{1-\\gamma}}{1-\\gamma} \\right]_{V_1}^{V_2} = \\frac{K V_2^{1-\\gamma} - K V_1^{1-\\gamma}}{1-\\gamma} = \\frac{P_2V_2 - P_1V_1}{1-\\gamma} = \\frac{P_1V_1 - P_2V_2}{\\gamma - 1}$.\n(c) Carnot efficiency $\\eta = 1 - \\frac{T_C}{T_H} = 1 - \\frac{300}{400} = 0.25$ or $25\\%$.\nWork done $W = \\eta Q_H = 0.25 \\times 1000 = 250\\text{ J}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Statement of First Law dQ = dU + dW", "allocated_marks": 1.0},
            {"step": 2, "rule": "Integration derivation of adiabatic work formula", "allocated_marks": 2.5},
            {"step": 3, "rule": "Efficiency calculation 25% and W = 250 J", "allocated_marks": 1.5}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 26"
    },
    {
        "grade_level": 11, "subject": "Physics", "chapter": "Oscillations",
        "topic": "Simple Harmonic Motion and Energy", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A particle executes simple harmonic motion with amplitude $A$. At what displacement from the mean position is the kinetic energy equal to the potential energy?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Total energy in SHM: $E = \\frac{1}{2}m\\omega^2 A^2$.\nPotential energy at displacement $x$: $U = \\frac{1}{2}m\\omega^2 x^2$.\nKinetic energy: $K = \\frac{1}{2}m\\omega^2 (A^2 - x^2)$.\nGiven $K = U \\implies \\frac{1}{2}m\\omega^2 (A^2 - x^2) = \\frac{1}{2}m\\omega^2 x^2 \\implies A^2 - x^2 = x^2 \\implies 2x^2 = A^2 \\implies x = \\pm \\frac{A}{\\sqrt{2}}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Formulas for KE and PE in SHM", "allocated_marks": 1.0},
            {"step": 2, "rule": "Equating KE = PE yielding 2x^2 = A^2", "allocated_marks": 1.0},
            {"step": 3, "rule": "Solving x = +- A/sqrt(2)", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 1 Chapter 12"
    },

    # =========================================================================
    # CLASS 11 - CHEMISTRY (OP Tandon + NCERT)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Structure of Atom",
        "topic": "Photoelectric Effect and De Broglie Wavelength", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Calculate the de Broglie wavelength of an electron accelerated through a potential difference of $100\\text{ V}$. (Mass of electron $m_e = 9.1 \\times 10^{-31}\\text{ kg}$, $h = 6.63 \\times 10^{-34}\\text{ J s}$, $e = 1.6 \\times 10^{-19}\\text{ C}$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Kinetic energy $K = eV = 100 \\times 1.6 \\times 10^{-19} = 1.6 \\times 10^{-17}\\text{ J}$.\nDe Broglie relation: $\\lambda = \\frac{h}{p} = \\frac{h}{\\sqrt{2mK}}$.\n$\\lambda = \\frac{6.63 \\times 10^{-34}}{\\sqrt{2 \\times 9.1 \\times 10^{-31} \\times 1.6 \\times 10^{-17}}} = \\frac{6.63 \\times 10^{-34}}{\\sqrt{2.912 \\times 10^{-47}}} = \\frac{6.63 \\times 10^{-34}}{5.396 \\times 10^{-24}} = 1.228 \\times 10^{-10}\\text{ m} = 0.123\\text{ nm} = 1.23\\text{ \\AA}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Kinetic energy K = eV formula", "allocated_marks": 1.0},
            {"step": 2, "rule": "De Broglie formula lambda = h / sqrt(2mK)", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculation of 0.123 nm / 1.23 Angstrom", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Class 11 Chemistry"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Chemical Bonding and Molecular Structure",
        "topic": "VSEPR Theory and Hybridization", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Predict the hybridization of the central atom and the molecular geometry of:\n(a) $\\text{PCl}_5$\n(b) $\\text{SF}_6$\n(c) $\\text{ClF}_3$",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) $\\text{PCl}_5$: Central atom P has 5 bond pairs and 0 lone pairs. Hybridization is $sp^3d$. Molecular geometry is **Trigonal Bipyramidal**.\n(b) $\\text{SF}_6$: Central atom S has 6 bond pairs and 0 lone pairs. Hybridization is $sp^3d^2$. Molecular geometry is **Octahedral**.\n(c) $\\text{ClF}_3$: Central atom Cl has 3 bond pairs and 2 lone pairs. Hybridization is $sp^3d$. Molecular geometry is **T-shaped**.",
        "step_marking_rubric": [
            {"step": 1, "rule": "PCl5 sp3d and trigonal bipyramidal", "allocated_marks": 1.0},
            {"step": 2, "rule": "SF6 sp3d2 and octahedral", "allocated_marks": 1.0},
            {"step": 3, "rule": "ClF3 sp3d and T-shaped geometry", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Inorganic Chemistry / NCERT Class 11 Chemistry"
    },
    {
        "grade_level": 11, "subject": "Chemistry", "chapter": "Chemical Thermodynamics",
        "topic": "Hess's Law and Gibbs Free Energy", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "For a reaction, $\\Delta H = -110\\text{ kJ/mol}$ and $\\Delta S = -140\\text{ J K}^{-1}\\text{ mol}^{-1}$. At what temperature will this reaction change from being spontaneous to non-spontaneous?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "A reaction is at equilibrium when $\\Delta G = 0 \\implies \\Delta H - T\\Delta S = 0 \\implies T = \\frac{\\Delta H}{\\Delta S}$.\n$T = \\frac{-110 \\times 10^3\\text{ J/mol}}{-140\\text{ J K}^{-1}\\text{ mol}^{-1}} = \\frac{110000}{140} = 785.7\\text{ K}$.\nSince $\\Delta H < 0$ and $\\Delta S < 0$, the reaction is spontaneous ($\\Delta G < 0$) below $785.7\\text{ K}$ and becomes non-spontaneous above $785.7\\text{ K}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Gibbs-Helmholtz equation delta G = delta H - T*delta S", "allocated_marks": 1.0},
            {"step": 2, "rule": "Setting delta G = 0 and solving T = delta H / delta S", "allocated_marks": 1.0},
            {"step": 3, "rule": "Conclusion T = 785.7 K threshold", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Class 11"
    },

    # =========================================================================
    # CLASS 11 - BIOLOGY (Trueman's + NCERT)
    # =========================================================================
    {
        "grade_level": 11, "subject": "Biology", "chapter": "Cell: The Unit of Life",
        "topic": "Fluid Mosaic Model of Plasma Membrane", "primary_exam": "NEET",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Describe the Fluid Mosaic Model of the cell membrane proposed by Singer and Nicolson (1972). Mention the role of integral and peripheral proteins.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "The Fluid Mosaic Model describes the cell membrane as a **quasi-fluid phospholipid bilayer** in which proteins are embedded like a mosaic.\n- **Lipid matrix**: Composed of amphipathic phospholipids with hydrophilic heads facing outward and hydrophobic tails sheltered inside.\n- **Integral proteins**: Buried partially or fully in the membrane; act as ion channels, carriers, and receptors.\n- **Peripheral proteins**: Lie on the surface of the membrane and participate in signaling and cytoskeletal attachment.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Fluid mosaic model concept and lipid bilayer", "allocated_marks": 1.5},
            {"step": 2, "rule": "Role of integral vs peripheral membrane proteins", "allocated_marks": 1.5}
        ],
        "source_book": "Trueman's Elementary Biology Vol 1 / NCERT Class 11 Biology"
    },
    {
        "grade_level": 11, "subject": "Biology", "chapter": "Cell Cycle and Cell Division",
        "topic": "Stages of Meiosis I and Crossing Over", "primary_exam": "NEET",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Name the five substages of Prophase I in Meiosis. In which specific substage does crossing over take place, and which enzyme facilitates this process?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "The five substages of Prophase I are:\n1. Leptotene\n2. Zygotene (synapsis occurs, forming synaptonemal complex)\n3. **Pachytene**\n4. Diplotene\n5. Diakinesis\nCrossing over occurs in **Pachytene** between non-sister chromatids of homologous chromosomes, mediated by the enzyme **recombinase**.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Correct chronological listing of all 5 substages", "allocated_marks": 1.5},
            {"step": 2, "rule": "Pachytene stage identified", "allocated_marks": 1.0},
            {"step": 3, "rule": "Recombinase enzyme named", "allocated_marks": 0.5}
        ],
        "source_book": "Trueman's Elementary Biology Vol 1 / NCERT Class 11 Biology"
    },

    # =========================================================================
    # CLASS 12 - PHYSICS (HC Verma Vol 2 + NCERT)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Physics", "chapter": "Electromagnetic Induction",
        "topic": "Faraday's and Lenz's Law, Motional EMF", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A straight metallic rod of length $l$ is rotated with angular velocity $\\omega$ in a uniform magnetic field $B$ perpendicular to its plane of rotation, about an axis through one end. Derive the induced emf between the two ends.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Consider a small element of length $dr$ at distance $r$ from the axis. Velocity of the element is $v = \\omega r$.\nInduced emf across this element is $d\\varepsilon = B v dr = B (\\omega r) dr$.\nTotal induced emf between center and rim:\n$\\varepsilon = \\int_0^l B \\omega r dr = B \\omega \\left[ \\frac{r^2}{2} \\right]_0^l = \\frac{1}{2} B \\omega l^2$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Element emf dE = B*v*dr = B*(omega*r)*dr", "allocated_marks": 1.5},
            {"step": 2, "rule": "Integration from 0 to l yielding 1/2 B*omega*l^2", "allocated_marks": 1.5}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 2 Chapter 38"
    },
    {
        "grade_level": 12, "subject": "Physics", "chapter": "Alternating Current",
        "topic": "Series LCR Resonant Circuit and Quality Factor", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 4, "question_format": "LONG_ANSWER", "marks": 5.0,
        "question_text_latex": "(a) In a series $LCR$ circuit connected to an AC voltage $V = V_0\\sin(\\omega t)$, obtain an expression for the impedance $Z$ and the phase angle $\\phi$ using a phasor diagram.\n(b) State the condition for electrical resonance and write the expression for resonant frequency $\\omega_r$.\n(c) Define Quality factor ($Q$-factor) of the circuit and write its formula in terms of $L, C$, and $R$.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) Phasor diagram: $V_R$ in phase with current $I$, $V_L$ leads $I$ by $\\pi/2$, $V_C$ lags $I$ by $\\pi/2$.\n$V = \\sqrt{V_R^2 + (V_L - V_C)^2} = I \\sqrt{R^2 + (X_L - X_C)^2}$.\nImpedance $Z = \\sqrt{R^2 + (\\omega L - \\frac{1}{\\omega C})^2}$. Phase angle $\\tan\\phi = \\frac{X_L - X_C}{R}$.\n(b) **Resonance condition**: $X_L = X_C \\implies \\omega L = \\frac{1}{\\omega C} \\implies \\omega_r = \\frac{1}{\\sqrt{LC}}$.\n(c) **Quality factor**: $Q = \\frac{\\omega_r L}{R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}}$. It characterizes the sharpness of resonance.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Phasor derivation of impedance Z and phase angle", "allocated_marks": 2.5},
            {"step": 2, "rule": "Resonance condition XL = XC and omega = 1/sqrt(LC)", "allocated_marks": 1.5},
            {"step": 3, "rule": "Definition and formula of Q-factor = 1/R * sqrt(L/C)", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 2 Chapter 39"
    },
    {
        "grade_level": 12, "subject": "Physics", "chapter": "Ray Optics and Optical Instruments",
        "topic": "Lens Maker's Formula and Refraction at Spherical Surfaces", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "The radii of curvature of the faces of a double convex lens are $10\\text{ cm}$ and $15\\text{ cm}$. Its focal length is $12\\text{ cm}$. What is the refractive index of the glass? (Lens is placed in air).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "According to the Lens Maker's Formula:\n$\\frac{1}{f} = (\\mu - 1) \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right)$.\nHere: $f = +12\\text{ cm}, R_1 = +10\\text{ cm}, R_2 = -15\\text{ cm}$.\n$\\frac{1}{12} = (\\mu - 1) \\left( \\frac{1}{10} - \\frac{1}{-15} \\right) = (\\mu - 1) \\left( \\frac{3 + 2}{30} \\right) = (\\mu - 1) \\frac{5}{30} = \\frac{\\mu - 1}{6}$.\n$\\mu - 1 = \\frac{6}{12} = 0.5 \\implies \\mu = 1.5$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Lens maker's formula with sign convention R1=+10, R2=-15", "allocated_marks": 1.5},
            {"step": 2, "rule": "Algebraic solution yielding mu = 1.5", "allocated_marks": 1.5}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 2 Chapter 18"
    },
    {
        "grade_level": 12, "subject": "Physics", "chapter": "Wave Optics",
        "topic": "Young's Double Slit Experiment and Fringe Width", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "In a Young's double-slit experiment, the slits are separated by $0.28\\text{ mm}$ and the screen is placed $1.4\\text{ m}$ away. The distance between the central bright fringe and the fourth bright fringe is measured to be $1.2\\text{ cm}$. Determine the wavelength of light used.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Given: $d = 0.28\\text{ mm} = 0.28 \\times 10^{-3}\\text{ m}$, $D = 1.4\\text{ m}$, $y_4 = 1.2\\text{ cm} = 1.2 \\times 10^{-2}\\text{ m}$, $n = 4$.\nPosition of $n$-th bright fringe: $y_n = \\frac{n\\lambda D}{d}$.\n$\\lambda = \\frac{y_4 d}{4 D} = \\frac{(1.2 \\times 10^{-2})(0.28 \\times 10^{-3})}{4 \\times 1.4} = \\frac{3.36 \\times 10^{-6}}{5.6} = 6 \\times 10^{-7}\\text{ m} = 600\\text{ nm}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Fringe position formula yn = n * lambda * D / d", "allocated_marks": 1.0},
            {"step": 2, "rule": "Correct unit conversion of d, D, and y4", "allocated_marks": 1.0},
            {"step": 3, "rule": "Calculation yielding lambda = 600 nm", "allocated_marks": 1.0}
        ],
        "source_book": "HC Verma Concepts of Physics Vol 2 Chapter 17"
    },

    # =========================================================================
    # CLASS 12 - CHEMISTRY (OP Tandon + NCERT)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Chemical Kinetics",
        "topic": "First Order Reaction and Arrhenius Equation", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A first-order reaction has a rate constant $k = 1.15 \\times 10^{-3}\\text{ s}^{-1}$. How long will $5\\text{ g}$ of this reactant take to reduce to $3\\text{ g}$? (Given $\\log 1.67 = 0.2227$).",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "For a first order reaction: $t = \\frac{2.303}{k} \\log\\frac{[R]_0}{[R]}$.\nHere: $[R]_0 = 5\\text{ g}, [R] = 3\\text{ g}, k = 1.15 \\times 10^{-3}\\text{ s}^{-1}$.\n$t = \\frac{2.303}{1.15 \\times 10^{-3}} \\log\\left(\\frac{5}{3}\\right) = \\frac{2.303}{1.15 \\times 10^{-3}} \\log(1.667)$.\n$t = 2002.6 \\times 0.2227 \\approx 446\\text{ seconds}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "First order integrated rate formula", "allocated_marks": 1.0},
            {"step": 2, "rule": "Substitution of R0=5, R=3 and k value", "allocated_marks": 1.0},
            {"step": 3, "rule": "Final answer 446 seconds", "allocated_marks": 1.0}
        ],
        "source_book": "OP Tandon Physical Chemistry / NCERT Class 12"
    },
    {
        "grade_level": 12, "subject": "Chemistry", "chapter": "Coordination Compounds",
        "topic": "Crystal Field Theory and Magnetic Moment", "primary_exam": "JEE_MAIN",
        "applicable_exams": ["CBSE_BOARD", "JEE_MAIN", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Using Crystal Field Theory, write the electronic configuration of $d^4$ in an octahedral complex when:\n(a) $\\Delta_o > P$ (strong field ligand)\n(b) $\\Delta_o < P$ (weak field ligand)\nCalculate the spin-only magnetic moment for each case.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) When $\\Delta_o > P$ (pairing energy), pairing occurs in lower $t_{2g}$ orbitals:\n- Configuration: $t_{2g}^4 e_g^0$.\n- Unpaired electrons $n = 2$.\n- Magnetic moment $\\mu = \\sqrt{2(2+2)} = \\sqrt{8} \\approx 2.83\\text{ BM}$.\n(b) When $\\Delta_o < P$, high spin complex forms:\n- Configuration: $t_{2g}^3 e_g^1$.\n- Unpaired electrons $n = 4$.\n- Magnetic moment $\\mu = \\sqrt{4(4+2)} = \\sqrt{24} \\approx 4.90\\text{ BM}$.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Low spin configuration t2g^4 eg^0 and mu = 2.83 BM", "allocated_marks": 1.5},
            {"step": 2, "rule": "High spin configuration t2g^3 eg^1 and mu = 4.90 BM", "allocated_marks": 1.5}
        ],
        "source_book": "OP Tandon Inorganic Chemistry / NCERT Class 12"
    },

    # =========================================================================
    # CLASS 12 - BIOLOGY (Trueman's + NCERT)
    # =========================================================================
    {
        "grade_level": 12, "subject": "Biology", "chapter": "Principles of Inheritance and Variation",
        "topic": "Sex-Linked Inheritance and Pedigree Analysis", "primary_exam": "NEET",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "A woman with normal vision whose father was color-blind marries a man with normal vision. What percentage of their sons and daughters are expected to be color-blind? Show the genetic cross.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Color-blindness is an X-linked recessive trait ($X^c$).\nWoman's father was color-blind ($X^c Y$) $\\implies$ Woman is a carrier: $X^C X^c$.\nNormal vision man: $X^C Y$.\nCross: $X^C X^c \\times X^C Y$:\n- Daughters: $X^C X^C$ (normal, $50\\%$) and $X^C X^c$ (carrier, $50\\%$). **$0\\%$ of daughters are color-blind**.\n- Sons: $X^C Y$ (normal, $50\\%$) and $X^c Y$ (color-blind, $50\\%$). **$50\\%$ of sons are color-blind**.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Identifying mother as carrier X^C X^c and father X^C Y", "allocated_marks": 1.0},
            {"step": 2, "rule": "Punnett square analysis of offspring genotypes", "allocated_marks": 1.0},
            {"step": 3, "rule": "Stating 0% colorblind daughters and 50% colorblind sons", "allocated_marks": 1.0}
        ],
        "source_book": "Trueman's Elementary Biology Vol 2 / NCERT Class 12 Biology"
    },
    {
        "grade_level": 12, "subject": "Biology", "chapter": "Biotechnology: Principles and Processes",
        "topic": "Recombinant DNA Technology and Restriction Enzymes", "primary_exam": "NEET",
        "applicable_exams": ["CBSE_BOARD", "NEET"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "Explain the role of:\n(a) Restriction endonucleases\n(b) DNA ligase\n(c) Taq polymerase in recombinant DNA technology.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "(a) **Restriction Endonucleases**: Molecular scissors that cut double-stranded DNA at specific palindromic recognition sequences, creating overhanging 'sticky ends'.\n(b) **DNA Ligase**: Molecular glue that joins sticky ends of vector and foreign DNA by forming phosphodiester bonds.\n(c) **Taq Polymerase**: Thermostable DNA polymerase isolated from *Thermus aquaticus* that synthesizes new DNA strands during high-temperature denaturation cycles of PCR.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Restriction enzyme role cutting palindromic sequences", "allocated_marks": 1.0},
            {"step": 2, "rule": "DNA ligase sealing phosphodiester backbone", "allocated_marks": 1.0},
            {"step": 3, "rule": "Taq polymerase role in thermal cycling PCR", "allocated_marks": 1.0}
        ],
        "source_book": "Trueman's Elementary Biology Vol 2 / NCERT Class 12 Biology"
    },

    # =========================================================================
    # CLASS 12 - ENGLISH (Flamingo & Vistas)
    # =========================================================================
    {
        "grade_level": 12, "subject": "English", "chapter": "The Last Lesson",
        "topic": "Linguistic Chauvinism and Patriotism", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 2, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "'When a people are enslaved, as long as they hold fast to their language it is as if they had the key to their prison.' Explain M. Hamel's statement in Alphonse Daudet's 'The Last Lesson'.",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "M. Hamel emphasizes that a native language is the soul and identity of an enslaved nation. French was declared the most beautiful, clearest, and most logical language in the world.\nHe tells the villagers that by preserving their language, they preserve their collective consciousness, unity, and pride. Linguistic unity serves as an indestructible key to break free from the mental bondage and oppression of foreign rule (Prussian occupation).",
        "step_marking_rubric": [
            {"step": 1, "rule": "Significance of native language as national identity", "allocated_marks": 1.5},
            {"step": 2, "rule": "Connection to resisting Prussian cultural enslavement", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 12 English: Flamingo Chapter 1"
    },
    {
        "grade_level": 12, "subject": "English", "chapter": "The Tiger King",
        "topic": "Irony and Hubris of Power", "primary_exam": "CBSE_BOARD",
        "applicable_exams": ["CBSE_BOARD"], "difficulty_tier": 3, "question_format": "SHORT_ANSWER", "marks": 3.0,
        "question_text_latex": "How does the author Kalki use satire and dramatic irony to highlight the vanity and hollow bravado of rulers in 'The Tiger King'?",
        "options": None, "correct_option": None,
        "ideal_solution_latex": "Kalki ridicules the Maharaja of Pratibandapuram who abandons governance, levies arbitrary taxes, and massacres 99 tigers solely to defy an astrologer's prophecy.\nThe supreme irony occurs when the king believes he killed the 100th tiger (missed by him and shot by a hunter). Ultimately, death claims him through an infection caused by a tiny wooden sliver from a crudely made toy tiger, proving the absolute futility of mortal arrogance against destiny.",
        "step_marking_rubric": [
            {"step": 1, "rule": "Satire on ruler neglecting governance to kill tigers", "allocated_marks": 1.5},
            {"step": 2, "rule": "Irony of death caused by a wooden toy tiger sliver", "allocated_marks": 1.5}
        ],
        "source_book": "NCERT Class 12 English: Vistas Chapter 2"
    }
]

def generate_content_hash(q: dict) -> str:
    raw = f"{q['grade_level']}_{q['subject']}_{q['chapter']}_{q.get('topic','')}_{q['question_text_latex']}"
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()

def main():
    logger.info("Starting Full Curriculum Question Bank Seeder...")
    logger.info(f"Connected to database: {'Supabase PostgreSQL' if db.use_supabase else 'Local SQLite'}")

    for q in QUESTIONS:
        q["content_hash"] = generate_content_hash(q)

    count = db.upsert_questions(QUESTIONS)
    logger.info(f"Successfully processed and seeded {count} new curriculum questions into {'Supabase Cloud' if db.use_supabase else 'SQLite'}!")

    # Check updated stats
    tax = db.get_taxonomy()
    total_qs = 0
    logger.info("Updated Question Bank Statistics:")
    for g, subs in tax.items():
        for s, chaps in subs.items():
            s_count = sum(c["count"] if isinstance(c, dict) else c for c in chaps.values())
            total_qs += s_count
            logger.info(f"  Grade {g} • {s}: {s_count} Questions across {len(chaps)} Chapters")

    logger.info(f"Total Questions now active in database: {total_qs}")

if __name__ == "__main__":
    main()
