"""
Compact object drawing functions.
Contains functions for neutron stars, black holes, and generic compact objects.
"""

import matplotlib.pyplot as plt

from rua.utils.colors import colors
from rua.components.stellar import star
from rua.components.decorator import label


def NS(x, y, size=0.1, label_text='NS', ax=None, **kwargs):
    """Draw neutron star with radial gradient (white to light blue).
    
    Creates a three-layer effect: outer (powder blue), middle (very light blue),
    and inner (alice blue) to simulate a luminous compact object.
    
    Parameters
    ----------
    x : float
        X-coordinate of the neutron star center.
    y : float
        Y-coordinate of the neutron star center.
    size : float, optional
        Outer layer size (default: 0.1).
    label_text : str, optional
        Text label to display near the neutron star (default: 'NS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    **kwargs
        Additional keyword arguments passed to the star function.
    
    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()
    star(ax=ax,
         x=x,
         y=y,
         size=size,
         label_text=label_text,
         color=colors['NS_outer'],
         edgecolor='black')  # Outer: powder blue
    star(ax=ax,
         x=x,
         y=y,
         size=size-size*0.3,
         color=colors['NS_middle'],
         edgecolor='none')  # Middle: very light blue
    star(ax=ax,
         x=x,
         y=y,
         size=size-size*0.6,
         color=colors['NS_inner'],
         edgecolor='none')  # Inner: near white (alice blue)


def BH(x, y, size=0.2, label_text='Black Hole', ax=None, **kwargs):
    """Draw black hole.
    
    Parameters
    ----------
    x : float
        X-coordinate of the black hole center.
    y : float
        Y-coordinate of the black hole center.
    size : float, optional
        Black hole size (default: 0.2).
    label_text : str, optional
        Text label to display near the black hole (default: 'Black Hole').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    **kwargs
        Additional keyword arguments passed to the star function.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    star(ax=ax,
         x=x,
         y=y,
         size=size,
         color=colors['BH'],
         edgecolor='black',
         label_text=label_text,
         **kwargs)  # Outer: dark gray

def WD(x,
       y,
       size=0.15,
       label_text='WD',
       ax=None,
       **kwargs):
    """Draw white dwarf.
    
    Parameters
    ----------
    x : float
        X-coordinate of the white dwarf center.
    y : float
        Y-coordinate of the white dwarf center.
    size : float, optional
        White dwarf size (default: 0.15).
    label_text : str, optional
        Text label to display near the white dwarf (default: 'WD').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    **kwargs
        Additional keyword arguments passed to the star function.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    star(ax=ax,
         x=x,
         y=y,
         size=size,
         color=colors['WD'],
         edgecolor='black',
         label_text=label_text,
         **kwargs)  # White dwarf: white color


def compact_objects(x, y, size=0.4, label_text='', label_position='right', ax=None):
    """Draw a compact object (neutron star or black hole).
    
    Shows both NS and BH with a slash separator to indicate either/or.
    
    Parameters
    ----------
    x : float
        X-coordinate of the compact object center.
    y : float
        Y-coordinate of the compact object center.
    size : float, optional
        Size for BH (NS uses size-0.1) (default: 0.4).
    label_text : str, optional
        Text label to display near the compact object (default: '').
    label_position : str, optional
        Position of the label relative to the object (default: 'right').
        Options: 'top', 'bottom', 'left', 'right'.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    ns_x, ns_y = x-0.3, y
    bh_x, bh_y = x+0.3, y
    
    NS(ns_x, ns_y, size=size-0.1, label_text='', ax=ax)
    ax.text(x-0.02, y, '/', ha='center', va='center', fontsize=20, fontweight='bold')
    BH(bh_x, bh_y, size=size, label_text='', ax=ax)
    
    if label_text:
        # Scale label offset with size
        label_offset = size + 0.15
        label(ax, x, y, label_text, label_position=label_position, label_offset=label_offset)
