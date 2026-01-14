#!/usr/bin/env python3
"""
Test script for binary evolution outcomes.
Demonstrates functions from outcomes.py module.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.components.outcomes import (
    gravitational_wave_merger, natal_kick, unbound_system, runaway_star,
    supernova_in_binary, binary_merger_product, common_envelope_ejection
)

# Create figure for binary outcomes
fig, ax = setup_canvas(width=14, height=10, xlim=(0, 14), ylim=(0, 10))
ax.set_title('Binary Evolution Outcomes', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Merger events
y1 = 8
gravitational_wave_merger(2, y1, size=0.6, n_waves=4, label_text='GW Merger')
binary_merger_product(6, y1, size=0.5, label_text='Merger Product')
common_envelope_ejection(10.5, y1, core_size=0.15, companion_size=0.12, 
                         envelope_size=0.7, label_text='CE Ejection')

# Row 2: Supernova events
y2 = 5
supernova_in_binary(3, y2, sn_size=0.7, companion_size=0.3, separation=1.2, 
                    label_text='SN in Binary')
natal_kick(8, y2, kick_direction=60, kick_length=0.9, compact_size=0.12,
           co_type='NS', label_text='Natal Kick (NS)')
natal_kick(12, y2, kick_direction=120, kick_length=0.7, compact_size=0.15,
           co_type='BH', label_text='Natal Kick (BH)')

# Row 3: Disrupted systems
y3 = 2
unbound_system(3, y3, size1=0.12, size2=0.2, separation=0.9, 
               escape_distance=0.6, label_text='Unbound System')
runaway_star(8, y3, size=0.3, velocity_direction=40, velocity_length=0.7,
             label_text='Runaway Star')

plt.tight_layout()
plt.savefig('tests/output_outcomes.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_outcomes.png")
plt.close()

print("\nBinary outcomes tests completed!")
print("Functions tested:")
print("  - gravitational_wave_merger()")
print("  - natal_kick()")
print("  - unbound_system()")
print("  - runaway_star()")
print("  - supernova_in_binary()")
print("  - binary_merger_product()")
print("  - common_envelope_ejection()")
