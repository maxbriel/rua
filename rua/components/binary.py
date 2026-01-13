"""
Binary stellar system drawing functions.
Contains functions for drawing binary stars, mass transfer, and binary evolution phases.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
import numpy as np

from rua.utils.colors import colors
from rua.components import stellar, compact
from rua.components.decorator import label

# Default binary drawing function

def binary(x, y,
           primary,
           secondary,
           size_primary=0.25,
           size_secondary=0.2,
           separation=0.6, 
           colors_tuple=(colors['ZAMS'],
                         colors['lower_mass_ZAMS']),
           label_text='',
           ax=None):
    """Draw a binary star system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    primary : callable
        Function to draw the primary star.
    secondary : callable
        Function to draw the secondary star.
    size_primary : float, optional
        Radius of the primary star (default: 0.25).
    size_secondary : float, optional
        Radius of the secondary star (default: 0.2).
    separation : float, optional
        Distance between the stars (default: 0.6).
    colors_tuple : tuple, optional
        Tuple of (primary_color, secondary_color) (default: ZAMS colors).
    label_text : str, optional
        Text label to display near the binary (default: '').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()
    
    
    primary(x - separation/2, y,
            ax = ax,
            size=size_primary, color=colors_tuple[0])
    secondary(x + separation/2, y,
              ax = ax,
              size=size_secondary, color=colors_tuple[1])
    
    if label_text:
        label(ax, x, y,
              label_text=label_text,
              label_position='bottom',)

### Special Binary Phases ###

