#!/usr/bin/env python3
"""
Test script for stellar object drawing functions.
Demonstrates all functions from stellar.py module.
"""

import matplotlib.pyplot as plt
from rua.components.stellar import (
    star,
    supernova_image,
    zams,
    wolf_rayet,
    supernova
)
from rua.utils.colors import colors

# Create figure with subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Stellar Object Drawing Functions Test', 
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

# Test 1: Basic stars with different colors
axes[0].set_title('star() - Various Colors', fontweight='bold')
star(axes[0], -1, 1, size=0.3, color='yellow', edgecolor='black')
star(axes[0], 1, 1, size=0.3, color='orange', edgecolor='darkred')
star(axes[0], -1, -1, size=0.25, color='lightblue', edgecolor='blue')
star(axes[0], 1, -1, size=0.35, color='red', edgecolor='darkred')
axes[0].text(0, -1.7, 'Different sizes and colors', ha='center', fontsize=10)

# Test 2: Stars with hatching patterns
axes[1].set_title('star() - With Hatching', fontweight='bold')
star(axes[1], -0.8, 0.5, size=0.4, color='yellow', 
     edgecolor='black', hatch='//')
star(axes[1], 0.8, 0.5, size=0.4, color='lightblue', 
     edgecolor='blue', hatch='\\\\')
star(axes[1], 0, -0.7, size=0.4, color='orange', 
     edgecolor='red', hatch='xx')
axes[1].text(0, -1.7, 'Hatch patterns: //, \\\\, xx', ha='center', fontsize=10)

# Test 3: ZAMS star
axes[2].set_title('zams()', fontweight='bold')
zams(axes[2], 0, 0.3, size=0.5, 
     label_text='ZAMS\n(Main Sequence)', 
     label_position='bottom')
zams(axes[2], 0, -0.8, size=0.3, 
     label_text='Smaller ZAMS', 
     label_position='bottom')
axes[2].text(0, -1.7, f"Color: {colors['ZAMS']}", ha='center', fontsize=9)

# Test 4: Wolf-Rayet star
axes[3].set_title('wolf_rayet()', fontweight='bold')
wolf_rayet(axes[3], -0.5, 0.3, size=0.5, 
           label_text='WR Phase\n(He-burning)', 
           label_position='right')
wolf_rayet(axes[3], 0.5, -0.7, size=0.4, 
           label_text='WR Star', 
           label_position='left')
axes[3].text(0, -1.7, f"Color: {colors['WR']}", ha='center', fontsize=9)

# Test 5: Supernova image (will use fallback if image not found)
axes[4].set_title('supernova_image()', fontweight='bold')
supernova_image(axes[4], 0, 0.3, size=1.2)
supernova_image(axes[4], 0, -0.8, size=0.6, image_path='nonexistent.png')
axes[4].text(0, -1.7, 'Top: image (or fallback)\nBottom: fallback', 
             ha='center', fontsize=9)

# Test 6: Complete supernova with label
axes[5].set_title('supernova()', fontweight='bold')
supernova(axes[5], 0, 0, size=1.5, 
          label_text='Supernova\n(BH/NS)')
axes[5].text(0, -1.7, 'Complete with label', ha='center', fontsize=9)

# Adjust layout and save
plt.tight_layout()
plt.savefig('test_stellar.png', dpi=150, bbox_inches='tight')
print("Figure saved as 'test_stellar.png'")
print("\nFunctions tested:")
print("  1. star() - basic star with various properties")
print("  2. star() - with hatch patterns")
print("  3. zams() - ZAMS stars with labels")
print("  4. wolf_rayet() - Wolf-Rayet stars with labels")
print("  5. supernova_image() - supernova image rendering")
print("  6. supernova() - complete supernova with label")
plt.close()
