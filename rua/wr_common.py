#!/usr/bin/env python3
"""
Common plotting functions for Wolf-Rayet stellar evolution diagrams.
Contains reusable functions for drawing stars, binaries, arrows, and various stellar phases.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Circle
from matplotlib.patches import Polygon, Ellipse
import matplotlib.image as mpimg
import numpy as np
import os

def draw_star(ax, x, y, size=0.3, color='yellow', edgecolor='black', label='', hatch=None):
    """Draw a cartoon star representation"""
    circle = Circle((x, y), size, facecolor=color, edgecolor=edgecolor, linewidth=0.5, zorder=3, hatch=hatch)
    ax.add_patch(circle)
    return circle


def draw_binary(ax, x, y, size1=0.25, size2=0.2, separation=0.6, colors=(colors['zams'], colors['lower_mass_zams']), label=''):
    """Draw a binary star system"""
    draw_star(ax, x - separation/2, y, size=size1, color=colors[0])
    draw_star(ax, x + separation/2, y, size=size2, color=colors[1])
    
    add_label(ax, x, y, label, 'bottom')

def draw_CO_binary(ax, x, y, size_star=0.25, size_compact=0.15, separation=0.6, star_color=colors['zams']):
    """Draw a binary with a compact object and a star"""
    draw_compact_object(ax, x - separation/2, y, size=size_compact)
    draw_star(ax, x + separation/2, y, size=size_star, color=star_color)
    
    add_label(ax, x, y+separation, 'CO + MS/evolved\ncompanion', label_position='bottom')
    
def draw_BBH(ax, x, y, size_compact1=0.15, size_compact2=0.15, separation=0.6, label_text='',):
    """Draw a double compact object binary"""
    draw_BH(ax, x - separation/2, y, size=size_compact1)
    draw_BH(ax, x + separation/2, y, size=size_compact2)
    
    add_label(ax, x, y, label_text or 'BBH', label_position='bottom')

def draw_BH_binary(ax, x, y, size_bh=0.15, size_star=0.25, separation=0.6, star_color=colors['zams'], label_text=''):
    """Draw a binary with a black hole and a star"""
    draw_BH(ax, x - separation/2, y, size=size_bh)
    draw_star(ax, x + separation/2, y, size=size_star, color=star_color)
    
    add_label(ax, x, y, label_text or 'BH + MS/evolved\ncompanion', label_position='bottom')
    
def draw_SN_and_CO(ax, x, y, size_sn=0.3, size_compact=0.15, separation=0.6, co_type=None, flip=False):
    """Draw a binary with a supernova and a compact object"""
    if flip:
        left = x-separation/2
        right = x+separation/2
    else:
        left = x+separation/2
        right = x-separation/2
    
    draw_supernova_image(ax, left, y, size=size_sn, image_path='supernova.png')
    
    if co_type == 'BH':
        draw_BH(ax, right, y, size=size_compact)
    elif co_type == 'NS':
        draw_NS(ax, right, y, size=size_compact)
    else:
        draw_compact_object(ax, right, y, size=size_compact)
        
    #add_label(ax, x, y+separation-0.15, 'Supernova', label_position='bottom')
    
    
def draw_SN_and_star(ax, x, y, size_sn=0.3, size_star=0.25, separation=0.6, star_color=colors['zams']):
    """Draw a binary with a supernova and a star"""
    draw_supernova_image(ax, x - separation/2, y, size=size_sn, image_path='supernova.png')
    draw_star(ax, x + separation/2, y, size=size_star, color=star_color)


def draw_arrow(ax, x1, y1, x2, y2, label='', style='solid', color='black', width=2, label_position='right'):
    """Draw an arrow between two points"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=20, 
                           linewidth=width, color=color,
                           linestyle=style, zorder=2)
    ax.add_patch(arrow)
    
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        
        # Label position offsets
        label_offset = 0.4
        positions = {
            'right': (mid_x + label_offset-0.2, mid_y, 'left'),
            'left': (mid_x - label_offset+0.2, mid_y, 'right'),
            'top': (mid_x, mid_y + label_offset-0.2, 'center'),
            'bottom': (mid_x, mid_y - label_offset, 'center')
        }
        
        label_x, label_y, ha = positions.get(label_position, positions['right'])
        ax.text(label_x, label_y, label, ha=ha, fontsize=8, 
                style='italic', bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.8))


def draw_supernova_image(ax, x, y, size=1.0, image_path='supernova.png'):
    """Display supernova PNG image at specified location"""
    if os.path.exists(image_path):
        img = mpimg.imread(image_path)
        # Calculate extent to center the image at (x, y) with given size
        extent = [x - size/2, x + size/2, y - size/2, y + size/2]
        ax.imshow(img, extent=extent, aspect='auto', zorder=3)
    else:
        # Fallback to drawing a simple star if image not found
        draw_star(ax, x, y, size=size/2, color='orange', edgecolor='red')


