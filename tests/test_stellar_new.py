#!/usr/bin/env python3
"""
Test script for new stellar evolution phases and phenomena.
Demonstrates all new functions from stellar.py module.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.components.stellar import (
    # Existing
    star, zams, wolf_rayet, supernova,
    # Giant branch
    red_giant, RGB, asymptotic_giant_branch, AGB,
    red_supergiant, RSG, blue_supergiant, BSG,
    yellow_supergiant, YSG, horizontal_branch, HB,
    hertzsprung_gap, HG,
    # Stripped stars
    helium_star, He_star, stripped_star,
    # Exotic
    thorne_zytkow, TZO,
    # Phenomena
    planetary_nebula, nova, kilonova,
    type_ia_supernova, failed_supernova,
    pair_instability_supernova, PISN, stellar_merger
)

# Create figure for stellar phases
fig, ax = setup_canvas(width=14, height=10, xlim=(0, 14), ylim=(0, 10))
ax.set_title('Stellar Evolution Phases', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Main Sequence and early evolution
y1 = 8.5
zams(1.5, y1, size=0.4, label_text='ZAMS')
hertzsprung_gap(4, y1, size=0.5, label_text='Hertzsprung Gap')
horizontal_branch(6.5, y1, size=0.4, label_text='Horizontal Branch')
helium_star(9, y1, size=0.35, label_text='He Star')
stripped_star(11.5, y1, size=0.3, label_text='Stripped Star')

# Row 2: Giants and supergiants
y2 = 6
red_giant(1.5, y2, size=0.55, label_text='Red Giant (RGB)')
asymptotic_giant_branch(4, y2, size=0.6, label_text='AGB Star')
red_supergiant(7, y2, size=0.7, label_text='Red Supergiant')
blue_supergiant(10, y2, size=0.5, label_text='Blue Supergiant')
yellow_supergiant(12.5, y2, size=0.55, label_text='Yellow Supergiant')

# Row 3: Wolf-Rayet and exotic objects
y3 = 3.5
wolf_rayet(2, y3, size=0.45, label_text='Wolf-Rayet')
thorne_zytkow(5, y3, size=0.6, core_size=0.1, label_text='Thorne-Żytkow Object')
stellar_merger(8, y3, size=0.5, label_text='Merger Product')

plt.tight_layout()
plt.savefig('tests/output_stellar_phases.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_stellar_phases.png")
plt.close()


# Create figure for stellar phenomena
fig, ax = setup_canvas(width=14, height=8, xlim=(0, 14), ylim=(0, 8))
ax.set_title('Stellar Phenomena (Explosions & Transients)', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Nebulae and novae
y1 = 5.5
planetary_nebula(2, y1, size=0.7, wd_size=0.1, label_text='Planetary Nebula')
nova(5, y1, size=0.5, label_text='Classical Nova')
kilonova(8, y1, size=0.6, label_text='Kilonova')
supernova(11.5, y1, size=1.0, label_text='Core-Collapse SN')

# Row 2: Different supernova types
y2 = 2.5
type_ia_supernova(2.5, y2, size=0.9, label_text='Type Ia SN')
failed_supernova(5.5, y2, size=0.25, label_text='Failed SN\n(Direct Collapse)')
pair_instability_supernova(9, y2, size=1.2, label_text='Pair-Instability SN')

plt.tight_layout()
plt.savefig('tests/output_stellar_phenomena.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_stellar_phenomena.png")
plt.close()

print("\nStellar phases and phenomena tests completed!")
print("Functions tested:")
print("  - red_giant(), RGB()")
print("  - asymptotic_giant_branch(), AGB()")
print("  - red_supergiant(), RSG()")
print("  - blue_supergiant(), BSG()")
print("  - yellow_supergiant(), YSG()")
print("  - horizontal_branch(), HB()")
print("  - hertzsprung_gap(), HG()")
print("  - helium_star(), He_star()")
print("  - stripped_star()")
print("  - thorne_zytkow(), TZO()")
print("  - planetary_nebula()")
print("  - nova()")
print("  - kilonova()")
print("  - type_ia_supernova()")
print("  - failed_supernova()")
print("  - pair_instability_supernova(), PISN()")
print("  - stellar_merger()")
