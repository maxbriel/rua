"""
Binary stellar system drawing functions.
Contains functions for drawing binary stars, mass transfer, and binary evolution phases.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Circle, Wedge, FancyArrowPatch
from matplotlib.transforms import Affine2D

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
        Text label to display near the system (default: 'Common Envelope').
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
        Text label to display near the system (default: 'Roche Lobe Overflow').
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


def HeMS_HMS(x, y, size_primary=0.25, size_secondary=0.25, separation=0.7,
             label_text='HeMS + HMS', ax=None):
    """Draw a binary system with a helium main sequence star and hydrogen main sequence star.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_primary : float, optional
        Radius of the HeMS star (default: 0.25).
    size_secondary : float, optional
        Radius of the HMS star (default: 0.25).
    separation : float, optional
        Distance between the stars (default: 0.7).
    label_text : str, optional
        Text label to display near the binary (default: 'HeMS + HMS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    binary(x, y, size_primary=size_primary, size_secondary=size_secondary, 
           separation=separation, colors_tuple=(colors['HeMS'], colors['ZAMS']),
           label_text=label_text, primary=stellar.star, secondary=stellar.star, ax=ax)


def WR_HMS(x, y, size_primary=0.2, size_secondary=0.3, separation=0.7,
           label_text='WR + HMS', ax=None):
    """Draw a binary system with a Wolf-Rayet star and hydrogen main sequence star.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_primary : float, optional
        Radius of the WR star (default: 0.2).
    size_secondary : float, optional
        Radius of the HMS star (default: 0.3).
    separation : float, optional
        Distance between the stars (default: 0.7).
    label_text : str, optional
        Text label to display near the binary (default: 'WR + HMS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    binary(x, y, size_primary=size_primary, size_secondary=size_secondary,
           separation=separation, colors_tuple=(colors['WR'], colors['ZAMS']),
           label_text=label_text, primary=stellar.star, secondary=stellar.star, ax=ax)


def BH_HMS(x, y, size_bh=0.15, size_star=0.3, separation=0.7,
           label_text='BH + HMS', ax=None):
    """Draw a binary system with a black hole and hydrogen main sequence star.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_bh : float, optional
        Size of the black hole (default: 0.15).
    size_star : float, optional
        Radius of the HMS star (default: 0.3).
    separation : float, optional
        Distance between the objects (default: 0.7).
    label_text : str, optional
        Text label to display near the binary (default: 'BH + HMS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.BH(x - separation/2, y, size=size_bh, label_text='', ax=ax)
    stellar.star(x + separation/2, y, size=size_star, color=colors['ZAMS'], ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def NS_HMS(x, y, size_ns=0.1, size_star=0.3, separation=0.7,
           label_text='NS + HMS', ax=None):
    """Draw a binary system with a neutron star and hydrogen main sequence star.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_ns : float, optional
        Size of the neutron star (default: 0.1).
    size_star : float, optional
        Radius of the HMS star (default: 0.3).
    separation : float, optional
        Distance between the objects (default: 0.7).
    label_text : str, optional
        Text label to display near the binary (default: 'NS + HMS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.NS(x - separation/2, y, size=size_ns, label_text='', ax=ax)
    stellar.star(x + separation/2, y, size=size_star, color=colors['ZAMS'], ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def BBH(x, y, size1=0.15, size2=0.15, separation=0.5,
        label_text='BBH', ax=None):
    """Draw a Binary Black Hole (BBH) system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size1 : float, optional
        Size of the first black hole (default: 0.15).
    size2 : float, optional
        Size of the second black hole (default: 0.15).
    separation : float, optional
        Distance between the black holes (default: 0.5).
    label_text : str, optional
        Text label to display near the binary (default: 'BBH').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.BH(x - separation/2, y, size=size1, label_text='', ax=ax)
    compact.BH(x + separation/2, y, size=size2, label_text='', ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def BNS(x, y, size1=0.1, size2=0.1, separation=0.4,
        label_text='BNS', ax=None):
    """Draw a Binary Neutron Star (BNS) system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size1 : float, optional
        Size of the first neutron star (default: 0.1).
    size2 : float, optional
        Size of the second neutron star (default: 0.1).
    separation : float, optional
        Distance between the neutron stars (default: 0.4).
    label_text : str, optional
        Text label to display near the binary (default: 'BNS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.NS(x - separation/2, y, size=size1, label_text='', ax=ax)
    compact.NS(x + separation/2, y, size=size2, label_text='', ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


# Alias for BNS
NS_NS = BNS


def BH_NS(x, y, size_bh=0.15, size_ns=0.1, separation=0.5,
          label_text='BH + NS', ax=None):
    """Draw a Black Hole - Neutron Star binary system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_bh : float, optional
        Size of the black hole (default: 0.15).
    size_ns : float, optional
        Size of the neutron star (default: 0.1).
    separation : float, optional
        Distance between the objects (default: 0.5).
    label_text : str, optional
        Text label to display near the binary (default: 'BH + NS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.BH(x - separation/2, y, size=size_bh, label_text='', ax=ax)
    compact.NS(x + separation/2, y, size=size_ns, label_text='', ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def WD_WD(x, y, size1=0.12, size2=0.12, separation=0.4,
          label_text='WD + WD', ax=None):
    """Draw a Double White Dwarf binary system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size1 : float, optional
        Size of the first white dwarf (default: 0.12).
    size2 : float, optional
        Size of the second white dwarf (default: 0.12).
    separation : float, optional
        Distance between the white dwarfs (default: 0.4).
    label_text : str, optional
        Text label to display near the binary (default: 'WD + WD').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.WD(x - separation/2, y, size=size1, label_text='', ax=ax)
    compact.WD(x + separation/2, y, size=size2, label_text='', ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def WD_HMS(x, y, size_wd=0.1, size_star=0.25, separation=0.6,
           label_text='WD + HMS', ax=None):
    """Draw a White Dwarf + Main Sequence binary system (CV progenitor).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_wd : float, optional
        Size of the white dwarf (default: 0.1).
    size_star : float, optional
        Radius of the HMS star (default: 0.25).
    separation : float, optional
        Distance between the objects (default: 0.6).
    label_text : str, optional
        Text label to display near the binary (default: 'WD + HMS').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.WD(x - separation/2, y, size=size_wd, label_text='', ax=ax)
    stellar.star(x + separation/2, y, size=size_star, color=colors['lower_mass_ZAMS'], ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def AM_CVn(x, y, size_accretor=0.1, size_donor=0.08, separation=0.4,
           label_text='AM CVn', ax=None):
    """Draw an AM CVn system (WD + He WD with mass transfer).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_accretor : float, optional
        Size of the accreting white dwarf (default: 0.1).
    size_donor : float, optional
        Size of the He donor (default: 0.08).
    separation : float, optional
        Distance between the objects (default: 0.4).
    label_text : str, optional
        Text label to display near the binary (default: 'AM CVn').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    # Accretor WD with disk
    accretion_disk(x - separation/2, y, inner_radius=size_accretor, 
                   outer_radius=size_accretor * 2, ax=ax)
    compact.WD(x - separation/2, y, size=size_accretor, label_text='', ax=ax)
    # Helium donor
    stellar.star(x + separation/2, y, size=size_donor, color=colors['HeMS'], ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def symbiotic_binary(x, y, size_wd=0.1, size_giant=0.4, separation=0.8,
                     label_text='Symbiotic Binary', ax=None):
    """Draw a symbiotic binary system (WD + Red Giant).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_wd : float, optional
        Size of the white dwarf (default: 0.1).
    size_giant : float, optional
        Radius of the red giant (default: 0.4).
    separation : float, optional
        Distance between the objects (default: 0.8).
    label_text : str, optional
        Text label to display near the binary (default: 'Symbiotic Binary').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    compact.WD(x - separation/2, y, size=size_wd, label_text='', ax=ax)
    stellar.star(x + separation/2, y, size=size_giant, color=colors['RGB'], 
                 edgecolor='darkred', ax=ax)
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def HMXB(x, y, size_co=0.12, size_star=0.35, separation=0.8, co_type='BH',
         label_text='HMXB', ax=None):
    """Draw a High Mass X-ray Binary system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_co : float, optional
        Size of the compact object (default: 0.12).
    size_star : float, optional
        Radius of the massive star (default: 0.35).
    separation : float, optional
        Distance between the objects (default: 0.8).
    co_type : str, optional
        Type of compact object: 'BH' or 'NS' (default: 'BH').
    label_text : str, optional
        Text label to display near the binary (default: 'HMXB').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Compact object with accretion disk
    accretion_disk(x - separation/2, y, inner_radius=size_co, 
                   outer_radius=size_co * 2.5, ax=ax)
    if co_type == 'NS':
        compact.NS(x - separation/2, y, size=size_co, label_text='', ax=ax)
    else:
        compact.BH(x - separation/2, y, size=size_co, label_text='', ax=ax)
    
    # Massive companion
    stellar.star(x + separation/2, y, size=size_star, 
                 color=colors['HMXB_star'], edgecolor='darkred', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def LMXB(x, y, size_co=0.1, size_star=0.2, separation=0.6, co_type='NS',
         label_text='LMXB', ax=None):
    """Draw a Low Mass X-ray Binary system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_co : float, optional
        Size of the compact object (default: 0.1).
    size_star : float, optional
        Radius of the low-mass star (default: 0.2).
    separation : float, optional
        Distance between the objects (default: 0.6).
    co_type : str, optional
        Type of compact object: 'BH' or 'NS' (default: 'NS').
    label_text : str, optional
        Text label to display near the binary (default: 'LMXB').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Compact object with accretion disk
    accretion_disk(x - separation/2, y, inner_radius=size_co, 
                   outer_radius=size_co * 2.5, ax=ax)
    if co_type == 'BH':
        compact.BH(x - separation/2, y, size=size_co, label_text='', ax=ax)
    else:
        compact.NS(x - separation/2, y, size=size_co, label_text='', ax=ax)
    
    # Low-mass companion
    stellar.star(x + separation/2, y, size=size_star, 
                 color=colors['LMXB_star'], edgecolor='darkorange', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


def cataclysmic_variable(x, y, size_wd=0.1, size_donor=0.2, separation=0.5,
                         disk_size=0.2, label_text='CV', ax=None):
    """Draw a Cataclysmic Variable system (WD accreting from donor).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_wd : float, optional
        Size of the white dwarf (default: 0.1).
    size_donor : float, optional
        Radius of the donor star (default: 0.2).
    separation : float, optional
        Distance between the objects (default: 0.5).
    disk_size : float, optional
        Outer radius of the accretion disk (default: 0.2).
    label_text : str, optional
        Text label to display near the binary (default: 'CV').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # WD with accretion disk
    accretion_disk(x - separation/2, y, inner_radius=size_wd, 
                   outer_radius=disk_size, ax=ax)
    compact.WD(x - separation/2, y, size=size_wd, label_text='', ax=ax)
    
    # Donor star
    stellar.star(x + separation/2, y, size=size_donor, 
                 color=colors['lower_mass_ZAMS'], ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom')


# Alias for cataclysmic_variable
CV = cataclysmic_variable


def contact_binary(x, y, size1=0.3, size2=0.25, overlap=0.1,
                   label_text='Contact Binary', ax=None):
    """Draw a contact binary system (two stars sharing envelope).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size1 : float, optional
        Radius of the primary star (default: 0.3).
    size2 : float, optional
        Radius of the secondary star (default: 0.25).
    overlap : float, optional
        Amount of overlap between stars (default: 0.1).
    label_text : str, optional
        Text label to display near the binary (default: 'Contact Binary').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Calculate positions with overlap
    separation = size1 + size2 - overlap
    
    # Draw contact envelope (figure-8 shape using ellipse approximation)
    envelope_width = separation + size1 + size2
    envelope_height = max(size1, size2) * 1.8
    envelope = Ellipse((x, y), width=envelope_width, height=envelope_height,
                        facecolor=colors['contact'], alpha=0.4, 
                        edgecolor='darkorange', linewidth=0.5, zorder=1)
    ax.add_patch(envelope)
    
    # Draw the two stars
    stellar.star(x - separation/2, y, size=size1, color=colors['contact'], 
                 edgecolor='darkorange', ax=ax)
    stellar.star(x + separation/2, y, size=size2, color=colors['contact'], 
                 edgecolor='darkorange', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom', 
              label_offset=envelope_height/2 + 0.2)


def overcontact_binary(x, y, size=0.5, label_text='Overcontact Binary', ax=None):
    """Draw an overcontact binary (both stars overfilling Roche lobes).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size : float, optional
        Overall size of the system (default: 0.5).
    label_text : str, optional
        Text label to display near the binary (default: 'Overcontact Binary').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw peanut-shaped envelope
    envelope = Ellipse((x, y), width=size*2.5, height=size*1.5,
                        facecolor=colors['contact'], alpha=0.6, 
                        edgecolor='darkorange', linewidth=1, zorder=1)
    ax.add_patch(envelope)
    
    # Draw cores
    stellar.star(x - size*0.5, y, size=size*0.4, color='orange', 
                 edgecolor='darkorange', ax=ax)
    stellar.star(x + size*0.5, y, size=size*0.35, color='orange', 
                 edgecolor='darkorange', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom', 
              label_offset=size*0.75 + 0.2)


def detached_binary(x, y, size1=0.25, size2=0.2, separation=1.0,
                    label_text='Detached Binary', ax=None):
    """Draw a detached binary system (well-separated stars).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size1 : float, optional
        Radius of the primary star (default: 0.25).
    size2 : float, optional
        Radius of the secondary star (default: 0.2).
    separation : float, optional
        Distance between the stars (default: 1.0).
    label_text : str, optional
        Text label to display near the binary (default: 'Detached Binary').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    binary(x, y, size_primary=size1, size_secondary=size2, separation=separation,
           colors_tuple=(colors['ZAMS'], colors['lower_mass_ZAMS']),
           label_text=label_text, primary=stellar.star, secondary=stellar.star, ax=ax)


def semi_detached_binary(x, y, size_donor=0.3, size_accretor=0.25, separation=0.8,
                         label_text='Semi-Detached', ax=None):
    """Draw a semi-detached binary system (one star filling Roche lobe).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary system center.
    y : float
        Y-coordinate of the binary system center.
    size_donor : float, optional
        Size of the Roche-lobe filling donor (default: 0.3).
    size_accretor : float, optional
        Radius of the accretor star (default: 0.25).
    separation : float, optional
        Distance between the objects (default: 0.8).
    label_text : str, optional
        Text label to display near the binary (default: 'Semi-Detached').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    roche_lobe_overflow(x, y, donor_size=size_donor, accretor_size=size_accretor,
                        separation=separation, label_text=label_text, ax=ax)


# ============================================================================
# MASS TRANSFER AND ACCRETION COMPONENTS
# ============================================================================

def accretion_disk(x, y, inner_radius=0.1, outer_radius=0.3, 
                   inclination=0.9, label_text='', label_position='bottom',
                   label_offset=None, ax=None):
    """Draw an accretion disk around a compact object.
    
    The disk is rendered in two halves to create a 3D effect: the back half 
    appears behind the central star (zorder=2), and the front half appears 
    in front of it (zorder=5).
    
    Parameters
    ----------
    x : float
        X-coordinate of the disk center.
    y : float
        Y-coordinate of the disk center.
    inner_radius : float, optional
        Inner radius of the disk (default: 0.1).
    outer_radius : float, optional
        Outer radius of the disk (default: 0.3).
    inclination : float, optional
        Disk inclination factor (0=face-on, 1=edge-on) (default: 0.3).
    label_text : str, optional
        Text label to display near the disk (default: '').
    label_position : str, optional
        Position of the label (default: 'bottom').
    label_offset : float, optional
        Distance offset from the disk to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Height based on inclination
    height_outer = outer_radius * 2 * (1 - inclination * 0.7)
    height_inner = inner_radius * 2 * (1 - inclination * 0.7)
    
    # Calculate scale factor for vertical compression
    scale_y = height_outer / (outer_radius * 2)
    scale_y_middle = (height_outer * 0.7) / (outer_radius * 1.4)
    
    # BACK HALF of disk (behind the star) - upper semicircle
    # Outer disk back
    outer_back = Wedge((x, y), outer_radius, 0, 180,
                       width=outer_radius-inner_radius,
                       facecolor=colors['disk'], alpha=0.6, 
                       edgecolor='none', linewidth=0.5, zorder=2)
    # Scale vertically around the center point (x, y)
    transform_back = (Affine2D()
                     .translate(-x, -y)  # Move to origin
                     .scale(1, scale_y)   # Scale vertically
                     .translate(x, y)     # Move back to (x, y)
                     + ax.transData)
    outer_back.set_transform(transform_back)
    ax.add_patch(outer_back)
    
    # Middle disk region back
    middle_back = Wedge((x, y), outer_radius*0.7, 0, 180,
                        width=outer_radius*0.7-inner_radius*0.7,
                        facecolor=colors['disk_inner'], alpha=0.7, 
                        edgecolor='none', zorder=2)
    transform_middle_back = (Affine2D()
                            .translate(-x, -y)
                            .scale(1, scale_y_middle)
                            .translate(x, y)
                            + ax.transData)
    middle_back.set_transform(transform_middle_back)
    ax.add_patch(middle_back)
    
    # FRONT HALF of disk (in front of the star) - lower semicircle
    # Outer disk front
    outer_front = Wedge((x, y), outer_radius, 180, 360,
                        width=outer_radius-inner_radius,
                        facecolor=colors['disk'], alpha=0.6, 
                        edgecolor='none', linewidth=0.5, zorder=5)
    transform_front = (Affine2D()
                      .translate(-x, -y)
                      .scale(1, scale_y)
                      .translate(x, y)
                      + ax.transData)
    outer_front.set_transform(transform_front)
    ax.add_patch(outer_front)
    
    # Middle disk region front
    middle_front = Wedge((x, y), outer_radius*0.7, 180, 360,
                         width=outer_radius*0.7-inner_radius,
                         facecolor=colors['disk_inner'], alpha=0.7, 
                         edgecolor='none', zorder=5)
    transform_middle_front = (Affine2D()
                             .translate(-x, -y)
                             .scale(1, scale_y_middle)
                             .translate(x, y)
                             + ax.transData)
    middle_front.set_transform(transform_middle_front)
    ax.add_patch(middle_front)
    
    if label_text:
        if label_offset is None:
            label_offset = height_outer/2 + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def mass_transfer_stream(x1, y1, x2, y2, width=0.05, color=None, 
                         label_text='', ax=None):
    """Draw a mass transfer stream between two objects.
    
    Parameters
    ----------
    x1, y1 : float
        Starting coordinates of the stream (donor).
    x2, y2 : float
        Ending coordinates of the stream (accretor).
    width : float, optional
        Width of the stream (default: 0.05).
    color : str, optional
        Color of the stream (default: uses colors['stream']).
    label_text : str, optional
        Text label to display near the stream (default: '').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    color = color or colors['stream']
    
    # Create curved stream path
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2 + 0.1  # Slight curve upward
    
    # Draw stream as a series of points
    n_points = 20
    for i in range(n_points):
        t = i / (n_points - 1)
        # Quadratic bezier curve
        bx = (1-t)**2 * x1 + 2*(1-t)*t * mid_x + t**2 * x2
        by = (1-t)**2 * y1 + 2*(1-t)*t * mid_y + t**2 * y2
        # Varying width along stream
        r = width * (1 - 0.5 * t)
        circle = Circle((bx, by), r, facecolor=color, 
                        edgecolor='none', alpha=0.6, zorder=2)
        ax.add_patch(circle)
    
    if label_text:
        label(ax, mid_x, mid_y + 0.15, label_text, label_position='top')


def jet(x, y, length=0.8, width=0.1, angle=90, color=None,
        label_text='', label_position='top', ax=None):
    """Draw a relativistic jet from a compact object.
    
    Parameters
    ----------
    x : float
        X-coordinate of the jet base.
    y : float
        Y-coordinate of the jet base.
    length : float, optional
        Length of each jet (default: 0.8).
    width : float, optional
        Width of the jet at base (default: 0.1).
    angle : float, optional
        Angle of the jet in degrees (default: 90, vertical).
    color : str, optional
        Color of the jet (default: uses colors['jet']).
    label_text : str, optional
        Text label to display near the jet (default: '').
    label_position : str, optional
        Position of the label (default: 'top').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    color = color or colors['jet']
    
    # Convert angle to radians
    theta = np.radians(angle)
    
    # Calculate jet direction
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)
    
    # Draw upper jet (cone shape)
    jet_points_up = [
        [x - width/2, y],
        [x + width/2, y],
        [x + width/4, y + dy],
        [x - width/4, y + dy]
    ]
    jet_up = Polygon(jet_points_up, facecolor=color, alpha=0.7,
                     edgecolor='darkviolet', linewidth=0.5, zorder=4)
    ax.add_patch(jet_up)
    
    # Draw lower jet (cone shape)
    jet_points_down = [
        [x - width/2, y],
        [x + width/2, y],
        [x + width/4, y - dy],
        [x - width/4, y - dy]
    ]
    jet_down = Polygon(jet_points_down, facecolor=color, alpha=0.7,
                       edgecolor='darkviolet', linewidth=0.5, zorder=4)
    ax.add_patch(jet_down)
    
    if label_text:
        label(ax, x, y + length + 0.1, label_text, label_position)


def wind_mass_transfer(x, y, size=0.3, wind_extent=0.5, 
                       label_text='', ax=None):
    """Draw wind mass transfer (Bondi-Hoyle accretion visualization).
    
    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.3).
    wind_extent : float, optional
        Extent of the wind beyond the star (default: 0.5).
    label_text : str, optional
        Text label to display (default: '').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw wind shells (concentric circles with decreasing opacity)
    for i in range(4):
        shell_size = size + wind_extent * (i + 1) / 4
        alpha = 1.0 - i * 0.25
        shell = Circle((x, y), shell_size, facecolor='none',
                       edgecolor=colors['wind'], linewidth=1, 
                       alpha=alpha, linestyle='--', zorder=0)
        ax.add_patch(shell)
    
    # Draw the star
    stellar.star(x, y, size=size, color=colors['BSG'], ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=size + wind_extent + 0.15)


def case_A_RLO(x, y, donor_size=0.35, accretor_size=0.3, separation=0.9,
               label_text='Case A RLO', ax=None):
    """Draw Case A Roche Lobe Overflow (during core H burning).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary center.
    y : float
        Y-coordinate of the binary center.
    donor_size : float, optional
        Size of the donor (default: 0.35).
    accretor_size : float, optional
        Size of the accretor (default: 0.3).
    separation : float, optional
        Distance between objects (default: 0.9).
    label_text : str, optional
        Text label (default: 'Case A RLO').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    roche_lobe_overflow(x, y, donor_size=donor_size, accretor_size=accretor_size,
                        separation=separation, donor_color=colors['ZAMS'],
                        accretor_color=colors['ZAMS'], label_text=label_text, ax=ax)


def case_B_RLO(x, y, donor_size=0.45, accretor_size=0.3, separation=1.0,
               label_text='Case B RLO', ax=None):
    """Draw Case B Roche Lobe Overflow (during H shell burning/HG).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary center.
    y : float
        Y-coordinate of the binary center.
    donor_size : float, optional
        Size of the donor (default: 0.45).
    accretor_size : float, optional
        Size of the accretor (default: 0.3).
    separation : float, optional
        Distance between objects (default: 1.0).
    label_text : str, optional
        Text label (default: 'Case B RLO').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    roche_lobe_overflow(x, y, donor_size=donor_size, accretor_size=accretor_size,
                        separation=separation, donor_color=colors['HG'],
                        accretor_color=colors['ZAMS'], label_text=label_text, ax=ax)


def case_C_RLO(x, y, donor_size=0.5, accretor_size=0.25, separation=1.1,
               label_text='Case C RLO', ax=None):
    """Draw Case C Roche Lobe Overflow (during He shell burning/AGB).
    
    Parameters
    ----------
    x : float
        X-coordinate of the binary center.
    y : float
        Y-coordinate of the binary center.
    donor_size : float, optional
        Size of the donor (default: 0.5).
    accretor_size : float, optional
        Size of the accretor (default: 0.25).
    separation : float, optional
        Distance between objects (default: 1.1).
    label_text : str, optional
        Text label (default: 'Case C RLO').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    roche_lobe_overflow(x, y, donor_size=donor_size, accretor_size=accretor_size,
                        separation=separation, donor_color=colors['AGB'],
                        accretor_color=colors['ZAMS'], label_text=label_text, ax=ax)


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


