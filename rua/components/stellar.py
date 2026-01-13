"""
Single stellar object drawing functions.
Contains functions for drawing individual stars and stellar phases.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.image as mpimg
import os

from rua.utils.colors import colors
from rua.components.decorator import add_label


def draw_star(ax, x, y, size=0.3, color='yellow', edgecolor='black', label='', hatch=None):
    """Draw a cartoon star representation
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: radius of the star
        color: fill color
        edgecolor: edge color
        label: optional label text
        hatch: optional hatch pattern
        
    Returns:
        circle: matplotlib Circle patch
    """
    circle = Circle((x, y), size, facecolor=color, edgecolor=edgecolor, linewidth=0.5, zorder=3, hatch=hatch)
    ax.add_patch(circle)
    return circle


def draw_supernova_image(ax, x, y, size=1.0, image_path='supernova.png'):
    """Display supernova PNG image at specified location
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: image size
        image_path: path to supernova image file
    """
    if os.path.exists(image_path):
        img = mpimg.imread(image_path)
        # Calculate extent to center the image at (x, y) with given size
        extent = [x - size/2, x + size/2, y - size/2, y + size/2]
        ax.imshow(img, extent=extent, aspect='auto', zorder=3)
    else:
        # Fallback to drawing a simple star if image not found
        draw_star(ax, x, y, size=size/2, color='orange', edgecolor='red')


def draw_zams_star(ax, x, y, size=0.4, label_text='ZAMS\n(Main Sequence)', label_position='bottom'):
    """Draw a ZAMS (Zero Age Main Sequence) star
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: star radius
        label_text: label text
        label_position: 'top', 'bottom', 'left', or 'right'
    """
    draw_star(ax, x, y, size=size, color=colors['ZAMS'], edgecolor='black')
    add_label(ax, x, y, label_text, label_position)


def draw_wr_star(ax, x, y, size=0.45, label_text='WR Phase\n(He-burning)', label_position='right'):
    """Draw a Wolf-Rayet phase star
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: star radius
        label_text: label text
        label_position: 'top', 'bottom', 'left', or 'right'
    """
    draw_star(ax, x, y, size=size, color=colors['WR'], edgecolor='black')
    add_label(ax, x, y, label_text, label_position=label_position)


def draw_supernova(ax, x, y, size=1.2, label_text='Supernova\n(BH/NS)', image_path='supernova.png'):
    """Draw a supernova explosion
    
    Args:
        ax: matplotlib axis
        x, y: position coordinates
        size: image size
        label_text: label text
        image_path: path to supernova image file
    """
    draw_supernova_image(ax, x, y, size=size, image_path=image_path)
    add_label(ax, x, y, label_text, label_position='right')
