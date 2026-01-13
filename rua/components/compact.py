"""
Compact object drawing functions.
Contains functions for neutron stars, black holes, and generic compact objects.
"""

import matplotlib.pyplot as plt

from rua.utils.colors import colors
from rua.components.stellar import draw_star
from rua.components.decorator import add_label


def draw_NS(ax, x, y, size=0.1, label_text='Neutron Star'):
    """Draw neutron star with radial gradient (white to light blue)
    
    Creates a three-layer effect: outer (powder blue), middle (very light blue),
    and inner (alice blue) to simulate a luminous compact object.
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: outer layer size
        label_text: optional label text
    """
    draw_star(ax, x, y, size=0.1, color=colors['NS_outer'], edgecolor='black')  # Outer: powder blue
    draw_star(ax, x, y, size=0.07, color=colors['NS_middle'], edgecolor='none')  # Middle: very light blue
    draw_star(ax, x, y, size=0.04, color=colors['NS_inner'], edgecolor='none')  # Inner: near white (alice blue)


def draw_BH(ax, x, y, size=0.2, label_text='Black Hole'):
    """Draw black hole
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: black hole size
        label_text: optional label text
    """
    draw_star(ax, x, y, size=size, color=colors['BH'], edgecolor='black')  # Outer: dark gray


def draw_compact_object(ax, x, y, size=0.2, label_text='', label_position='right'):
    """Draw a compact object (neutron star or black hole)
    
    Shows both NS and BH with a slash separator to indicate either/or.
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: size for BH (NS uses fixed smaller size)
        label_text: optional label text
        label_position: 'top', 'bottom', 'left', or 'right'
    """
    # Neutron star
    ns_x, ns_y = x-0.3, y
    bh_x, bh_y = x+0.3, y
    
    draw_NS(ax, ns_x, ns_y, size=0.1)
    ax.text(x-0.05, y, '/', ha='center', va='center', fontsize=20, fontweight='bold')
    draw_BH(ax, bh_x, bh_y, size=size)
    
    if label_text:
        add_label(ax, x, y, label_text, label_position=label_position)
