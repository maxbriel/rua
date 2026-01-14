#!/usr/bin/env python3
"""
Test script for multi-star systems.
Demonstrates functions from multiples.py module.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.components.multiples import (
    triple_system, quadruple_system_2plus2, quadruple_system_3plus1,
    star_cluster, triple_with_compact, hierarchical_triple_diagram
)

# Create figure for multi-star systems
fig, ax = setup_canvas(width=14, height=12, xlim=(0, 14), ylim=(0, 12))
ax.set_title('Multi-Star Systems', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Triple systems
y1 = 10
triple_system(2.5, y1, sizes=(0.3, 0.25, 0.2), inner_separation=0.6,
              outer_separation=1.5, label_text='Hierarchical Triple')
triple_with_compact(7.5, y1, co_type='BH', co_size=0.12, star_sizes=(0.3, 0.2),
                    inner_separation=0.5, outer_separation=1.2,
                    label_text='Triple with BH')
hierarchical_triple_diagram(12, y1, inner_period='P₁', outer_period='P₂',
                            sizes=(0.25, 0.2, 0.15), label_text='')

# Row 2: Quadruple systems
y2 = 6.5
quadruple_system_2plus2(3.5, y2, sizes=(0.25, 0.2, 0.22, 0.18),
                        inner_separations=(0.45, 0.4), outer_separation=2.0,
                        label_text='2+2 Quadruple')
quadruple_system_3plus1(10, y2, sizes=(0.25, 0.2, 0.18, 0.15),
                        inner_separation=0.45, mid_separation=1.0,
                        outer_separation=2.0, label_text='3+1 Quadruple')

# Row 3: Star clusters
y3 = 2.5
star_cluster(3, y3, n_stars=15, cluster_radius=1.2, size_range=(0.08, 0.2),
             label_text='Star Cluster', seed=42)
star_cluster(9, y3, n_stars=25, cluster_radius=1.5, size_range=(0.06, 0.18),
             label_text='Dense Cluster', seed=123)

plt.tight_layout()
plt.savefig('tests/output_multiples.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_multiples.png")
plt.close()

print("\nMulti-star systems tests completed!")
print("Functions tested:")
print("  - triple_system()")
print("  - triple_with_compact()")
print("  - hierarchical_triple_diagram()")
print("  - quadruple_system_2plus2()")
print("  - quadruple_system_3plus1()")
print("  - star_cluster()")
