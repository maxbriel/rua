#!/usr/bin/env python3
"""
Test script for arrow drawing with different label positions.
"""

import matplotlib.pyplot as plt
from rua.components.decorator import arrow

# Create figure
fig, ax = plt.subplots(figsize=(10, 10))

# Set up the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Arrow Label Position Test', fontsize=16, fontweight='bold')

# Draw arrows with different label positions
# Top label
arrow(ax, 1, 2, 4, 2, label='Top Label', label_position='top', color='blue')

# Bottom label
arrow(ax, 1, 4, 4, 4, label='Bottom Label', label_position='bottom', color='green')

# Left label
arrow(ax, 1, 6, 4, 6, label='Left Label', label_position='left', color='red')

# Right label
arrow(ax, 1, 8, 4, 8, label='Right Label', label_position='right', color='purple')

# Diagonal arrows with different positions
arrow(ax, 6, 2, 9, 4, label='Top', label_position='top', color='orange', style='dashed')
arrow(ax, 6, 4.5, 9, 6.5, label='Bottom', label_position='bottom', color='cyan', style='dashed')
arrow(ax, 6, 7, 9, 9, label='Left', label_position='left', color='magenta', style='dotted')

# Add some annotations
ax.text(2.5, 0.5, 'Horizontal Arrows', ha='center', fontsize=12, style='italic')
ax.text(7.5, 0.5, 'Diagonal Arrows', ha='center', fontsize=12, style='italic')

# Save the figure
plt.tight_layout()
plt.savefig('tests/test_arrows.png', dpi=150, bbox_inches='tight')
print("Figure saved as 'tests/test_arrows.png'")
plt.close()
