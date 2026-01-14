"""
Outcome and event drawing functions for binary evolution.
Contains functions for mergers, kicks, disruption, and other binary outcomes.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Wedge
import numpy as np

from rua.utils.colors import colors
from rua.components import stellar, compact
from rua.components.decorator import label


def gravitational_wave_merger(x, y, size=0.5, n_waves=4, 
                              label_text='GW Merger', label_position='bottom',
                              label_offset=None, ax=None):
    """Draw a gravitational wave merger event.
    
    Shows two compact objects spiraling in with gravitational waves.
    
    Parameters
    ----------
    x : float
        X-coordinate of the merger center.
    y : float
        Y-coordinate of the merger center.
    size : float, optional
        Overall size of the visualization (default: 0.5).
    n_waves : int, optional
        Number of gravitational wave rings (default: 4).
    label_text : str, optional
        Text label to display (default: 'GW Merger').
    label_position : str, optional
        Position of the label (default: 'bottom').
    label_offset : float, optional
        Distance offset for the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw gravitational wave rings
    for i in range(n_waves):
        wave_radius = size * (0.5 + i * 0.4)
        alpha = 0.4 - i * 0.08
        wave = Circle((x, y), wave_radius, facecolor='none',
                      edgecolor=colors['gw_wave'], linewidth=2,
                      alpha=alpha, linestyle='-', zorder=0)
        ax.add_patch(wave)
    
    # Draw two inspiraling compact objects
    offset = size * 0.15
    compact.BH(x - offset, y, size=size*0.2, label_text='', ax=ax)
    compact.BH(x + offset, y, size=size*0.15, label_text='', ax=ax)
    
    # Central bright region (merger)
    merger_glow = Circle((x, y), size*0.25, facecolor='white',
                         edgecolor='none', alpha=0.5, zorder=2)
    ax.add_patch(merger_glow)
    
    if label_text:
        if label_offset is None:
            label_offset = size * 1.5 + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def natal_kick(x, y, kick_direction=45, kick_length=0.8, 
               compact_size=0.12, co_type='NS', label_text='Natal Kick',
               label_position='top', ax=None):
    """Draw a natal kick imparted to a compact object after supernova.
    
    Parameters
    ----------
    x : float
        X-coordinate of the compact object.
    y : float
        Y-coordinate of the compact object.
    kick_direction : float, optional
        Direction of the kick in degrees (default: 45).
    kick_length : float, optional
        Length of the kick arrow (default: 0.8).
    compact_size : float, optional
        Size of the compact object (default: 0.12).
    co_type : str, optional
        Type of compact object: 'NS' or 'BH' (default: 'NS').
    label_text : str, optional
        Text label to display (default: 'Natal Kick').
    label_position : str, optional
        Position of the label (default: 'top').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw remnant supernova debris
    debris = Circle((x, y), compact_size * 3, facecolor=colors['Supernova'],
                    edgecolor='none', alpha=0.2, zorder=0)
    ax.add_patch(debris)
    
    # Draw compact object
    if co_type == 'BH':
        compact.BH(x, y, size=compact_size, label_text='', ax=ax)
    else:
        compact.NS(x, y, size=compact_size, label_text='', ax=ax)
    
    # Calculate kick arrow endpoint
    theta = np.radians(kick_direction)
    end_x = x + kick_length * np.cos(theta)
    end_y = y + kick_length * np.sin(theta)
    
    # Draw kick arrow
    arrow = FancyArrowPatch((x, y), (end_x, end_y),
                            arrowstyle='->', mutation_scale=15,
                            linewidth=2.5, color='red',
                            linestyle='-', zorder=5)
    ax.add_patch(arrow)
    
    if label_text:
        label(ax, (x + end_x)/2, (y + end_y)/2 + 0.15, label_text, label_position)


def unbound_system(x, y, size1=0.15, size2=0.12, separation=0.8,
                   escape_distance=0.5, label_text='Unbound System',
                   ax=None):
    """Draw an unbound (disrupted) binary system.
    
    Shows two objects moving apart after disruption.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    size1 : float, optional
        Size of the first object (default: 0.15).
    size2 : float, optional
        Size of the second object (default: 0.12).
    separation : float, optional
        Current separation (default: 0.8).
    escape_distance : float, optional
        Length of escape arrows (default: 0.5).
    label_text : str, optional
        Text label to display (default: 'Unbound System').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw first object (NS) with escape arrow
    ns_x = x - separation/2
    compact.NS(ns_x, y, size=size1, label_text='', ax=ax)
    arrow1 = FancyArrowPatch((ns_x - size1, y), (ns_x - size1 - escape_distance, y),
                             arrowstyle='->', mutation_scale=12,
                             linewidth=2, color='gray', linestyle='--', zorder=4)
    ax.add_patch(arrow1)
    
    # Draw second object (star or compact) with escape arrow
    star_x = x + separation/2
    stellar.star(star_x, y, size=size2, color=colors['ZAMS'], ax=ax)
    arrow2 = FancyArrowPatch((star_x + size2, y), (star_x + size2 + escape_distance, y),
                             arrowstyle='->', mutation_scale=12,
                             linewidth=2, color='gray', linestyle='--', zorder=4)
    ax.add_patch(arrow2)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=max(size1, size2) + 0.3)