# Phase-specific plotting functions
# Position offsets for the label


def add_label(ax, x, y, label_text, label_position):
    """Add label to the star at specified position"""
    offset = 0.4
    positions = {
        'bottom': lambda x,y: (x, y - offset, 'center', 'top'),
        'top': lambda x,y: (x, y + offset, 'center', 'bottom'),
        'left': lambda x,y: (x - offset, y, 'center', 'center'),
        'right': lambda x,y: (x + offset, y, 'center', 'center')
    }
    
    label_x, label_y, ha, va = positions.get(label_position, positions['bottom'])(x, y)
    ax.text(label_x, label_y, label_text, ha=ha, va=va, fontweight='bold')


# SINGLE STAR SPECIFIC FUNCTIONS

def draw_zams_star(ax, x, y, size=0.4, label_text='ZAMS\n(Main Sequence)', label_position='bottom'):
    """Draw a ZAMS (Zero Age Main Sequence) star
    
    Args:
        label_position: 'top', 'bottom', 'left', or 'right'
    """
    draw_star(ax, x, y, size=size, color=colors['zams'], edgecolor='black')
    add_label(ax, x, y, label_text, label_position)

def draw_wr_star(ax, x, y, size=0.45, label_text='WR Phase\n(He-burning)', label_position='right'):
    """Draw a Wolf-Rayet phase star"""
    draw_star(ax, x, y, size=size, color=colors['wr'], edgecolor='black')
    add_label(ax, x, y, label_text, label_position=label_position)

def draw_supernova(ax, x, y, size=1.2, label_text='Supernova\n(BH/NS)', image_path='supernova.png'):
    """Draw a supernova explosion"""
    draw_supernova_image(ax, x, y, size=size, image_path=image_path)
    add_label(ax, x, y, label_text, label_position='right')

def draw_NS(ax, x, y, size=0.1, label_text='Neutron Star'):
    """Draw neutron star with radial gradient (white to light blue)"""
    draw_star(ax, x, y, size=0.1, color=colors['neutron_star_outer'], edgecolor='black')  # Outer: powder blue
    draw_star(ax, x, y, size=0.07, color=colors['neutron_star_middle'], edgecolor='none')  # Middle: very light blue
    draw_star(ax, x, y, size=0.04, color=colors['neutron_star_inner'], edgecolor='none')  # Inner: near white (alice blue)

def draw_BH(ax, x, y, size=0.2, label_text='Black Hole'):
    """Draw black hole"""
    draw_star(ax, x, y, size=size, color=colors['black_hole'], edgecolor='black')  # Outer: dark gray

def draw_compact_object(ax, x, y, size=0.2, label_text='', label_position='right'):
    """Draw a compact object (neutron star or black hole)"""
    # Neutron star
    ns_x, ns_y = x-0.3, y
    bh_x, bh_y = x+0.3, y
    
    draw_NS(ax, ns_x, ns_y, size=0.1)
    ax.text(x-0.05, y, '/', ha='center', va='center', fontsize=20, fontweight='bold')
    draw_BH(ax, bh_x, bh_y, size=size)
    
    if label_text:
        add_label(ax, x, y, label_text, label_position=label_position)

# BINARY SPECIFIC DRAWING FUNCTIONS

def draw_zams_binary(ax, x, y, size1=0.3, size2=0.25, separation=0.7, label_text='Binary ZAMS'):
    """Draw a ZAMS binary system"""
    draw_binary(ax, x, y, size1=size1, size2=size2, separation=separation, 
                colors=(colors['zams'], colors['lower_mass_zams']), label=label_text)


def draw_common_envelope(ax, x, y, envelope_size=0.5, star_sizes=(0.15, 0.15),
                         label_text='Common\nEnvelope',
                         colors=(colors['zams'],
                                 colors['wr'],
                                 colors['lower_mass_zams']
                                 )
                         ):
    """Draw a common envelope phase with two stars inside"""
    ellipse_ce = Ellipse((x, y), width=envelope_size*2, height=envelope_size*1.5, 
                         facecolor=colors[0], alpha=0.6, 
                         edgecolor='black', linewidth=0.5, zorder=2)
    ax.add_patch(ellipse_ce)
    draw_star(ax, x - 0.2, y, size=star_sizes[0], color=colors[1])
    draw_star(ax, x + 0.2, y, size=star_sizes[1], color=colors[2])
    
    add_label(ax, x, y, label_text, label_position='bottom')


