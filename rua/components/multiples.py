"""
Multi-star system drawing functions.
Contains functions for triple, quadruple, and cluster systems.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch
import numpy as np

from rua.utils.colors import colors
from rua.components import stellar, compact
from rua.components.decorator import label


def triple_system(x, y, sizes=(0.25, 0.2, 0.15), inner_separation=0.5,
                  outer_separation=1.2, inner_colors=None, outer_color=None,
                  label_text='Triple System', ax=None):
    """Draw a hierarchical triple star system.
    
    Shows an inner binary with a tertiary companion.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    sizes : tuple, optional
        Sizes of (primary, secondary, tertiary) stars (default: (0.25, 0.2, 0.15)).
    inner_separation : float, optional
        Separation of the inner binary (default: 0.5).
    outer_separation : float, optional
        Distance of tertiary from inner binary center (default: 1.2).
    inner_colors : tuple, optional
        Colors for (primary, secondary). Default uses ZAMS colors.
    outer_color : str, optional
        Color for tertiary. Default uses tertiary color.
    label_text : str, optional
        Text label to display (default: 'Triple System').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    if inner_colors is None:
        inner_colors = (colors['ZAMS'], colors['lower_mass_ZAMS'])
    if outer_color is None:
        outer_color = colors['tertiary']
    
    # Inner binary center
    inner_x = x - outer_separation/3
    
    # Draw orbit ellipse for tertiary
    orbit = Ellipse((x, y), width=outer_separation*1.5, height=outer_separation*0.8,
                    facecolor='none', edgecolor='gray', linewidth=0.5,
                    linestyle='--', alpha=0.5, zorder=0)
    ax.add_patch(orbit)
    
    # Draw inner binary orbit
    inner_orbit = Circle((inner_x, y), inner_separation/2, facecolor='none',
                         edgecolor='gray', linewidth=0.5, linestyle=':',
                         alpha=0.5, zorder=0)
    ax.add_patch(inner_orbit)
    
    # Draw inner binary
    stellar.star(inner_x - inner_separation/2, y, size=sizes[0], 
                 color=inner_colors[0], ax=ax)
    stellar.star(inner_x + inner_separation/2, y, size=sizes[1], 
                 color=inner_colors[1], ax=ax)
    
    # Draw tertiary
    tertiary_x = x + outer_separation/2
    stellar.star(tertiary_x, y, size=sizes[2], color=outer_color, 
                 edgecolor='mediumpurple', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=max(sizes) + outer_separation/2 + 0.2)


