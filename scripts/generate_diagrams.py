"""
Generates clean, precise scientific SVG diagrams for CBSE Class 10, 11, 12 Physics, Chemistry, Biology, and Math.
Saves to data/diagrams/ and frontend/public/diagrams/.
"""
from pathlib import Path
import shutil

DIAGRAMS = {}

# 1. Wheatstone Bridge
DIAGRAMS["wheatstone_bridge.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 320" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Diamond Bridge -->
  <line x1="225" y1="40" x2="100" y2="160" stroke="#1e293b" stroke-width="2.5" />
  <line x1="225" y1="40" x2="350" y2="160" stroke="#1e293b" stroke-width="2.5" />
  <line x1="100" y1="160" x2="225" y2="280" stroke="#1e293b" stroke-width="2.5" />
  <line x1="350" y1="160" x2="225" y2="280" stroke="#1e293b" stroke-width="2.5" />
  <!-- Resistor Boxes -->
  <rect x="140" y="85" width="45" height="20" rx="3" fill="#f8fafc" stroke="#2563eb" stroke-width="2" transform="rotate(-40 162 95)" />
  <text x="135" y="80" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e40af">P (10 &#937;)</text>
  <rect x="265" y="85" width="45" height="20" rx="3" fill="#f8fafc" stroke="#2563eb" stroke-width="2" transform="rotate(40 287 95)" />
  <text x="305" y="80" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e40af">Q (20 &#937;)</text>
  <rect x="140" y="215" width="45" height="20" rx="3" fill="#f8fafc" stroke="#2563eb" stroke-width="2" transform="rotate(40 162 225)" />
  <text x="135" y="255" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e40af">R (15 &#937;)</text>
  <rect x="265" y="215" width="45" height="20" rx="3" fill="#f8fafc" stroke="#dc2626" stroke-width="2" transform="rotate(-40 287 225)" />
  <text x="305" y="255" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">S = ?</text>
  <!-- Galvanometer branch -->
  <line x1="225" y1="40" x2="225" y2="135" stroke="#1e293b" stroke-width="2" />
  <circle cx="225" cy="160" r="24" fill="#eff6ff" stroke="#1e293b" stroke-width="2" />
  <text x="219" y="166" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1e293b">G</text>
  <line x1="225" y1="184" x2="225" y2="280" stroke="#1e293b" stroke-width="2" />
  <!-- Node circles -->
  <circle cx="225" cy="40" r="5" fill="#1e293b" />
  <text x="220" y="28" font-family="sans-serif" font-size="14" font-weight="bold">B</text>
  <circle cx="225" cy="280" r="5" fill="#1e293b" />
  <text x="220" y="302" font-family="sans-serif" font-size="14" font-weight="bold">D</text>
  <circle cx="100" cy="160" r="5" fill="#1e293b" />
  <text x="75" y="165" font-family="sans-serif" font-size="14" font-weight="bold">A</text>
  <circle cx="350" cy="160" r="5" fill="#1e293b" />
  <text x="362" y="165" font-family="sans-serif" font-size="14" font-weight="bold">C</text>
  <!-- External Battery circuit -->
  <path d="M 100 160 L 50 160 L 50 300 L 400 300 L 400 160 L 350 160" fill="none" stroke="#1e293b" stroke-width="2" />
  <!-- Battery symbol -->
  <line x1="215" y1="290" x2="215" y2="310" stroke="#1e293b" stroke-width="3" />
  <line x1="230" y1="295" x2="230" y2="305" stroke="#1e293b" stroke-width="1.5" />
  <text x="200" y="285" font-family="sans-serif" font-size="13" font-weight="bold">+</text>
  <text x="235" y="285" font-family="sans-serif" font-size="13" font-weight="bold">-</text>
  <text x="215" y="318" font-family="sans-serif" font-size="11" fill="#475569">E = 6 V</text>
</svg>"""

# 2. Resistors Series-Parallel Mixed Circuit
DIAGRAMS["resistors_series_parallel.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 240" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Circuit Wires -->
  <line x1="50" y1="120" x2="110" y2="120" stroke="#1e293b" stroke-width="2" />
  <!-- Resistor R1 -->
  <rect x="110" y="110" width="50" height="20" fill="#eff6ff" stroke="#2563eb" stroke-width="2" rx="2" />
  <text x="120" y="103" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e40af">R1 = 4 &#937;</text>
  <!-- Parallel junction -->
  <line x1="160" y1="120" x2="200" y2="120" stroke="#1e293b" stroke-width="2" />
  <line x1="200" y1="120" x2="200" y2="60" stroke="#1e293b" stroke-width="2" />
  <line x1="200" y1="120" x2="200" y2="180" stroke="#1e293b" stroke-width="2" />
  <circle cx="200" cy="120" r="4" fill="#1e293b" />
  <!-- Top Branch R2 -->
  <line x1="200" y1="60" x2="230" y2="60" stroke="#1e293b" stroke-width="2" />
  <rect x="230" y="50" width="50" height="20" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" rx="2" />
  <text x="238" y="43" font-family="sans-serif" font-size="12" font-weight="bold" fill="#166534">R2 = 6 &#937;</text>
  <line x1="280" y1="60" x2="310" y2="60" stroke="#1e293b" stroke-width="2" />
  <!-- Bottom Branch R3 -->
  <line x1="200" y1="180" x2="230" y2="180" stroke="#1e293b" stroke-width="2" />
  <rect x="230" y="170" width="50" height="20" fill="#fef2f2" stroke="#dc2626" stroke-width="2" rx="2" />
  <text x="238" y="206" font-family="sans-serif" font-size="12" font-weight="bold" fill="#991b1b">R3 = 12 &#937;</text>
  <line x1="280" y1="180" x2="310" y2="180" stroke="#1e293b" stroke-width="2" />
  <!-- Rejoin parallel branch -->
  <line x1="310" y1="60" x2="310" y2="180" stroke="#1e293b" stroke-width="2" />
  <circle cx="310" cy="120" r="4" fill="#1e293b" />
  <line x1="310" y1="120" x2="380" y2="120" stroke="#1e293b" stroke-width="2" />
  <!-- Ammeter -->
  <circle cx="350" cy="120" r="14" fill="#ffffff" stroke="#1e293b" stroke-width="2" />
  <text x="345" y="125" font-family="sans-serif" font-size="13" font-weight="bold">A</text>
  <!-- Outer loop return -->
  <line x1="380" y1="120" x2="410" y2="120" stroke="#1e293b" stroke-width="2" />
  <line x1="410" y1="120" x2="410" y2="220" stroke="#1e293b" stroke-width="2" />
  <line x1="410" y1="220" x2="50" y2="220" stroke="#1e293b" stroke-width="2" />
  <line x1="50" y1="220" x2="50" y2="120" stroke="#1e293b" stroke-width="2" />
  <!-- Battery on bottom line -->
  <line x1="215" y1="210" x2="215" y2="230" stroke="#1e293b" stroke-width="3" />
  <line x1="225" y1="215" x2="225" y2="225" stroke="#1e293b" stroke-width="1.5" />
  <text x="202" y="208" font-family="sans-serif" font-size="12" font-weight="bold">+</text>
  <text x="230" y="208" font-family="sans-serif" font-size="12" font-weight="bold">-</text>
  <text x="210" y="238" font-family="sans-serif" font-size="11" fill="#475569">V = 12 V</text>
</svg>"""

# 3. Ray Optics: Triangular Prism Refraction
DIAGRAMS["ray_optics_prism.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 300" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Glass Prism Triangle -->
  <polygon points="225,40 100,240 350,240" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5" />
  <text x="220" y="32" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0369a1">A</text>
  <text x="85" y="250" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0369a1">B</text>
  <text x="355" y="250" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0369a1">C</text>
  <!-- Incident Ray PE -->
  <line x1="40" y1="180" x2="155" y2="152" stroke="#dc2626" stroke-width="2.5" />
  <!-- Arrow on incident ray -->
  <polygon points="95,163 103,165 98,171" fill="#dc2626" />
  <text x="35" y="172" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">Incident Ray</text>
  <!-- Refracted Ray EF -->
  <line x1="155" y1="152" x2="280" y2="152" stroke="#dc2626" stroke-width="2.5" />
  <polygon points="220,152 212,148 212,156" fill="#dc2626" />
  <!-- Emergent Ray FS -->
  <line x1="280" y1="152" x2="400" y2="200" stroke="#dc2626" stroke-width="2.5" />
  <polygon points="345,178 337,172 341,182" fill="#dc2626" />
  <text x="350" y="218" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">Emergent Ray</text>
  <!-- Normal at AB -->
  <line x1="120" y1="110" x2="200" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4" />
  <text x="110" y="105" font-family="sans-serif" font-size="11" fill="#64748b">N1</text>
  <!-- Normal at AC -->
  <line x1="320" y1="110" x2="240" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4" />
  <text x="325" y="105" font-family="sans-serif" font-size="11" fill="#64748b">N2</text>
  <!-- Angle of Deviation Delta -->
  <line x1="155" y1="152" x2="310" y2="115" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" />
  <line x1="280" y1="152" x2="230" y2="132" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" />
  <text x="270" y="125" font-family="sans-serif" font-size="13" font-weight="bold" fill="#7c3aed">&#948; (Deviation)</text>
  <text x="125" y="145" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">i</text>
  <text x="295" y="145" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">e</text>
</svg>"""

# 4. Convex Lens Ray Diagram (Real, Inverted Image)
DIAGRAMS["convex_lens_ray_diagram.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Principal Axis -->
  <line x1="20" y1="120" x2="480" y2="120" stroke="#334155" stroke-width="1.5" />
  <!-- Convex Lens Silhouette -->
  <path d="M 250 30 Q 265 120 250 210 Q 235 120 250 30 Z" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" />
  <line x1="250" y1="20" x2="250" y2="220" stroke="#0284c7" stroke-width="1" stroke-dasharray="3,3" />
  <!-- Focus markers -->
  <circle cx="250" cy="120" r="3" fill="#1e293b" />
  <text x="246" y="136" font-family="sans-serif" font-size="11" font-weight="bold">O</text>
  <circle cx="180" cy="120" r="3" fill="#1e293b" />
  <text x="174" y="136" font-family="sans-serif" font-size="11" font-weight="bold">F1</text>
  <circle cx="110" cy="120" r="3" fill="#1e293b" />
  <text x="100" y="136" font-family="sans-serif" font-size="11" font-weight="bold">2F1</text>
  <circle cx="320" cy="120" r="3" fill="#1e293b" />
  <text x="314" y="136" font-family="sans-serif" font-size="11" font-weight="bold">F2</text>
  <circle cx="390" cy="120" r="3" fill="#1e293b" />
  <text x="382" y="136" font-family="sans-serif" font-size="11" font-weight="bold">2F2</text>
  <!-- Object AB between F1 and 2F1 -->
  <line x1="140" y1="120" x2="140" y2="70" stroke="#dc2626" stroke-width="3" />
  <polygon points="140,65 136,75 144,75" fill="#dc2626" />
  <text x="132" y="60" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">A (Object)</text>
  <text x="135" y="136" font-family="sans-serif" font-size="11" font-weight="bold">B</text>
  <!-- Parallel Ray to Lens and through F2 -->
  <line x1="140" y1="70" x2="250" y2="70" stroke="#2563eb" stroke-width="1.8" />
  <line x1="250" y1="70" x2="430" y2="185" stroke="#2563eb" stroke-width="1.8" />
  <!-- Ray through Optical Centre O -->
  <line x1="140" y1="70" x2="430" y2="185" stroke="#16a34a" stroke-width="1.8" />
  <!-- Inverted Real Image A'B' beyond 2F2 -->
  <line x1="430" y1="120" x2="430" y2="185" stroke="#9333ea" stroke-width="3" />
  <polygon points="430,190 426,180 434,180" fill="#9333ea" />
  <text x="415" y="205" font-family="sans-serif" font-size="12" font-weight="bold" fill="#9333ea">A' (Image)</text>
  <text x="425" y="115" font-family="sans-serif" font-size="11" font-weight="bold">B'</text>
</svg>"""

# 5. Logic Gates Circuit (NAND + NOR combination)
DIAGRAMS["logic_gates_circuit.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Inputs A and B -->
  <line x1="40" y1="65" x2="110" y2="65" stroke="#1e293b" stroke-width="2" />
  <text x="25" y="70" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">A</text>
  <line x1="40" y1="95" x2="110" y2="95" stroke="#1e293b" stroke-width="2" />
  <text x="25" y="100" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">B</text>
  <!-- NAND Gate 1 -->
  <path d="M 110 50 L 140 50 A 30 30 0 0 1 140 110 L 110 110 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
  <circle cx="174" cy="80" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
  <text x="120" y="85" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e40af">NAND</text>
  <!-- Intermediate wire Y1 -->
  <line x1="178" y1="80" x2="250" y2="80" stroke="#1e293b" stroke-width="2" />
  <text x="200" y="72" font-family="sans-serif" font-size="12" font-weight="bold" fill="#475569">Y1</text>
  <!-- Input C -->
  <line x1="40" y1="150" x2="250" y2="150" stroke="#1e293b" stroke-width="2" />
  <text x="25" y="155" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">C</text>
  <!-- NOR Gate 2 -->
  <path d="M 250 65 Q 265 115 250 165 Q 285 165 310 115 Q 285 65 250 65 Z" fill="#fef2f2" stroke="#dc2626" stroke-width="2" />
  <circle cx="314" cy="115" r="4" fill="#ffffff" stroke="#dc2626" stroke-width="2" />
  <text x="265" y="120" font-family="sans-serif" font-size="11" font-weight="bold" fill="#991b1b">NOR</text>
  <!-- Final Output Y -->
  <line x1="318" y1="115" x2="400" y2="115" stroke="#1e293b" stroke-width="2.5" />
  <text x="410" y="120" font-family="sans-serif" font-size="15" font-weight="bold" fill="#15803d">Y (Output)</text>
</svg>"""

# 6. Galvanic / Daniell Cell (Chemistry)
DIAGRAMS["galvanic_cell.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 280" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Left Beaker (Anode) Zn -->
  <rect x="50" y="110" width="130" height="130" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="2" />
  <rect x="52" y="145" width="126" height="93" rx="4" fill="#e2e8f0" opacity="0.6" />
  <rect x="95" y="70" width="25" height="110" fill="#94a3b8" stroke="#475569" stroke-width="2" />
  <text x="80" y="60" font-family="sans-serif" font-size="12" font-weight="bold" fill="#334155">Zn Anode (-)</text>
  <text x="65" y="225" font-family="sans-serif" font-size="11" fill="#475569">1M ZnSO4 sol.</text>
  <!-- Right Beaker (Cathode) Cu -->
  <rect x="280" y="110" width="130" height="130" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="2" />
  <rect x="282" y="145" width="126" height="93" rx="4" fill="#bae6fd" opacity="0.7" />
  <rect x="330" y="70" width="25" height="110" fill="#ea580c" stroke="#c2410c" stroke-width="2" />
  <text x="315" y="60" font-family="sans-serif" font-size="12" font-weight="bold" fill="#c2410c">Cu Cathode (+)</text>
  <text x="295" y="225" font-family="sans-serif" font-size="11" fill="#0369a1">1M CuSO4 sol.</text>
  <!-- Inverted U-tube Salt Bridge -->
  <path d="M 155 170 L 155 90 Q 155 80 165 80 L 295 80 Q 305 80 305 90 L 305 170" fill="none" stroke="#f59e0b" stroke-width="14" stroke-linecap="round" />
  <path d="M 155 170 L 155 90 Q 155 80 165 80 L 295 80 Q 305 80 305 90 L 305 170" fill="none" stroke="#d97706" stroke-width="2" />
  <text x="195" y="72" font-family="sans-serif" font-size="11" font-weight="bold" fill="#b45309">Salt Bridge (KCl/Agar)</text>
  <!-- External Circuit with Voltmeter -->
  <line x1="107" y1="70" x2="107" y2="25" stroke="#1e293b" stroke-width="2" />
  <line x1="107" y1="25" x2="210" y2="25" stroke="#1e293b" stroke-width="2" />
  <circle cx="230" cy="25" r="16" fill="#ffffff" stroke="#1e293b" stroke-width="2" />
  <text x="224" y="31" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">V</text>
  <line x1="246" y1="25" x2="342" y2="25" stroke="#1e293b" stroke-width="2" />
  <line x1="342" y1="25" x2="342" y2="70" stroke="#1e293b" stroke-width="2" />
  <text x="210" y="48" font-family="sans-serif" font-size="11" font-weight="bold" fill="#15803d">E&#176; = 1.10 V</text>
  <!-- Electron flow arrow -->
  <line x1="130" y1="15" x2="180" y2="15" stroke="#2563eb" stroke-width="2" />
  <polygon points="185,15 178,11 178,19" fill="#2563eb" />
  <text x="140" y="10" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb">e- flow</text>
</svg>"""

# 7. Human Heart Schematic (Biology)
DIAGRAMS["human_heart_schematic.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 300" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Heart Outline Box/Septum -->
  <rect x="130" y="50" width="200" height="200" rx="20" fill="#f8fafc" stroke="#991b1b" stroke-width="3" />
  <!-- Central Septum separating Right (deoxygenated - blue) and Left (oxygenated - red) -->
  <line x1="230" y1="50" x2="230" y2="250" stroke="#991b1b" stroke-width="5" />
  <!-- Horizontal Valve divider -->
  <line x1="130" y1="140" x2="330" y2="140" stroke="#991b1b" stroke-width="3" stroke-dasharray="6,4" />
  <!-- Right Atrium (RA) -->
  <rect x="135" y="55" width="90" height="80" rx="10" fill="#dbeafe" />
  <text x="145" y="95" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e40af">Right Atrium</text>
  <text x="155" y="112" font-family="sans-serif" font-size="10" fill="#1e3a8a">(Deox. Blood)</text>
  <!-- Right Ventricle (RV) -->
  <rect x="135" y="145" width="90" height="100" rx="10" fill="#bfdbfe" />
  <text x="142" y="195" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e40af">Right Ventricle</text>
  <text x="145" y="212" font-family="sans-serif" font-size="10" fill="#1e3a8a">&#8594; Pulm. Artery</text>
  <!-- Left Atrium (LA) -->
  <rect x="235" y="55" width="90" height="80" rx="10" fill="#fee2e2" />
  <text x="250" y="95" font-family="sans-serif" font-size="13" font-weight="bold" fill="#991b1b">Left Atrium</text>
  <text x="252" y="112" font-family="sans-serif" font-size="10" fill="#7f1d1d">(Ox. Blood)</text>
  <!-- Left Ventricle (LV - Thick walled) -->
  <rect x="235" y="145" width="90" height="100" rx="10" fill="#fca5a5" />
  <text x="245" y="195" font-family="sans-serif" font-size="13" font-weight="bold" fill="#991b1b">Left Ventricle</text>
  <text x="255" y="212" font-family="sans-serif" font-size="10" fill="#7f1d1d">&#8594; Aorta (Body)</text>
  <!-- Blood Flow Labels & Arrows -->
  <text x="30" y="90" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e40af">Vena Cava &#8594;</text>
  <text x="345" y="90" font-family="sans-serif" font-size="12" font-weight="bold" fill="#991b1b">&#8592; Pulm. Veins</text>
  <text x="200" y="280" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Interventricular Septum</text>
</svg>"""

# 8. Stomata Open vs Closed (Biology)
DIAGRAMS["stomata_diagram.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Open Stoma Left -->
  <g transform="translate(60, 20)">
    <path d="M 60 20 C 20 50 20 130 60 160 C 45 120 45 60 60 20 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2" />
    <path d="M 90 20 C 130 50 130 130 90 160 C 105 120 105 60 90 20 Z" fill="#bbf7d0" stroke="#16a34a" stroke-width="2" />
    <!-- Stomatal Pore -->
    <ellipse cx="75" cy="90" rx="12" ry="35" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5" />
    <circle cx="45" cy="80" r="4" fill="#166534" />
    <circle cx="105" cy="80" r="4" fill="#166534" />
    <text x="40" y="185" font-family="sans-serif" font-size="13" font-weight="bold" fill="#166534">(A) Open Stoma</text>
    <text x="45" y="200" font-family="sans-serif" font-size="10" fill="#475569">(Turgid Guard Cells)</text>
  </g>
  <!-- Closed Stoma Right -->
  <g transform="translate(260, 20)">
    <path d="M 68 20 C 35 50 35 130 68 160 C 60 120 60 60 68 20 Z" fill="#dcfce7" stroke="#16a34a" stroke-width="2" />
    <path d="M 82 20 C 115 50 115 130 82 160 C 90 120 90 60 82 20 Z" fill="#dcfce7" stroke="#16a34a" stroke-width="2" />
    <line x1="75" y1="25" x2="75" y2="155" stroke="#15803d" stroke-width="2" />
    <circle cx="50" cy="80" r="4" fill="#166534" />
    <circle cx="100" cy="80" r="4" fill="#166534" />
    <text x="35" y="185" font-family="sans-serif" font-size="13" font-weight="bold" fill="#166534">(B) Closed Stoma</text>
    <text x="40" y="200" font-family="sans-serif" font-size="10" fill="#475569">(Flaccid Guard Cells)</text>
  </g>
</svg>"""

# 9. Circle Tangents from External Point (Math Class 10)
DIAGRAMS["circle_tangents.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 240" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Circle with Center O -->
  <circle cx="280" cy="120" r="70" fill="#f8fafc" stroke="#2563eb" stroke-width="2.5" />
  <circle cx="280" cy="120" r="4" fill="#1e293b" />
  <text x="290" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">O (Center)</text>
  <!-- External Point P -->
  <circle cx="70" cy="120" r="5" fill="#dc2626" />
  <text x="45" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#dc2626">P</text>
  <!-- Tangent Points A and B on circle -->
  <!-- Coordinates: cos(theta) = 70/210 = 1/3 -> theta = ~70.5 deg -> x = 280 - 70*1/3 = 256.7, y = 120 - 70*sqrt(8)/3 = 54 -->
  <line x1="70" y1="120" x2="257" y2="54" stroke="#dc2626" stroke-width="2.5" />
  <circle cx="257" cy="54" r="4" fill="#dc2626" />
  <text x="255" y="42" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">A</text>
  <!-- Radius OA -->
  <line x1="280" y1="120" x2="257" y2="54" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" />
  <text x="272" y="85" font-family="sans-serif" font-size="12" fill="#0284c7">r = 5 cm</text>
  <!-- Tangent PB -->
  <line x1="70" y1="120" x2="257" y2="186" stroke="#dc2626" stroke-width="2.5" />
  <circle cx="257" cy="186" r="4" fill="#dc2626" />
  <text x="255" y="204" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">B</text>
  <!-- Radius OB -->
  <line x1="280" y1="120" x2="257" y2="186" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4" />
  <!-- Line OP connecting center to external point -->
  <line x1="70" y1="120" x2="280" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
  <text x="145" y="112" font-family="sans-serif" font-size="12" fill="#475569">OP = 13 cm</text>
  <!-- Right Angle symbol at A -->
  <polyline points="250,56 252,65 259,62" fill="none" stroke="#0284c7" stroke-width="1.5" />
</svg>"""

# 10. Trigonometric Angle of Elevation (Math)
DIAGRAMS["trigonometry_elevation.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 240" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <!-- Ground Level Line BC -->
  <line x1="60" y1="200" x2="380" y2="200" stroke="#334155" stroke-width="2" />
  <!-- Vertical Tower AB -->
  <line x1="340" y1="200" x2="340" y2="50" stroke="#1e293b" stroke-width="4" />
  <circle cx="340" cy="50" r="5" fill="#dc2626" />
  <text x="350" y="55" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">A (Tower Top)</text>
  <circle cx="340" cy="200" r="4" fill="#1e293b" />
  <text x="350" y="215" font-family="sans-serif" font-size="14" font-weight="bold">B (Base)</text>
  <!-- Observer point C -->
  <circle cx="100" cy="200" r="5" fill="#2563eb" />
  <text x="80" y="220" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">C (Observer)</text>
  <!-- Line of Sight AC -->
  <line x1="100" y1="200" x2="340" y2="50" stroke="#dc2626" stroke-width="2.5" />
  <text x="190" y="115" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">Line of Sight</text>
  <!-- Angle of Elevation theta -->
  <path d="M 140 200 A 40 40 0 0 0 134 178" fill="none" stroke="#2563eb" stroke-width="2" />
  <text x="150" y="190" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">&#952; = 60&#176;</text>
  <!-- Distance BC -->
  <text x="195" y="218" font-family="sans-serif" font-size="12" fill="#475569">d = 30 m</text>
  <!-- Tower Height h -->
  <text x="355" y="130" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e293b">h = ?</text>
  <!-- Right angle mark at B -->
  <polyline points="325,200 325,185 340,185" fill="none" stroke="#334155" stroke-width="1.5" />
</svg>"""

# 11. Default School Emblem / Logo
DIAGRAMS["default_school_logo.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <circle cx="60" cy="60" r="55" fill="#1e3a8a" stroke="#fbbf24" stroke-width="4" />
  <circle cx="60" cy="60" r="46" fill="#ffffff" />
  <!-- Open Book & Torch Emblem -->
  <path d="M 40 68 Q 60 60 60 76 Q 60 60 80 68 L 80 82 Q 60 74 60 88 Q 60 74 40 82 Z" fill="#1e3a8a" />
  <path d="M 57 32 Q 60 22 63 32 Q 68 42 60 48 Q 52 42 57 32 Z" fill="#f59e0b" />
  <!-- Ribbon / Stars -->
  <circle cx="36" cy="50" r="3" fill="#fbbf24" />
  <circle cx="84" cy="50" r="3" fill="#fbbf24" />
  <text x="60" y="103" text-anchor="middle" font-family="serif" font-size="8" font-weight="bold" fill="#1e3a8a">ESTD. 1985</text>
</svg>"""

def save_diagrams():
    data_dir = Path("data/diagrams")
    pub_dir = Path("frontend/public/diagrams")
    logo_dir = Path("data/logos")
    pub_logo_dir = Path("frontend/public/logos")

    for d in [data_dir, pub_dir, logo_dir, pub_logo_dir]:
        d.mkdir(parents=True, exist_ok=True)

    count = 0
    for name, content in DIAGRAMS.items():
        if "logo" in name:
            (logo_dir / name).write_text(content, encoding="utf-8")
            (pub_logo_dir / name).write_text(content, encoding="utf-8")
        else:
            (data_dir / name).write_text(content, encoding="utf-8")
            (pub_dir / name).write_text(content, encoding="utf-8")
        count += 1

    print(f"Successfully generated {count} scientific SVG diagrams & logos in data/ and frontend/public/!")

if __name__ == "__main__":
    save_diagrams()
