"""
Harmonic Spiral Map Generator (Intuitive Octave Guide)
Scalar Relaxation Cosmology - Atomic Harmonics Module

All 118 elements on fixed radial steps with labeled octave rings.
Includes a plain-English guide in the side panel for non-physicists.

Usage:
    python3 harmonic_spiral_map.py
"""

import matplotlib
matplotlib.use("Agg")  # Headless-safe
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os

# ---------------------------------------------------------------
# THE 6 MECHANICAL ARCHETYPES (Color Key)
# ---------------------------------------------------------------
ARCHETYPES = {
    "BLUE":  "#1565C0",   # Primary Boundary Shedder (+)
    "LBLUE": "#4FC3F7",   # Secondary Boundary Shedder (2+)
    "GREEN": "#2E7D32",   # Structural Hub (0)
    "RED":   "#C62828",   # High Aether Sink (-)
    "WHITE": "#B0BEC5",   # Harmonic Zero (0) - inert
    "GOLD":  "#F9A825",   # Core Transition Tensor
}

# ---------------------------------------------------------------
# ALL 118 ELEMENTS (Z 1 -> 118)
# ---------------------------------------------------------------
SYMBOLS = [
    "H","He","Li","Be","B","C","N","O","F","Ne",
    "Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
    "Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
    "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr",
    "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",
    "Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
    "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
    "Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
    "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",
    "Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
    "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds",
    "Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og",
]
assert len(SYMBOLS) == 118

NOBLE      = {2, 10, 18, 36, 54, 86, 118}
ALKALI     = {3, 11, 19, 37, 55, 87}
ALKEARTH   = {4, 12, 20, 38, 56, 88}
HALOGEN    = {9, 17, 35, 53, 85, 117}
NONMETAL   = {1, 6, 7, 8, 15, 16, 34, 52}
STRUCTURAL = {5, 14, 32, 33, 51}

def archetype(z):
    if z in NOBLE:      return "WHITE"
    if z in ALKALI:     return "BLUE"
    if z in ALKEARTH:   return "LBLUE"
    if z in HALOGEN:    return "RED"
    if z in NONMETAL:   return "RED" if z != 6 else "GREEN"
    if z in STRUCTURAL: return "GREEN"
    return "GOLD"

def polarity_mark(z):
    if z in NOBLE:          return ""
    if z in ALKALI:         return "\u207A"
    if z in ALKEARTH:       return "\u00B2\u207A"
    if z in HALOGEN:        return "\u207B"
    if z in (8, 16, 34, 52): return "\u00B2\u207B"
    if z in (7, 15):        return "\u00B3\u207B"
    if z == 1:              return "\u207B"
    if z in (5, 14, 32, 33, 51): return ""
    return "\u1D57"

# ---------------------------------------------------------------
# FIXED-STEP PLACEMENT
# ---------------------------------------------------------------
Z_MAX   = 118
R_START = 2.0
R_STEP  = 0.072
TURNS   = 7.0
DTHETA  = TURNS * 2 * np.pi / Z_MAX

def spiral_point(z):
    theta = (z - 1) * DTHETA
    r = R_START + (z - 1) * R_STEP
    return r * np.cos(theta), r * np.sin(theta), r, theta

# ---------------------------------------------------------------
# FIGURE (Slightly wider side panel to fit guide text)
# ---------------------------------------------------------------
fig = plt.figure(figsize=(18, 14), facecolor="black")
gs = gridspec.GridSpec(1, 2, width_ratios=[3.2, 1.3],
                       wspace=0.03, figure=fig)

ax = fig.add_subplot(gs[0])
ax.set_facecolor("black")
axl = fig.add_subplot(gs[1])
axl.set_facecolor("black")

# --- Octave closure rings + LABELS ---
octave_labels = ["O1:He", "O2:Ne", "O3:Ar", "O4:Kr",
                 "O5:Xe", "O6:Rn", "O7:Og"]
label_angle = np.radians(118)
for i, z_noble in enumerate(sorted(NOBLE)):
    _, _, r_ring, _ = spiral_point(z_noble)
    circle = plt.Circle((0, 0), r_ring, color="#546E7A",
                        fill=False, linewidth=1.3, linestyle="--", zorder=2)
    ax.add_patch(circle)
    lx = (r_ring + 0.28) * np.cos(label_angle)
    ly = (r_ring + 0.28) * np.sin(label_angle)
    ax.text(lx, ly, octave_labels[i], ha="center", va="center",
            fontsize=9, color="#CFD8DC", fontweight="bold", zorder=7)