def runaway_star(x, y, size=0.25, velocity_direction=30, velocity_length=0.6,
                 label_text='Runaway Star', label_position='top', ax=None):
    """Draw a runaway star ejected from a binary system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the star.
    y : float
        Y-coordinate of the star.
    size : float, optional
        Radius of the star (default: 0.25).
    velocity_direction : float, optional
        Direction of motion in degrees (default: 30).
    velocity_length : float, optional
        Length of the velocity arrow (default: 0.6).
    label_text : str, optional
        Text label to display (default: 'Runaway Star').
    label_position : str, optional
        Position of the label (default: 'top').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw the star
    stellar.star(x, y, size=size, color=colors['BSG'], edgecolor='darkblue', ax=ax)
    
    # Calculate velocity arrow
    theta = np.radians(velocity_direction)
    end_x = x + velocity_length * np.cos(theta)
    end_y = y + velocity_length * np.sin(theta)
    
    # Draw velocity arrow
    arrow = FancyArrowPatch((x, y), (end_x, end_y),
                            arrowstyle='->', mutation_scale=15,
                            linewidth=2, color='blue',
                            linestyle='-', zorder=5)
    ax.add_patch(arrow)
    
    # Draw trail effect
    for i in range(3):
        trail_x = x - (i + 1) * 0.15 * np.cos(theta)
        trail_y = y - (i + 1) * 0.15 * np.sin(theta)
        alpha = 0.3 - i * 0.08
        trail = Circle((trail_x, trail_y), size * (0.8 - i * 0.2),
                       facecolor=colors['BSG'], edgecolor='none',
                       alpha=alpha, zorder=1)
        ax.add_patch(trail)
    
    if label_text:
        label(ax, x, y + size + 0.2, label_text, label_position)


def supernova_in_binary(x, y, sn_size=0.6, companion_size=0.25, separation=1.0,
                        label_text='SN in Binary', ax=None):
    """Draw a supernova explosion in a binary system with companion.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    sn_size : float, optional
        Size of the supernova (default: 0.6).
    companion_size : float, optional
        Size of the companion star (default: 0.25).
    separation : float, optional
        Distance between objects (default: 1.0).
    label_text : str, optional
        Text label to display (default: 'SN in Binary').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw supernova
    stellar.supernova(x - separation/2, y, size=sn_size, label_text='', ax=ax)
    
    # Draw companion star
    stellar.star(x + separation/2, y, size=companion_size, 
                 color=colors['ZAMS'], ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=max(sn_size/2, companion_size) + 0.2)


def binary_merger_product(x, y, size=0.45, label_text='Merger Product',
                          label_position='bottom', label_offset=None, ax=None):
    """Draw a binary stellar merger product.
    
    Parameters
    ----------
    x : float
        X-coordinate of the merger product.
    y : float
        Y-coordinate of the merger product.
    size : float, optional
        Size of the merger product (default: 0.45).
    label_text : str, optional
        Text label to display (default: 'Merger Product').
    label_position : str, optional
        Position of the label (default: 'bottom').
    label_offset : float, optional
        Distance offset for the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw glowing outer region (from violent merger)
    glow = Circle((x, y), size * 1.3, facecolor=colors['merger_product'],
                  edgecolor='none', alpha=0.3, zorder=1)
    ax.add_patch(glow)
    
    # Draw the merger product star
    stellar.stellar_merger(x, y, size=size, label_text='', ax=ax)
    
    if label_text:
        if label_offset is None:
            label_offset = size * 1.3 + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def common_envelope_ejection(x, y, core_size=0.15, companion_size=0.12,
                             envelope_size=0.6, ejection_arrows=True,
                             label_text='CE Ejection', ax=None):
    """Draw common envelope ejection outcome.
    
    Parameters
    ----------
    x : float
        X-coordinate of the system center.
    y : float
        Y-coordinate of the system center.
    core_size : float, optional
        Size of the exposed core (default: 0.15).
    companion_size : float, optional
        Size of the companion (default: 0.12).
    envelope_size : float, optional
        Size of the ejected envelope (default: 0.6).
    ejection_arrows : bool, optional
        Whether to show ejection arrows (default: True).
    label_text : str, optional
        Text label to display (default: 'CE Ejection').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw expanding envelope shell
    envelope = Circle((x, y), envelope_size, facecolor=colors['CE'],
                      edgecolor='gray', linewidth=1, alpha=0.3, 
                      linestyle='--', zorder=0)
    ax.add_patch(envelope)
    
    # Draw tight binary (core + companion)
    separation = core_size + companion_size + 0.05
    stellar.star(x - separation/2, y, size=core_size, 
                 color=colors['He_star'], edgecolor='steelblue', ax=ax)
    stellar.star(x + separation/2, y, size=companion_size, 
                 color=colors['lower_mass_ZAMS'], ax=ax)
    
    # Draw ejection arrows
    if ejection_arrows:
        for angle in [45, 135, 225, 315]:
            theta = np.radians(angle)
            start_r = envelope_size * 0.7
            end_r = envelope_size * 1.1
            start_x = x + start_r * np.cos(theta)
            start_y = y + start_r * np.sin(theta)
            end_x = x + end_r * np.cos(theta)
            end_y = y + end_r * np.sin(theta)
            arrow = FancyArrowPatch((start_x, start_y), (end_x, end_y),
                                    arrowstyle='->', mutation_scale=10,
                                    linewidth=1.5, color='gray',
                                    linestyle='-', zorder=1)
            ax.add_patch(arrow)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=envelope_size + 0.2)
