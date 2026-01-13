#!/usr/bin/env python3
"""
Test script for binary stellar system drawing functions.
Demonstrates binary() and HMS_HMS() functions from binary.py module.
"""

import matplotlib.pyplot as plt
from rua.components.binary import binary, HMS_HMS, common_envelope, roche_lobe_overflow
from rua.components.stellar import star
from rua.utils.colors import colors

# Create figure with subplots
fig, axes = plt.subplots(4, 3, figsize=(15, 20))
fig.suptitle('Binary System Drawing Functions Test', 
             fontsize=18, fontweight='bold')

# Flatten axes for easier iteration
axes = axes.flatten()

# Set common properties for all subplots
for ax in axes:
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.3)

# Test 1: Basic binary with default colors
axes[0].set_title('binary() - Default Colors', fontweight='bold')
binary(0, 0, 
       primary=star, 
       secondary=star,
       size_primary=0.3, 
       size_secondary=0.25,
       separation=1.0,
       ax=axes[0])
axes[0].text(0, -2.5, 'ZAMS colors (default)', ha='center', fontsize=10)

# Test 2: Binary with custom colors
axes[1].set_title('binary() - Custom Colors', fontweight='bold')
binary(0, 0,
       primary=star,
       secondary=star,
       size_primary=0.35,
       size_secondary=0.2,
       separation=1.2,
       colors_tuple=('orange', 'lightblue'),
       ax=axes[1])
axes[1].text(0, -2.5, 'Orange primary, light blue secondary', ha='center', fontsize=10)

# Test 3: Binary with label
axes[2].set_title('binary() - With Label', fontweight='bold')
binary(0, 0,
       primary=star,
       secondary=star,
       size_primary=0.3,
       size_secondary=0.25,
       separation=1.0,
       label_text='Binary System',
       ax=axes[2])
axes[2].text(0, -2.5, 'With label text', ha='center', fontsize=10)

# Test 4: Binary with different separations
axes[3].set_title('binary() - Varying Separation', fontweight='bold')
binary(-0.8, 1.0,
       primary=star,
       secondary=star,
       size_primary=0.2,
       size_secondary=0.15,
       separation=0.5,
       colors_tuple=('yellow', 'yellow'),
       ax=axes[3])
binary(-0.8, 0,
       primary=star,
       secondary=star,
       size_primary=0.2,
       size_secondary=0.15,
       separation=1.0,
       colors_tuple=('yellow', 'yellow'),
       ax=axes[3])
binary(-0.8, -1.0,
       primary=star,
       secondary=star,
       size_primary=0.2,
       size_secondary=0.15,
       separation=1.5,
       colors_tuple=('yellow', 'yellow'),
       ax=axes[3])
axes[3].text(0, -2.5, 'Separations: 0.5, 1.0, 1.5', ha='center', fontsize=10)

# Test 5: HMS_HMS - default
axes[4].set_title('HMS_HMS() - Default', fontweight='bold')
HMS_HMS(0, 0,
        size_primary=0.35,
        size_secondary=0.3,
        separation=1.2,
        ax=axes[4])
axes[4].text(0, -2.5, 'High-mass main sequence binary', ha='center', fontsize=10)

# Test 6: HMS_HMS - with custom label
axes[5].set_title('HMS_HMS() - Custom Label', fontweight='bold')
HMS_HMS(0, 0.5,
        size_primary=0.3,
        size_secondary=0.25,
        separation=1.0,
        label_text='Massive\nBinary',
        ax=axes[5])
HMS_HMS(0, -1.0,
        size_primary=0.25,
        size_secondary=0.2,
        separation=0.8,
        label_text='Compact HMS',
        ax=axes[5])
axes[5].text(0, -2.5, 'Multiple HMS binaries', ha='center', fontsize=10)

# Test 7: common_envelope - default
axes[6].set_title('common_envelope() - Default', fontweight='bold')
common_envelope(0, 0,
                primary=star,
                secondary=star,
                envelope_size=1.0,
                ax=axes[6])
axes[6].text(0, -2.5, 'Common envelope with default colors', ha='center', fontsize=10)

# Test 8: common_envelope - custom sizes and colors
axes[7].set_title('common_envelope() - Custom', fontweight='bold')
common_envelope(0, 0,
                primary=star,
                secondary=star,
                primary_size=0.25,
                secondary_size=0.2,
                envelope_size=1.2,
                colors_tuple=('pink', 'orange', 'yellow'),
                ax=axes[7])
axes[7].text(0, -2.5, 'Pink envelope, orange/yellow cores', ha='center', fontsize=10)

# Test 9: common_envelope - with label
axes[8].set_title('common_envelope() - With Label', fontweight='bold')
common_envelope(0, 0.3,
                primary=star,
                secondary=star,
                envelope_size=0.8,
                label_text='CE Phase',
                ax=axes[8])
common_envelope(0, -1.2,
                primary=star,
                secondary=star,
                envelope_size=0.6,
                label_text='Compact CE',
                ax=axes[8])
axes[8].text(0, -2.5, 'Multiple CE systems with labels', ha='center', fontsize=10)

# Test 10: roche_lobe_overflow - default
axes[9].set_title('roche_lobe_overflow() - Default', fontweight='bold')
roche_lobe_overflow(0, 0,
                    accretor=star,
                    ax=axes[9])
axes[9].text(0, -2.5, 'Roche lobe overflow (default)', ha='center', fontsize=10)

# Test 11: roche_lobe_overflow - custom colors and sizes
axes[10].set_title('roche_lobe_overflow() - Custom', fontweight='bold')
roche_lobe_overflow(0, 0,
                    accretor=star,
                    donor_size=0.4,
                    accretor_size=0.3,
                    separation=1.0,
                    donor_color='red',
                    accretor_color='lightblue',
                    ax=axes[10])
axes[10].text(0, -2.5, 'Red donor, blue accretor, larger sizes', ha='center', fontsize=10)

# Test 12: roche_lobe_overflow - flipped and with label
axes[11].set_title('roche_lobe_overflow() - Flipped', fontweight='bold')
roche_lobe_overflow(0, 0.5,
                    accretor=star,
                    flip=True,
                    donor_size=0.35,
                    accretor_size=0.25,
                    label_text='RLO\n(flipped)',
                    ax=axes[11])
roche_lobe_overflow(0, -1.0,
                    accretor=star,
                    flip=False,
                    donor_size=0.3,
                    accretor_size=0.2,
                    label_text='RLO\n(normal)',
                    ax=axes[11])
axes[11].text(0, -2.5, 'Flipped vs normal orientation', ha='center', fontsize=10)

# Adjust layout and save
plt.tight_layout()
plt.savefig('test_binary.png', dpi=150, bbox_inches='tight')
print("Figure saved as 'test_binary.png'")
print("\nFunctions tested:")
print("  1. binary() - default ZAMS colors")
print("  2. binary() - custom colors (orange & light blue)")
print("  3. binary() - with label text")
print("  4. binary() - varying separations (0.5, 1.0, 1.5)")
print("  5. HMS_HMS() - default high-mass main sequence binary")
print("  6. HMS_HMS() - multiple systems with custom labels")
print("  7. common_envelope() - default common envelope")
print("  8. common_envelope() - custom sizes and colors")
print("  9. common_envelope() - multiple systems with labels")
print(" 10. roche_lobe_overflow() - default configuration")
print(" 11. roche_lobe_overflow() - custom colors and sizes")
print(" 12. roche_lobe_overflow() - flipped vs normal orientation")
plt.close()