def common_envelope(x, y,
                    primary=stellar.star,
                    secondary=stellar.star,
                    primary_size=0.2,
                    secondary_size=0.15,
                    envelope_size=0.5,
                    separation=0.5,
                    label_text='Common\nEnvelope',
                    colors_tuple=(colors['ZAMS'], colors['WR'], colors['lower_mass_ZAMS']),
                    ax=None,):
    """Draw a common envelope phase with two stars inside.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    primary : callable, optional
        Function to draw the primary star (default: stellar.star).
    secondary : callable, optional
        Function to draw the secondary star (default: stellar.star).
    primary_size : float, optional
        Size of the primary core (default: 0.2).
    secondary_size : float, optional
        Size of the secondary core (default: 0.15).
    envelope_size : float, optional
        Size of the common envelope (default: 0.5).
    separation : float, optional
        Distance between the cores (default: 0.5).
    label_text : str, optional
        Text label to display near the system (default: 'Common\nEnvelope').
    colors_tuple : tuple, optional
        Tuple of (envelope_color, primary_core_color, secondary_core_color)
        (default: ZAMS, WR, lower_mass_ZAMS colors).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """ 
    
    ax = ax or plt.gca()
    ellipse_ce = Ellipse((x, y), width=envelope_size*2, height=envelope_size*1.5, 
                         facecolor=colors_tuple[0], alpha=0.6, 
                         edgecolor='black', linewidth=0.5, zorder=-3)
    ax.add_patch(ellipse_ce)
    primary(x - separation/2, y, size=primary_size, color=colors_tuple[1], ax=ax)
    secondary(x + separation/2, y, size=secondary_size, color=colors_tuple[2], ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def roche_lobe_overflow(x, y,
                        accretor=stellar.star,
                        flip=False,
                        donor_size=0.3,
                        accretor_size=0.25,
                        separation=0.8,
                        donor_color='orange', accretor_color='yellow', 
                        label_text='Roche Lobe\nOverflow',
                        ax=None):
    """Draw a Roche lobe overflow (RLO) binary system with teardrop-shaped donor.
    
    Creates a teardrop-shaped donor star with material flowing toward a companion star.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    accretor : callable, optional
        Function to draw the accretor star (default: stellar.star).
    flip : bool, optional
        If True, swap positions of donor and accretor (default: False).
    donor_size : float, optional
        Size of the donor star (default: 0.3).
    accretor_size : float, optional
        Size of the accretor star (default: 0.25).
    separation : float, optional
        Distance between the stars (default: 0.8).
    donor_color : str, optional
        Color of the donor star (default: 'orange').
    accretor_color : str, optional
        Color of the accretor star (default: 'yellow').
    label_text : str, optional
        Text label to display near the system (default: 'Roche Lobe\nOverflow').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Position donor and accretor (accretor on left, donor on right)
    if flip:
        accretor_x = x - separation/2
        donor_x = x + separation/2
    else:
        accretor_x = x + separation/2
        donor_x = x - separation/2
        
    accretor(accretor_x, y, size=accretor_size,     color=accretor_color, ax=ax)
    
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
    if flip:
        rotation_angle = np.pi * 5/4 
    else:
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
        label(ax, x, y, label_text, label_position='bottom')



####### COMMON BINARY TYPES ########

def HMS_HMS(x,y,
            size_primary=0.25,
            size_secondary=0.25,
            separation=0.7, 
            label_text='HMS + HMS',
            star_func=None,
            ax=None):
    """Draw a binary system with two hydrogen-burning main sequence stars.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_primary : float, optional
        Radius of the primary star (default: 0.25).
    size_secondary : float, optional
        Radius of the secondary star (default: 0.25).
    separation : float, optional
        Distance between the stars (default: 0.7).
    label_text : str, optional
        Text label to display near the binary (default: 'HMS + HMS').
    star_func : callable, optional
        Function to draw stars (default: None, uses stellar.star).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    if star_func is None:
        star_func = stellar.star
        
    if ax is None:
        ax = plt.gca()
    
    binary(x, y, size_primary=size_primary, size_secondary=size_secondary, separation=separation, 
           colors_tuple=(colors['ZAMS'], colors['ZAMS']), 
           label_text=label_text, primary=star_func, secondary=star_func, ax=ax)


# def CO_binary(ax, x, y, size_star=0.25, size_compact=0.15, separation=0.6, 
#               star_color=colors['ZAMS'], label_text='CO + MS/evolved\ncompanion',
#               star_func=None, compact_func=None):
#     """Draw a binary with a compact object and a star
    
#     Args:
#         ax: matplotlib axis
#         x, y: center position of binary system
#         size_star: radius of the star
#         size_compact: size of compact object
#         separation: distance between objects
#         star_color: color of the companion star
#         label_text: optional label text
#         star_func: callable to draw star (default: stellar.star)
#         compact_func: callable to draw compact object (default: compact.draw_compact_object)
#     """
#     if compact_func is None:
#         compact_func = compact.draw_compact_object
#     if star_func is None:
#         star_func = stellar.star
    
#     compact_func(ax, x - separation/2, y, size=size_compact)
#     star_func(ax, x + separation/2, y, size=size_star, color=star_color)
    
#     if label_text:
#         add_label(ax, x, y+separation, label_text, label_position='bottom')
    

# def BBH(ax, x, y, size_compact1=0.15, size_compact2=0.15, separation=0.6, 
#         label_text='BBH', bh_func=None):
#     """Draw a double compact object binary (binary black holes)
    
#     Args:
#         ax: matplotlib axis
#         x, y: center position of binary system
#         size_compact1: size of first black hole
#         size_compact2: size of second black hole
#         separation: distance between black holes
#         label_text: optional label text
#         bh_func: callable to draw black hole (default: compact.draw_BH)
#     """
#     if bh_func is None:
#         bh_func = compact.draw_BH
    
#     bh_func(ax, x - separation/2, y, size=size_compact1)
#     bh_func(ax, x + separation/2, y, size=size_compact2)
    
#     if label_text:
#         add_label(ax, x, y, label_text, label_position='bottom')


# def BH_binary(ax, x, y, size_bh=0.15, size_star=0.25, separation=0.6, 
#               star_color=colors['ZAMS'], label_text='BH + MS/evolved\ncompanion',
#               bh_func=None, star_func=None):
#     """Draw a binary with a black hole and a star
    
#     Args:
#         ax: matplotlib axis
#         x, y: center position of binary system
#         size_bh: size of black hole
#         size_star: radius of the star
#         separation: distance between objects
#         star_color: color of the companion star
#         label_text: optional label text
#         bh_func: callable to draw black hole (default: compact.draw_BH)
#         star_func: callable to draw star (default: stellar.star)
#     """
#     if bh_func is None:
#         bh_func = compact.draw_BH
#     if star_func is None:
#         star_func = stellar.star
    
#     bh_func(ax, x - separation/2, y, size=size_bh)
#     star_func(ax, x + separation/2, y, size=size_star, color=star_color)
    
#     if label_text:
#         add_label(ax, x, y, label_text, label_position='bottom')
    

# def SN_and_CO(ax, x, y, size_sn=0.3, size_compact=0.15, separation=0.6, 
#               co_type=None, flip=False, sn_func=None, bh_func=None, 
#               ns_func=None, compact_func=None):
#     """Draw a binary with a supernova and a compact object
    
#     Args:
#         ax: matplotlib axis
#         x, y: center position of binary system
#         size_sn: size of supernova explosion
#         size_compact: size of compact object
#         separation: distance between objects
#         co_type: 'BH', 'NS', or None for generic compact object
#         flip: if True, swap positions of supernova and compact object
#         sn_func: callable to draw supernova (default: stellar.supernova_image)
#         bh_func: callable to draw black hole (default: compact.draw_BH)
#         ns_func: callable to draw neutron star (default: compact.draw_NS)
#         compact_func: callable to draw compact object (default: compact.draw_compact_object)
#     """
#     if sn_func is None:
#         sn_func = stellar.supernova_image
#     if bh_func is None:
#         bh_func = compact.draw_BH
#     if ns_func is None:
#         ns_func = compact.draw_NS
#     if compact_func is None:
#         compact_func = compact.draw_compact_object
    
#     if flip:
#         left = x-separation/2
#         right = x+separation/2
#     else:
#         left = x+separation/2
#         right = x-separation/2
    
#     sn_func(ax, left, y, size=size_sn, image_path='supernova.png')
    
#     if co_type == 'BH':
#         bh_func(ax, right, y, size=size_compact)
#     elif co_type == 'NS':
#         ns_func(ax, right, y, size=size_compact)
#     else:
#         compact_func(ax, right, y, size=size_compact)
    

# def SN_and_star(ax, x, y, size_sn=0.3, size_star=0.25, separation=0.6, 
#                 star_color=colors['ZAMS'], sn_func=None, star_func=None):
#     """Draw a binary with a supernova and a star
    
#     Args:
#         ax: matplotlib axis
#         x, y: center position of binary system
#         size_sn: size of supernova explosion
#         size_star: radius of the star
#         separation: distance between objects
#         star_color: color of the companion star
#         sn_func: callable to draw supernova (default: stellar.supernova_image)
#         star_func: callable to draw star (default: stellar.star)
#     """
#     if sn_func is None:
#         sn_func = stellar.supernova_image
#     if star_func is None:
#         star_func = stellar.star
    
#     sn_func(ax, x - separation/2, y, size=size_sn, image_path='supernova.png')
#     star_func(ax, x + separation/2, y, size=size_star, color=star_color)



# def roche_lobe_overflow_BH(ax, x, y, donor_size=0.3, accretor_size=0.2, separation=0.8, 
#                            donor_color='orange', accretor_color='gray', 
#                            label_text='Roche Lobe\nOverflow', bh_func=None):
#     """Draw a Roche lobe overflow (RLO) binary system with BH accretor
    
#     Creates a teardrop-shaped donor star with material flowing toward a black hole.
    
#     Args:
#         ax: matplotlib axis
#         x, y: center position of binary system
#         donor_size: size of donor star
#         accretor_size: size of black hole accretor
#         separation: distance between objects
#         donor_color: color of donor star
#         accretor_color: color of accretor (not used for BH)
#         label_text: optional label text
#         bh_func: callable to draw black hole (default: compact.draw_BH)
#     """
#     if bh_func is None:
#         bh_func = compact.draw_BH
    
#     # Position donor and accretor (accretor on left, donor on right)
#     accretor_x = x - separation/2
#     donor_x = x + separation/2
    
#     bh_func(ax, accretor_x, y, size=accretor_size)

#     teardrop_points = []
#     n_points = 60
#     # Create 3/4 circle (from 0 to 3π/2, leaving top-right quadrant open)
#     circle_start_angle = 0
#     circle_end_angle = 3/2 * np.pi
#     for i in range(n_points):
#         angle = circle_start_angle + i * (circle_end_angle - circle_start_angle) / (n_points - 1)
#         px = donor_x + donor_size * np.cos(angle)
#         py = y + donor_size * np.sin(angle)
#         teardrop_points.append([px, py])
    
#     # Add the pointing tip in the missing quadrant (top-right corner)
#     tip_x = donor_x + donor_size * 1  # Adjust 0.7 to control how far the point extends
#     tip_y = y - donor_size
#     teardrop_points.append([tip_x, tip_y])

#     rotation_angle = np.pi * 5/4  # 225 degrees in radians
#     cos_theta = np.cos(rotation_angle)
#     sin_theta = np.sin(rotation_angle)
#     rotated_points = []
#     for px, py in teardrop_points:
#         # Translate to origin
#         px_rel = px - donor_x
#         py_rel = py - y
#         # Rotate
#         px_rot = px_rel * cos_theta - py_rel * sin_theta
#         py_rot = px_rel * sin_theta + py_rel * cos_theta
#         # Translate back
#         rotated_points.append([px_rot + donor_x, py_rot + y])
#     teardrop_points = rotated_points
    
#     # Create and draw pear shape
#     pear = Polygon(teardrop_points, facecolor=donor_color,
#                    edgecolor='black', linewidth=0.5, zorder=3)
#     ax.add_patch(pear)
    
#     # Add label
#     if label_text:
#         add_label(ax, x, y, label_text, label_position='bottom')