def quadruple_system_2plus2(x, y, sizes=(0.2, 0.18, 0.18, 0.15),
                            inner_separations=(0.4, 0.35), outer_separation=1.5,
                            label_text='2+2 Quadruple', ax=None):
    """Draw a 2+2 hierarchical quadruple system.
    
    Two binaries orbiting each other.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    sizes : tuple, optional
        Sizes of the four stars (default: (0.2, 0.18, 0.18, 0.15)).
    inner_separations : tuple, optional
        Separations of the two inner binaries (default: (0.4, 0.35)).
    outer_separation : float, optional
        Distance between the two binary centers (default: 1.5).
    label_text : str, optional
        Text label to display (default: '2+2 Quadruple').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Centers of the two binaries
    binary1_x = x - outer_separation/2
    binary2_x = x + outer_separation/2
    
    # Draw outer orbit
    outer_orbit = Ellipse((x, y), width=outer_separation*1.2, height=outer_separation*0.6,
                          facecolor='none', edgecolor='gray', linewidth=0.5,
                          linestyle='--', alpha=0.5, zorder=0)
    ax.add_patch(outer_orbit)
    
    # Draw binary 1
    inner_orbit1 = Circle((binary1_x, y), inner_separations[0]/2, facecolor='none',
                          edgecolor='gray', linewidth=0.5, linestyle=':',
                          alpha=0.5, zorder=0)
    ax.add_patch(inner_orbit1)
    stellar.star(binary1_x - inner_separations[0]/2, y, size=sizes[0], 
                 color=colors['ZAMS'], ax=ax)
    stellar.star(binary1_x + inner_separations[0]/2, y, size=sizes[1], 
                 color=colors['lower_mass_ZAMS'], ax=ax)
    
    # Draw binary 2
    inner_orbit2 = Circle((binary2_x, y), inner_separations[1]/2, facecolor='none',
                          edgecolor='gray', linewidth=0.5, linestyle=':',
                          alpha=0.5, zorder=0)
    ax.add_patch(inner_orbit2)
    stellar.star(binary2_x - inner_separations[1]/2, y, size=sizes[2], 
                 color=colors['tertiary'], edgecolor='mediumpurple', ax=ax)
    stellar.star(binary2_x + inner_separations[1]/2, y, size=sizes[3], 
                 color=colors['quaternary'], edgecolor='darkcyan', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=max(sizes) + 0.4)


def quadruple_system_3plus1(x, y, sizes=(0.22, 0.18, 0.15, 0.12),
                            inner_separation=0.4, mid_separation=0.9,
                            outer_separation=1.6, label_text='3+1 Quadruple', ax=None):
    """Draw a 3+1 hierarchical quadruple system.
    
    A triple system with a distant fourth companion.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    sizes : tuple, optional
        Sizes of the four stars (default: (0.22, 0.18, 0.15, 0.12)).
    inner_separation : float, optional
        Separation of the innermost binary (default: 0.4).
    mid_separation : float, optional
        Distance of tertiary from inner binary (default: 0.9).
    outer_separation : float, optional
        Distance of quaternary from triple center (default: 1.6).
    label_text : str, optional
        Text label to display (default: '3+1 Quadruple').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Triple center
    triple_x = x - outer_separation/4
    
    # Draw outermost orbit
    outer_orbit = Ellipse((x, y), width=outer_separation*1.3, height=outer_separation*0.7,
                          facecolor='none', edgecolor='gray', linewidth=0.5,
                          linestyle='--', alpha=0.4, zorder=0)
    ax.add_patch(outer_orbit)
    
    # Draw triple (inner binary + tertiary)
    inner_binary_x = triple_x - mid_separation/3
    
    # Inner binary orbit
    inner_orbit = Circle((inner_binary_x, y), inner_separation/2, facecolor='none',
                         edgecolor='gray', linewidth=0.5, linestyle=':',
                         alpha=0.5, zorder=0)
    ax.add_patch(inner_orbit)
    
    # Mid orbit for tertiary
    mid_orbit = Ellipse((triple_x, y), width=mid_separation*1.2, height=mid_separation*0.6,
                        facecolor='none', edgecolor='gray', linewidth=0.5,
                        linestyle='-.', alpha=0.4, zorder=0)
    ax.add_patch(mid_orbit)
    
    # Draw inner binary
    stellar.star(inner_binary_x - inner_separation/2, y, size=sizes[0], 
                 color=colors['ZAMS'], ax=ax)
    stellar.star(inner_binary_x + inner_separation/2, y, size=sizes[1], 
                 color=colors['lower_mass_ZAMS'], ax=ax)
    
    # Draw tertiary
    stellar.star(triple_x + mid_separation/2, y, size=sizes[2], 
                 color=colors['tertiary'], edgecolor='mediumpurple', ax=ax)
    
    # Draw quaternary (distant)
    quaternary_x = x + outer_separation/2
    stellar.star(quaternary_x, y, size=sizes[3], 
                 color=colors['quaternary'], edgecolor='darkcyan', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=max(sizes) + 0.5)