def draw_roche_lobe_overflow_BH(ax, x, y, donor_size=0.3, accretor_size=0.2, separation=0.8, 
                              donor_color='orange', accretor_color='gray', label_text='Roche Lobe\nOverflow'):
    """Draw a Roche lobe overflow (RLO) binary system with BH accretor """
    
    # Position donor and accretor (accretor on left, donor on right)
    accretor_x = x - separation/2
    donor_x = x + separation/2
    
    
    draw_BH(ax, accretor_x, y, size=accretor_size)

    teardrop_points = []
    n_points = 60
    # Create 3/4 circle (from 0 to 3π/2, leaving top-right quadrant open)
    circle_start_angle = 0
    circle_end_angle = 3/2 * np.pi
    for i in range(n_points):
        angle = circle_start_angle + i * (circle_end_angle - circle_start_angle) / (n_points - 1)
        px = donor_x + donor_size * np.cos(angle)
        py = y + donor_size * np.sin(angle)
        teardrop_points.append([px, py])
    
    # Add the pointing tip in the missing quadrant (top-right corner)
    tip_x = donor_x + donor_size * 1  # Adjust 0.7 to control how far the point extends
    tip_y = y - donor_size
    teardrop_points.append([tip_x, tip_y])

    rotation_angle = np.pi * 5/4  # 45 degrees in radians
    cos_theta = np.cos(rotation_angle)
    sin_theta = np.sin(rotation_angle)
    rotated_points = []
    for px, py in teardrop_points:
        # Translate to origin
        px_rel = px - donor_x
        py_rel = py - y
        # Rotate
        px_rot = px_rel * cos_theta - py_rel * sin_theta
        py_rot = px_rel * sin_theta + py_rel * cos_theta
        # Translate back
        rotated_points.append([px_rot + donor_x, py_rot + y])
    teardrop_points = rotated_points
    # Create and draw pear shape
    pear = Polygon(teardrop_points, facecolor=donor_color,
                   edgecolor='black', linewidth=0.5, zorder=3)
    ax.add_patch(pear)
    # Add label
    if label_text:
        add_label(ax, x, y, label_text, label_position='bottom')

    
    
    


def draw_roche_lobe_overflow(ax, x, y, donor_size=0.3, accretor_size=0.25, separation=0.8, 
                              donor_color='orange', accretor_color='yellow', label_text='Roche Lobe\nOverflow'):
    """Draw a Roche lobe overflow (RLO) binary system with teardrop-shaped donor
    
    Args:
        ax: matplotlib axis
        x, y: center position of the binary system
        donor_size: size of the donor star (left)
        accretor_size: size of the accretor star (right)
        separation: separation between stars
        donor_color: color of donor star
        accretor_color: color of accretor star
        label_text: label for the system
    """
    # Position donor and accretor (accretor on left, donor on right)
    accretor_x = x + separation/2
    donor_x = x - separation/2
        
    draw_star(ax, accretor_x, y, size=accretor_size, color=accretor_color)
    
    # Create pear/bulb shape: large rounded bulb on left, narrow on right
    teardrop_points = []
    
    n_points = 60
    
    # Create 3/4 circle (from 0 to 3π/2, leaving top-right quadrant open)
    circle_start_angle = 0
    circle_end_angle = 3/2 * np.pi
    
    for i in range(n_points):
        angle = circle_start_angle + i * (circle_end_angle - circle_start_angle) / (n_points - 1)
        px = donor_x + donor_size * np.cos(angle)
        py = y + donor_size * np.sin(angle)
        teardrop_points.append([px, py])
    
    # Add the pointing tip in the missing quadrant (top-right corner)
    # This creates the teardrop point toward the accretor
    tip_x = donor_x + donor_size * 1  # Adjust 0.7 to control how far the point extends
    tip_y = y - donor_size 
    teardrop_points.append([tip_x, tip_y])
    
    # Rotate all points by 45 degrees around donor center
    rotation_angle = np.pi / 4  # 45 degrees in radians
    cos_theta = np.cos(rotation_angle)
    sin_theta = np.sin(rotation_angle)
    
    rotated_points = []
    for px, py in teardrop_points:
        # Translate to origin
        px_rel = px - donor_x
        py_rel = py - y
        # Rotate
        px_rot = px_rel * cos_theta - py_rel * sin_theta
        py_rot = px_rel * sin_theta + py_rel * cos_theta
        # Translate back
        rotated_points.append([px_rot + donor_x, py_rot + y])
    
    teardrop_points = rotated_points
            
    
    # Create and draw pear shape
    pear = Polygon(teardrop_points, facecolor=donor_color, 
                   edgecolor='black', linewidth=0.5, zorder=3)
    ax.add_patch(pear)

    # Add label
    if label_text:
        add_label(ax, x, y, label_text, label_position='bottom')
