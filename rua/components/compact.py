"""
Compact object drawing functions.
Contains functions for neutron stars, black holes, and generic compact objects.
"""

import matplotlib.pyplot as plt

from rua.utils.colors import colors
from rua.components.stellar import star
from rua.components.decorator import label


def NS(ax, x, y, size=0.1, label_text='Neutron Star'):
    """Draw neutron star with radial gradient (white to light blue)
    
    Creates a three-layer effect: outer (powder blue), middle (very light blue),
    and inner (alice blue) to simulate a luminous compact object.
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: outer layer size
        label_text: optional label text
    """
    star(ax, x, y, size=0.1, color=colors['NS_outer'], edgecolor='black')  # Outer: powder blue
    star(ax, x, y, size=0.07, color=colors['NS_middle'], edgecolor='none')  # Middle: very light blue
    star(ax, x, y, size=0.04, color=colors['NS_inner'], edgecolor='none')  # Inner: near white (alice blue)


def BH(ax, x, y, size=0.2, label_text='Black Hole'):
    """Draw black hole
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: black hole size
        label_text: optional label text
    """
    star(ax, x, y, size=size, color=colors['BH'], edgecolor='black')  # Outer: dark gray

def WD(ax, x, y, size=0.15, label_text='White Dwarf'):
    """Draw white dwarf
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: white dwarf size
        label_text: optional label text
    """
    star(ax, x, y, size=size, color=colors['WD'], edgecolor='black')  # White dwarf: white color


def compact_objects(ax, x, y, size=0.2, label_text='', label_position='right'):
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
    
    NS(ax, ns_x, ns_y, size=0.1)
    ax.text(x-0.05, y, '/', ha='center', va='center', fontsize=20, fontweight='bold')
    BH(ax, bh_x, bh_y, size=size)
    
    if label_text:
        label(ax, x, y, label_text, label_position=label_position)
