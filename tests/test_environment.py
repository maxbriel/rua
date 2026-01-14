#!/usr/bin/env python3
"""
Test script for environment and structure components.
Demonstrates functions from environment.py module.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.components.environment import (
    circumbinary_disk, stellar_wind, magnetosphere, pulsar,
    pulsar_wind_nebula, common_envelope_spiral, supernova_remnant,
    accretion_column, tidal_tail
)
from rua.components.stellar import star
from rua.utils.colors import colors

# Create figure for environment components
fig, ax = setup_canvas(width=14, height=14, xlim=(0, 14), ylim=(0, 14))
ax.set_title('Environment & Structure Components', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Disks and winds
y1 = 12
circumbinary_disk(2.5, y1, inner_radius=0.9, outer_radius=1.6, 
                  inclination=0.3, gap_radius=0.7, label_text='Circumbinary Disk')
# Add binary inside the disk
star(2.2, y1, size=0.15, color=colors['ZAMS'], ax=ax)
star(2.8, y1, size=0.12, color=colors['lower_mass_ZAMS'], ax=ax)

stellar_wind(7, y1, star_size=0.35, wind_extent=0.7, n_shells=4,
             label_text='Stellar Wind')
tidal_tail(11.5, y1, star_size=0.3, tail_length=1.0, tail_direction=30,
           label_text='Tidal Tail')

# Row 2: Neutron star environments
y2 = 8.5
magnetosphere(2, y2, ns_size=0.12, field_extent=0.6, n_lines=5,
              label_text='NS Magnetosphere')
pulsar(6, y2, ns_size=0.1, beam_length=0.7, beam_width=0.15,
       beam_angle=25, label_text='Pulsar')
accretion_column(10, y2, ns_size=0.12, column_height=0.5, column_width=0.1,
                 label_text='Accretion Columns')

# Row 3: Extended structures
y3 = 5
pulsar_wind_nebula(2.5, y3, pulsar_size=0.08, nebula_size=1.0,
                   label_text='Pulsar Wind Nebula')
supernova_remnant(7, y3, remnant_size=1.2, co_size=0.08, co_type='NS',
                  n_shells=3, label_text='Supernova Remnant (NS)')
supernova_remnant(11.5, y3, remnant_size=1.0, co_size=0.1, co_type='BH',
                  n_shells=3, label_text='Supernova Remnant (BH)')

# Row 4: Common envelope with spiral
y4 = 1.8
common_envelope_spiral(4, y4, core_size=0.18, companion_size=0.12,
                       envelope_size=0.8, n_arms=2, n_turns=1.5,
                       label_text='CE with Spiral Arms')
supernova_remnant(10, y4, remnant_size=0.9, co_size=0.06, co_type=None,
                  n_shells=4, label_text='Type Ia Remnant\n(no central object)')

plt.tight_layout()
plt.savefig('tests/output_environment.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_environment.png")
plt.close()

print("\nEnvironment components tests completed!")
print("Functions tested:")
print("  - circumbinary_disk()")
print("  - stellar_wind()")
print("  - magnetosphere()")
print("  - pulsar()")
print("  - pulsar_wind_nebula()")
print("  - common_envelope_spiral()")
print("  - supernova_remnant()")
print("  - accretion_column()")
print("  - tidal_tail()")
