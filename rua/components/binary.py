"""
Binary stellar system drawing functions.
Contains functions for drawing binary stars, mass transfer, and binary evolution phases.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
import numpy as np

from rua.utils.colors import colors
from rua.components.stellar import draw_star, draw_supernova_image
from rua.components.compact import draw_compact_object, draw_NS, draw_BH
from rua.components.decorator import add_label


def draw_binary(ax, x, y, size1=0.25, size2=0.2, separation=0.6, colors_tuple=(colors['ZAMS'], colors['lower_mass_ZAMS']), label=''):
    """Draw a binary star system
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        size1: radius of primary star
        size2: radius of secondary star
        separation: distance between stars
        colors_tuple: tuple of (primary_color, secondary_color)
        label: optional label text
    """
    draw_star(ax, x - separation/2, y, size=size1, color=colors_tuple[0])
    draw_star(ax, x + separation/2, y, size=size2, color=colors_tuple[1])
    
    add_label(ax, x, y, label, 'bottom')


def draw_CO_binary(ax, x, y, size_star=0.25, size_compact=0.15, separation=0.6, star_color=colors['ZAMS']):
    """Draw a binary with a compact object and a star
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        size_star: radius of the star
        size_compact: size of compact object
        separation: distance between objects
        star_color: color of the companion star
    """
    draw_compact_object(ax, x - separation/2, y, size=size_compact)
    draw_star(ax, x + separation/2, y, size=size_star, color=star_color)
    
    add_label(ax, x, y+separation, 'CO + MS/evolved\ncompanion', label_position='bottom')
    

def draw_BBH(ax, x, y, size_compact1=0.15, size_compact2=0.15, separation=0.6, label_text=''):
    """Draw a double compact object binary (binary black holes)
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        size_compact1: size of first black hole
        size_compact2: size of second black hole
        separation: distance between black holes
        label_text: optional label text
    """
    draw_BH(ax, x - separation/2, y, size=size_compact1)
    draw_BH(ax, x + separation/2, y, size=size_compact2)
    
    add_label(ax, x, y, label_text or 'BBH', label_position='bottom')


def draw_BH_binary(ax, x, y, size_bh=0.15, size_star=0.25, separation=0.6, star_color=colors['ZAMS'], label_text=''):
    """Draw a binary with a black hole and a star
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        size_bh: size of black hole
        size_star: radius of the star
        separation: distance between objects
        star_color: color of the companion star
        label_text: optional label text
    """
    draw_BH(ax, x - separation/2, y, size=size_bh)
    draw_star(ax, x + separation/2, y, size=size_star, color=star_color)
    
    add_label(ax, x, y, label_text or 'BH + MS/evolved\ncompanion', label_position='bottom')
    

def draw_SN_and_CO(ax, x, y, size_sn=0.3, size_compact=0.15, separation=0.6, co_type=None, flip=False):
    """Draw a binary with a supernova and a compact object
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        size_sn: size of supernova explosion
        size_compact: size of compact object
        separation: distance between objects
        co_type: 'BH', 'NS', or None for generic compact object
        flip: if True, swap positions of supernova and compact object
    """
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
    

def draw_SN_and_star(ax, x, y, size_sn=0.3, size_star=0.25, separation=0.6, star_color=colors['ZAMS']):
    """Draw a binary with a supernova and a star
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        size_sn: size of supernova explosion
        size_star: radius of the star
        separation: distance between objects
        star_color: color of the companion star
    """
    draw_supernova_image(ax, x - separation/2, y, size=size_sn, image_path='supernova.png')
    draw_star(ax, x + separation/2, y, size=size_star, color=star_color)


def draw_zams_binary(ax, x, y, size1=0.3, size2=0.25, separation=0.7, label_text='Binary ZAMS'):
    """Draw a ZAMS binary system
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        size1: radius of primary star
        size2: radius of secondary star
        separation: distance between stars
        label_text: optional label text
    """
    draw_binary(ax, x, y, size1=size1, size2=size2, separation=separation, 
                colors_tuple=(colors['ZAMS'], colors['lower_mass_ZAMS']), label=label_text)


def draw_common_envelope(ax, x, y, envelope_size=0.5, star_sizes=(0.15, 0.15),
                         label_text='Common\nEnvelope',
                         colors_tuple=(colors['ZAMS'],
                                 colors['WR'],
                                 colors['lower_mass_ZAMS']
                                 )
                         ):
    """Draw a common envelope phase with two stars inside
    
    Args:
        ax: matplotlib axis
        x, y: center position of system
        envelope_size: size of the envelope
        star_sizes: tuple of (primary_size, secondary_size)
        label_text: optional label text
        colors_tuple: tuple of (envelope_color, primary_core_color, secondary_core_color)
    """
    ellipse_ce = Ellipse((x, y), width=envelope_size*2, height=envelope_size*1.5, 
                         facecolor=colors_tuple[0], alpha=0.6, 
                         edgecolor='black', linewidth=0.5, zorder=2)
    ax.add_patch(ellipse_ce)
    draw_star(ax, x - 0.2, y, size=star_sizes[0], color=colors_tuple[1])
    draw_star(ax, x + 0.2, y, size=star_sizes[1], color=colors_tuple[2])
    
    add_label(ax, x, y, label_text, label_position='bottom')


def draw_roche_lobe_overflow_BH(ax, x, y, donor_size=0.3, accretor_size=0.2, separation=0.8, 
                              donor_color='orange', accretor_color='gray', label_text='Roche Lobe\nOverflow'):
    """Draw a Roche lobe overflow (RLO) binary system with BH accretor
    
    Creates a teardrop-shaped donor star with material flowing toward a black hole.
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        donor_size: size of donor star
        accretor_size: size of black hole accretor
        separation: distance between objects
        donor_color: color of donor star
        accretor_color: color of accretor (not used for BH)
        label_text: optional label text
    """
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

    rotation_angle = np.pi * 5/4  # 225 degrees in radians
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
    
    Creates a teardrop-shaped donor star with material flowing toward a companion star.
    
    Args:
        ax: matplotlib axis
        x, y: center position of binary system
        donor_size: size of donor star
        accretor_size: size of accretor star
        separation: distance between stars
        donor_color: color of donor star
        accretor_color: color of accretor star
        label_text: optional label text
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