def star_cluster(x, y, n_stars=12, cluster_radius=1.0, size_range=(0.08, 0.2),
                 label_text='Star Cluster', seed=None, ax=None):
    """Draw a small star cluster.
    
    Parameters
    ----------
    x : float
        X-coordinate of the cluster center.
    y : float
        Y-coordinate of the cluster center.
    n_stars : int, optional
        Number of stars in the cluster (default: 12).
    cluster_radius : float, optional
        Radius of the cluster (default: 1.0).
    size_range : tuple, optional
        Range of star sizes (min, max) (default: (0.08, 0.2)).
    label_text : str, optional
        Text label to display (default: 'Star Cluster').
    seed : int, optional
        Random seed for reproducibility (default: None).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random star positions (concentrated toward center)
    for i in range(n_stars):
        # Use exponential distribution for distance (more stars near center)
        r = cluster_radius * np.random.exponential(0.4)
        r = min(r, cluster_radius)  # Cap at cluster radius
        theta = np.random.uniform(0, 2*np.pi)
        
        star_x = x + r * np.cos(theta)
        star_y = y + r * np.sin(theta)
        
        # Random size
        star_size = np.random.uniform(size_range[0], size_range[1])
        
        # Random color (various MS colors)
        color_choices = [colors['ZAMS'], colors['lower_mass_ZAMS'], 
                        colors['BSG'], colors['HeMS']]
        color = np.random.choice(color_choices)
        
        stellar.star(star_x, star_y, size=star_size, color=color, ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=cluster_radius + 0.2)


def triple_with_compact(x, y, co_type='BH', co_size=0.12, star_sizes=(0.25, 0.2),
                        inner_separation=0.5, outer_separation=1.0,
                        label_text='Triple with CO', ax=None):
    """Draw a triple system with a compact object.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    co_type : str, optional
        Type of compact object: 'BH', 'NS', or 'WD' (default: 'BH').
    co_size : float, optional
        Size of the compact object (default: 0.12).
    star_sizes : tuple, optional
        Sizes of the two stars (default: (0.25, 0.2)).
    inner_separation : float, optional
        Separation of the inner pair (default: 0.5).
    outer_separation : float, optional
        Distance of outer component (default: 1.0).
    label_text : str, optional
        Text label to display (default: 'Triple with CO').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Inner pair: compact object + star
    inner_x = x - outer_separation/3
    
    # Draw orbits
    outer_orbit = Ellipse((x, y), width=outer_separation*1.4, height=outer_separation*0.7,
                          facecolor='none', edgecolor='gray', linewidth=0.5,
                          linestyle='--', alpha=0.5, zorder=0)
    ax.add_patch(outer_orbit)
    
    inner_orbit = Circle((inner_x, y), inner_separation/2, facecolor='none',
                         edgecolor='gray', linewidth=0.5, linestyle=':',
                         alpha=0.5, zorder=0)
    ax.add_patch(inner_orbit)
    
    # Draw compact object
    if co_type == 'NS':
        compact.NS(inner_x - inner_separation/2, y, size=co_size, label_text='', ax=ax)
    elif co_type == 'WD':
        compact.WD(inner_x - inner_separation/2, y, size=co_size, label_text='', ax=ax)
    else:
        compact.BH(inner_x - inner_separation/2, y, size=co_size, label_text='', ax=ax)
    
    # Draw inner companion
    stellar.star(inner_x + inner_separation/2, y, size=star_sizes[0], 
                 color=colors['ZAMS'], ax=ax)
    
    # Draw tertiary
    stellar.star(x + outer_separation/2, y, size=star_sizes[1], 
                 color=colors['tertiary'], edgecolor='mediumpurple', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=max(star_sizes) + outer_separation/2 + 0.2)


def hierarchical_triple_diagram(x, y, inner_period='P_in', outer_period='P_out',
                                sizes=(0.2, 0.15, 0.12), label_text='', ax=None):
    """Draw a schematic hierarchical triple with period labels.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    inner_period : str, optional
        Label for inner orbital period (default: 'P_in').
    outer_period : str, optional
        Label for outer orbital period (default: 'P_out').
    sizes : tuple, optional
        Sizes of the three stars (default: (0.2, 0.15, 0.12)).
    label_text : str, optional
        Additional text label (default: '').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    inner_sep = 0.4
    outer_sep = 1.2
    
    # Inner binary center
    inner_x = x - outer_sep/4
    
    # Draw outer orbit with label
    outer_orbit = Ellipse((x - 0.1, y), width=outer_sep*1.1, height=outer_sep*0.6,
                          facecolor='none', edgecolor='blue', linewidth=1,
                          linestyle='--', alpha=0.7, zorder=0)
    ax.add_patch(outer_orbit)
    ax.text(x + outer_sep*0.5, y + outer_sep*0.4, outer_period, 
            fontsize=10, color='blue', ha='center')
    
    # Draw inner orbit with label
    inner_orbit = Circle((inner_x, y), inner_sep/2, facecolor='none',
                         edgecolor='red', linewidth=1, linestyle='-',
                         alpha=0.7, zorder=0)
    ax.add_patch(inner_orbit)
    ax.text(inner_x, y + inner_sep*0.7, inner_period, 
            fontsize=10, color='red', ha='center')
    
    # Draw stars
    stellar.star(inner_x - inner_sep/2, y, size=sizes[0], 
                 color=colors['ZAMS'], ax=ax)
    stellar.star(inner_x + inner_sep/2, y, size=sizes[1], 
                 color=colors['lower_mass_ZAMS'], ax=ax)
    stellar.star(x + outer_sep/3, y, size=sizes[2], 
                 color=colors['tertiary'], edgecolor='mediumpurple', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=outer_sep/2 + 0.3)