# ---------------------------------------------------------------
# PLACE ALL 118 ELEMENTS
# ---------------------------------------------------------------
for z, sym in enumerate(SYMBOLS, start=1):
    x, y, r, theta = spiral_point(z)
    color = ARCHETYPES[archetype(z)]
    mark = polarity_mark(z)

    ax.scatter(x, y, s=180, c=color, edgecolors="white",
               linewidths=0.7, zorder=5)
    ax.text(x, y, f"{sym}{mark}", ha="center", va="center",
            fontsize=6.5, fontweight="bold", color="black", zorder=6)

# --- Center core ---
ax.scatter([0], [0], s=180, c="white", marker="*", zorder=4)
ax.text(0, -0.6, "CORE", ha="center", va="top",
        fontsize=8, color="white", fontweight="bold")

# --- Title ---
ax.text(0, 11.9, "HARMONIC OCTAVE MAP", ha="center",
        fontsize=17, fontweight="bold", color="white")
ax.text(0, 11.25, "Standing-Wave Nodal Radii & Element Nodes (1 -> 118)",
        ha="center", fontsize=10.5, color="#B0BEC5")

# --- Map frame ---
ax.set_xlim(-11.5, 11.5)
ax.set_ylim(-11.5, 12.5)
ax.set_aspect("equal")
ax.axis("off")

# ---------------------------------------------------------------
# LEGEND & PLAIN-ENGLISH GUIDE PANEL
# ---------------------------------------------------------------
axl.set_xlim(0, 10)
axl.set_ylim(0, 13)
axl.axis("off")

axl.text(5, 12.4, "MECHANICAL KEY", ha="center", fontsize=14,
         fontweight="bold", color="white")

legend_entries = [
    ("Primary Shedder",       "BLUE",  "+",   "Loose outer ring; sheds freely"),
    ("Secondary Shedder",     "LBLUE", "2+",  "Two outer rings; higher tension"),
    ("Structural Hub",        "GREEN", "0",   "Balanced symmetric lattice geometry"),
    ("High Aether Sink",      "RED",   "-",   "Aggressive inward boundary pull"),
    ("Harmonic Zero",         "WHITE", "0",   "Octave closure; inert / zero shear"),
    ("Core Transition Tensor","GOLD",  "t",   "Multi-octave internal torsional fold"),
]

y = 11.2
for label, key, pol, desc in legend_entries:
    axl.scatter([0.8], [y], s=260, c=ARCHETYPES[key],
                edgecolors="white", linewidths=1.2, zorder=5)
    axl.text(1.5, y, f"{label} [{pol}]", fontsize=10.5,
             color="white", fontweight="bold", va="center")
    axl.text(1.5, y - 0.42, desc, fontsize=8,
             color="#90A4AE", va="center")
    y -= 1.35

# --- Plain-English Guide Box for Non-Physicists ---
axl.text(5, 3.2, "HOW TO READ THE RINGS", ha="center", fontsize=11,
         fontweight="bold", color="#FFD54F")

guide_text = (
    "• Dashed rings = Acoustic octaves\n"
    "• Expanding outward (O1 -> O7) scales\n"
    "  the atom, packing in more boundary rings.\n"
    "• At the ring (White): Octave is full.\n"
    "  Pressure balances to zero (inert).\n"
    "• Just past a ring (Blue): A new octave\n"
    "  starts with a loose ring ready to shed.\n"
    "• Just before a ring (Red): Octave is\n"
    "  nearly full; pulls hard to grab a ring."
)
axl.text(0.4, 2.5, guide_text, fontsize=8.5, color="#ECEFF1",
         family="monospace", va="top", linespacing=1.4)

# ---------------------------------------------------------------
# SAVE
# ---------------------------------------------------------------
plt.savefig("harmonic_spiral_map.png", dpi=120, facecolor="black")
plt.savefig("harmonic_spiral_map.pdf", facecolor="black")
print("Saved: harmonic_spiral_map.png and harmonic_spiral_map.pdf")
print("PNG size: {:.1f} KB".format(
    os.path.getsize("harmonic_spiral_map.png") / 1024))

