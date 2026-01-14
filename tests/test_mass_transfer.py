#!/usr/bin/env python3
"""
Test script for mass transfer and accretion components.
Demonstrates accretion disk, jets, mass transfer streams, and RLO cases.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.components.binary import (
    accretion_disk, mass_transfer_stream, jet, wind_mass_transfer,
    case_A_RLO, case_B_RLO, case_C_RLO, roche_lobe_overflow
)
from rua.components.compact import BH, NS

# Create figure for mass transfer components
fig, ax = setup_canvas(width=14, height=12, xlim=(0, 14), ylim=(0, 12))
ax.set_title('Mass Transfer & Accretion Components', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Accretion disks with different properties
y1 = 10
accretion_disk(2, y1, inner_radius=0.15, outer_radius=0.5, inclination=0.2,
               label_text='Accretion Disk\n(low inclination)', ax=ax)
BH(2, y1, size=0.15, label_text='', ax=ax)

accretion_disk(6, y1, inner_radius=0.12, outer_radius=0.6, inclination=0.5,
               label_text='Accretion Disk\n(high inclination)', ax=ax)
NS(6, y1, size=0.12, label_text='', ax=ax)

# Jet with accretion disk
accretion_disk(10, y1, inner_radius=0.12, outer_radius=0.4, inclination=0.3, ax=ax)
BH(10, y1, size=0.12, label_text='', ax=ax)
jet(10, y1, length=0.8, width=0.1, label_text='Relativistic Jet', ax=ax)

# Row 2: Mass transfer stream
y2 = 7
mass_transfer_stream(4, y2, 7, y2, width=0.06, label_text='Mass Transfer Stream', ax=ax)
# Add source and target stars
from rua.components.stellar import star
from rua.utils.colors import colors
star(3.8, y2, size=0.3, color=colors['RGB'], edgecolor='darkred', ax=ax)
accretion_disk(7.2, y2, inner_radius=0.1, outer_radius=0.3, ax=ax)
NS(7.2, y2, size=0.1, label_text='', ax=ax)

# Wind mass transfer
wind_mass_transfer(11, y2, size=0.35, wind_extent=0.6, label_text='Wind Mass Transfer', ax=ax)

# Row 3: Case A, B, C RLO
y3 = 4
case_A_RLO(2, y3, donor_size=0.35, accretor_size=0.3, separation=0.9,
           label_text='Case A RLO\n(H core burning)', ax=ax)
case_B_RLO(7, y3, donor_size=0.45, accretor_size=0.3, separation=1.0,
           label_text='Case B RLO\n(H shell burning)', ax=ax)
case_C_RLO(12, y3, donor_size=0.5, accretor_size=0.25, separation=1.1,
           label_text='Case C RLO\n(He shell burning)', ax=ax)

# Row 4: RLO with flip
y4 = 1.5
roche_lobe_overflow(3, y4, donor_size=0.35, accretor_size=0.25, separation=0.9,
                    flip=False, label_text='RLO (normal)', ax=ax)
roche_lobe_overflow(9, y4, donor_size=0.35, accretor_size=0.25, separation=0.9,
                    flip=True, label_text='RLO (flipped)', ax=ax)

plt.tight_layout()
plt.savefig('tests/output_mass_transfer.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_mass_transfer.png")
plt.close()

print("\nMass transfer components tests completed!")
print("Functions tested:")
print("  - accretion_disk()")
print("  - mass_transfer_stream()")
print("  - jet()")
print("  - wind_mass_transfer()")
print("  - case_A_RLO()")
print("  - case_B_RLO()")
print("  - case_C_RLO()")
print("  - roche_lobe_overflow() with flip parameter")
