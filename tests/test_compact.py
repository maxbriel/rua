#!/usr/bin/env python3
"""
Test script for compact object drawing functions.
Demonstrates all functions from compact.py module.
"""

import matplotlib.pyplot as plt
from rua.components.compact import NS, BH, WD, compact_objects
from rua.utils.colors import colors

# Create figure with subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Compact Object Drawing Functions Test', 
             fontsize=18, fontweight='bold')

# Flatten axes for easier iteration
axes = axes.flatten()

# Set common properties for all subplots
for ax in axes:
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.3)

# Test 1: Neutron stars with different sizes
axes[0].set_title('NS() - Neutron Stars', fontweight='bold')
NS(0, 0.5, size=0.15, label_text='Larger NS', ax=axes[0])
NS(0, -0.5, size=0.1, label_text='Standard NS', ax=axes[0])
axes[0].text(0, -1.7, 'Gradient effect: powder blue to white', ha='center', fontsize=10)

# Test 2: Black holes with different sizes
axes[1].set_title('BH() - Black Holes', fontweight='bold')
BH(0, 0.7, size=0.3, label_text='Large BH', ax=axes[1])
BH(0, 0, size=0.2, label_text='Medium BH', ax=axes[1])
BH(0, -0.7, size=0.15, label_text='Small BH', ax=axes[1])
axes[1].text(0, -1.7, f"Color: {colors['BH']}", ha='center', fontsize=9)

# Test 3: White dwarfs with different sizes
axes[2].set_title('WD() - White Dwarfs', fontweight='bold')
WD(0, 0.6, size=0.25, label_text='Large WD', ax=axes[2])
WD(0, 0, size=0.15, label_text='Standard WD', ax=axes[2])
WD(0, -0.6, size=0.1, label_text='Small WD', ax=axes[2])
axes[2].text(0, -1.7, f"Color: {colors['WD']}", ha='center', fontsize=9)

# Test 4: Comparison of all compact objects
axes[3].set_title('Compact Object Comparison', fontweight='bold')
NS(0, 0.8, size=0.1, label_text='NS', ax=axes[3])
BH(0, 0, size=0.2, label_text='BH', ax=axes[3])
WD(0, -0.8, size=0.15, label_text='WD', ax=axes[3])
axes[3].text(0, -1.7, 'All three types side by side', ha='center', fontsize=10)

# Test 5: compact_objects() - NS/BH combination
axes[4].set_title('compact_objects() - Default', fontweight='bold')
compact_objects(0, 0, size=0.2, label_text='NS / BH', label_position='bottom', ax=axes[4])
axes[4].text(0, -1.7, 'Either neutron star or black hole', ha='center', fontsize=10)

# Test 6: compact_objects() - different label positions
axes[5].set_title('compact_objects() - Label Positions', fontweight='bold')
compact_objects(0, 0.8, size=0.15, label_text='Top', label_position='top', ax=axes[5])
compact_objects(0, -0.8, size=0.15, label_text='Bottom', label_position='bottom', ax=axes[5])
axes[5].text(0, -1.7, 'Different label placements', ha='center', fontsize=10)

# Adjust layout and save
plt.tight_layout()
plt.savefig('tests/test_compact.png', dpi=150, bbox_inches='tight')
print("Figure saved as 'tests/test_compact.png'")
print("\nFunctions tested:")
print("  1. NS() - neutron stars with gradient effect")
print("  2. BH() - black holes in various sizes")
print("  3. WD() - white dwarfs in various sizes")
print("  4. Comparison - all three compact object types")
print("  5. compact_objects() - NS/BH combination (default)")
print("  6. compact_objects() - different label positions")
plt.close()
