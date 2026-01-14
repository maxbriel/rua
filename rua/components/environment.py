"""
Environment and structure drawing functions.
Contains functions for disks, winds, magnetospheres, and other environmental features.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Arc, Wedge, Polygon
import numpy as np

from rua.utils.colors import colors
from rua.components import stellar, compact
from rua.components.decorator import label


def circumbinary_disk(x, y, inner_radius=0.8, outer_radius=1.5, inclination=0.3,
                      gap_radius=0.6, label_text='Circumbinary Disk', ax=None):
    """Draw a circumbinary disk around a binary system.
    
    Parameters
    ----------
    x : float
        X-coordinate of the disk center.
    y : float
        Y-coordinate of the disk center.
    inner_radius : float, optional
        Inner radius of the disk (default: 0.8).
    outer_radius : float, optional
        Outer radius of the disk (default: 1.5).
    inclination : float, optional
        Disk inclination factor (default: 0.3).
    gap_radius : float, optional
        Radius of the inner gap/cavity (default: 0.6).
    label_text : str, optional
        Text label to display (default: 'Circumbinary Disk').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Calculate heights based on inclination
    height_outer = outer_radius * 2 * (1 - inclination * 0.7)
    height_inner = inner_radius * 2 * (1 - inclination * 0.7)
    height_gap = gap_radius * 2 * (1 - inclination * 0.7)
    
    # Outer disk
    outer = Ellipse((x, y), width=outer_radius*2, height=height_outer,
                    facecolor=colors['circumbinary'], alpha=0.4, 
                    edgecolor='sienna', linewidth=0.5, zorder=0)
    ax.add_patch(outer)
    
    # Middle ring
    middle = Ellipse((x, y), width=inner_radius*2, height=height_inner,
                     facecolor=colors['disk'], alpha=0.5, 
                     edgecolor='none', zorder=0)
    ax.add_patch(middle)
    
    # Inner gap (clear region)
    gap = Ellipse((x, y), width=gap_radius*2, height=height_gap,
                  facecolor='white', edgecolor='none', zorder=1)
    ax.add_patch(gap)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=height_outer/2 + 0.2)


def stellar_wind(x, y, star_size=0.3, wind_extent=0.6, n_shells=4,
                 wind_color=None, label_text='Stellar Wind', ax=None):
    """Draw stellar wind outflow.
    
    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    star_size : float, optional
        Radius of the star (default: 0.3).
    wind_extent : float, optional
        Maximum extent of wind beyond star (default: 0.6).
    n_shells : int, optional
        Number of wind shells to draw (default: 4).
    wind_color : str, optional
        Color of the wind (default: uses colors['wind']).
    label_text : str, optional
        Text label to display (default: 'Stellar Wind').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    wind_color = wind_color or colors['wind']
    
    # Draw expanding wind shells
    for i in range(n_shells):
        shell_radius = star_size + wind_extent * (i + 1) / n_shells
        alpha = 0.4 - i * (0.3 / n_shells)
        shell = Circle((x, y), shell_radius, facecolor='none',
                       edgecolor=wind_color, linewidth=1.5,
                       alpha=alpha, linestyle='--', zorder=0)
        ax.add_patch(shell)
    
    # Draw outward arrows
    n_arrows = 8
    for i in range(n_arrows):
        angle = i * 2 * np.pi / n_arrows
        start_r = star_size * 1.1
        end_r = star_size + wind_extent * 0.8
        start_x = x + start_r * np.cos(angle)
        start_y = y + start_r * np.sin(angle)
        end_x = x + end_r * np.cos(angle)
        end_y = y + end_r * np.sin(angle)
        arrow = FancyArrowPatch((start_x, start_y), (end_x, end_y),
                                arrowstyle='->', mutation_scale=8,
                                linewidth=0.8, color=wind_color,
                                alpha=0.5, zorder=1)
        ax.add_patch(arrow)
    
    # Draw the star
    stellar.star(x, y, size=star_size, color=colors['BSG'], 
                 edgecolor='darkblue', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=star_size + wind_extent + 0.15)


def magnetosphere(x, y, ns_size=0.1, field_extent=0.5, n_lines=6,
                  label_text='Magnetosphere', ax=None):
    """Draw a neutron star magnetosphere with field lines.
    
    Parameters
    ----------
    x : float
        X-coordinate of the neutron star center.
    y : float
        Y-coordinate of the neutron star center.
    ns_size : float, optional
        Size of the neutron star (default: 0.1).
    field_extent : float, optional
        Extent of the magnetic field lines (default: 0.5).
    n_lines : int, optional
        Number of field line pairs (default: 6).
    label_text : str, optional
        Text label to display (default: 'Magnetosphere').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw magnetic field lines (dipole-like)
    for i in range(n_lines):
        # Symmetric field lines on both sides
        offset = (i + 1) * 0.08
        
        # Top field line
        theta_start = np.pi/2 - np.pi/6 * (i + 1) / n_lines
        theta_end = np.pi/2 + np.pi/6 * (i + 1) / n_lines
        
        # Create curved field line using bezier-like points
        n_points = 20
        field_line_top = []
        for j in range(n_points):
            t = j / (n_points - 1)
            angle = theta_start + t * (theta_end - theta_start)
            r = ns_size + field_extent * (1 - abs(2*t - 1)**2) * ((n_lines - i) / n_lines)
            px = x + r * np.cos(angle)
            py = y + r * np.sin(angle)
            field_line_top.append([px, py])
        
        # Draw top field line
        field_line_top = np.array(field_line_top)
        ax.plot(field_line_top[:, 0], field_line_top[:, 1], 
                color=colors['magnetosphere'], linewidth=0.8, alpha=0.7)
        
        # Bottom field line (mirror)
        field_line_bottom = field_line_top.copy()
        field_line_bottom[:, 1] = 2*y - field_line_bottom[:, 1]
        ax.plot(field_line_bottom[:, 0], field_line_bottom[:, 1], 
                color=colors['magnetosphere'], linewidth=0.8, alpha=0.7)
    
    # Draw the neutron star
    compact.NS(x, y, size=ns_size, label_text='', ax=ax)
    
    # Draw magnetic poles
    pole_size = ns_size * 0.3
    ax.add_patch(Circle((x, y + ns_size*0.9), pole_size, 
                        facecolor='red', edgecolor='none', alpha=0.8, zorder=5))
    ax.add_patch(Circle((x, y - ns_size*0.9), pole_size, 
                        facecolor='blue', edgecolor='none', alpha=0.8, zorder=5))
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=field_extent + 0.15)


def pulsar(x, y, ns_size=0.1, beam_length=0.6, beam_width=0.15,
           beam_angle=30, rotation_indicator=True,
           label_text='Pulsar', ax=None):
    """Draw a pulsar with emission beams.
    
    Parameters
    ----------
    x : float
        X-coordinate of the pulsar center.
    y : float
        Y-coordinate of the pulsar center.
    ns_size : float, optional
        Size of the neutron star (default: 0.1).
    beam_length : float, optional
        Length of the emission beams (default: 0.6).
    beam_width : float, optional
        Width of the beams at the base (default: 0.15).
    beam_angle : float, optional
        Angle of the magnetic axis from vertical in degrees (default: 30).
    rotation_indicator : bool, optional
        Whether to show rotation direction (default: True).
    label_text : str, optional
        Text label to display (default: 'Pulsar').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    theta = np.radians(beam_angle)
    
    # Calculate beam directions
    beam_dx = np.sin(theta)
    beam_dy = np.cos(theta)
    
    # Draw upper beam
    beam_up = Wedge((x, y), beam_length, 90 - beam_angle - 15, 90 - beam_angle + 15,
                    facecolor=colors['pulsar_wind'], alpha=0.5,
                    edgecolor='darkcyan', linewidth=0.5, zorder=2)
    ax.add_patch(beam_up)
    
    # Draw lower beam
    beam_down = Wedge((x, y), beam_length, 270 - beam_angle - 15, 270 - beam_angle + 15,
                      facecolor=colors['pulsar_wind'], alpha=0.5,
                      edgecolor='darkcyan', linewidth=0.5, zorder=2)
    ax.add_patch(beam_down)
    
    # Draw the neutron star
    compact.NS(x, y, size=ns_size, label_text='', ax=ax)
    
    # Draw rotation indicator
    if rotation_indicator:
        arc = Arc((x, y), ns_size*4, ns_size*4, angle=0, 
                  theta1=120, theta2=240,
                  color='gray', linewidth=1.5, linestyle='-')
        ax.add_patch(arc)
        # Rotation arrow
        arrow_x = x + ns_size*2 * np.cos(np.radians(240))
        arrow_y = y + ns_size*2 * np.sin(np.radians(240))
        ax.annotate('', xy=(arrow_x - 0.05, arrow_y + 0.03), 
                    xytext=(arrow_x, arrow_y),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=beam_length + 0.15)


def pulsar_wind_nebula(x, y, pulsar_size=0.08, nebula_size=0.8,
                       label_text='Pulsar Wind Nebula', ax=None):
    """Draw a pulsar wind nebula.
    
    Parameters
    ----------
    x : float
        X-coordinate of the center.
    y : float
        Y-coordinate of the center.
    pulsar_size : float, optional
        Size of the central pulsar (default: 0.08).
    nebula_size : float, optional
        Size of the nebula (default: 0.8).
    label_text : str, optional
        Text label to display (default: 'Pulsar Wind Nebula').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw outer nebula
    outer = Circle((x, y), nebula_size, facecolor=colors['pulsar_wind'],
                   edgecolor='teal', linewidth=0.5, alpha=0.3, zorder=0)
    ax.add_patch(outer)
    
    # Draw inner nebula
    inner = Circle((x, y), nebula_size * 0.6, facecolor=colors['pulsar_wind'],
                   edgecolor='none', alpha=0.4, zorder=1)
    ax.add_patch(inner)
    
    # Draw wind termination shock
    shock = Circle((x, y), nebula_size * 0.3, facecolor='none',
                   edgecolor='cyan', linewidth=1, linestyle='--',
                   alpha=0.7, zorder=2)
    ax.add_patch(shock)
    
    # Draw pulsar at center
    compact.NS(x, y, size=pulsar_size, label_text='', ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=nebula_size + 0.15)


def common_envelope_spiral(x, y, core_size=0.15, companion_size=0.12,
                           envelope_size=0.6, n_arms=2, n_turns=1.5,
                           label_text='CE Inspiral', ax=None):
    """Draw common envelope phase with spiral density pattern.
    
    Parameters
    ----------
    x : float
        X-coordinate of the center.
    y : float
        Y-coordinate of the center.
    core_size : float, optional
        Size of the primary core (default: 0.15).
    companion_size : float, optional
        Size of the companion (default: 0.12).
    envelope_size : float, optional
        Size of the common envelope (default: 0.6).
    n_arms : int, optional
        Number of spiral arms (default: 2).
    n_turns : float, optional
        Number of spiral turns (default: 1.5).
    label_text : str, optional
        Text label to display (default: 'CE Inspiral').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw common envelope
    envelope = Circle((x, y), envelope_size, facecolor=colors['CE'],
                      edgecolor='gray', linewidth=0.5, alpha=0.5, zorder=0)
    ax.add_patch(envelope)
    
    # Draw spiral arms
    for arm in range(n_arms):
        arm_offset = arm * 2 * np.pi / n_arms
        n_points = 50
        spiral_x = []
        spiral_y = []
        
        for i in range(n_points):
            theta = arm_offset + i * n_turns * 2 * np.pi / n_points
            r = companion_size + (envelope_size - companion_size) * i / n_points
            spiral_x.append(x + r * np.cos(theta))
            spiral_y.append(y + r * np.sin(theta))
        
        ax.plot(spiral_x, spiral_y, color=colors['Envelope'], 
                linewidth=2, alpha=0.6, zorder=1)
    
    # Draw central core
    stellar.star(x, y, size=core_size, color=colors['He_star'], 
                 edgecolor='steelblue', ax=ax)
    
    # Draw inspiraling companion
    companion_theta = np.pi / 4  # Position along spiral
    companion_r = envelope_size * 0.5
    comp_x = x + companion_r * np.cos(companion_theta)
    comp_y = y + companion_r * np.sin(companion_theta)
    stellar.star(comp_x, comp_y, size=companion_size, 
                 color=colors['lower_mass_ZAMS'], ax=ax)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=envelope_size + 0.15)


def supernova_remnant(x, y, remnant_size=1.0, co_size=0.08, co_type='NS',
                      n_shells=3, label_text='SNR', ax=None):
    """Draw a supernova remnant with central compact object.
    
    Parameters
    ----------
    x : float
        X-coordinate of the center.
    y : float
        Y-coordinate of the center.
    remnant_size : float, optional
        Size of the remnant (default: 1.0).
    co_size : float, optional
        Size of the central compact object (default: 0.08).
    co_type : str, optional
        Type of compact object: 'NS', 'BH', or None (default: 'NS').
    n_shells : int, optional
        Number of shell layers (default: 3).
    label_text : str, optional
        Text label to display (default: 'SNR').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw expanding shells
    for i in range(n_shells):
        shell_radius = remnant_size * (n_shells - i) / n_shells
        alpha = 0.2 + 0.15 * i
        
        # Outer shells are more red (older, cooler)
        # Inner shells are more orange/yellow (hotter)
        if i == 0:
            color = 'darkred'
        elif i == 1:
            color = 'orangered'
        else:
            color = 'orange'
        
        shell = Circle((x, y), shell_radius, facecolor=color,
                       edgecolor='darkred' if i == 0 else 'none',
                       linewidth=1, alpha=alpha, zorder=i)
        ax.add_patch(shell)
    
    # Draw central compact object
    if co_type == 'NS':
        compact.NS(x, y, size=co_size, label_text='', ax=ax)
    elif co_type == 'BH':
        compact.BH(x, y, size=co_size, label_text='', ax=ax)
    # If co_type is None, no central object (like Type Ia remnant)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=remnant_size + 0.15)


def accretion_column(x, y, ns_size=0.1, column_height=0.4, column_width=0.08,
                     label_text='Accretion Column', ax=None):
    """Draw magnetic accretion columns on a neutron star.
    
    Parameters
    ----------
    x : float
        X-coordinate of the neutron star center.
    y : float
        Y-coordinate of the neutron star center.
    ns_size : float, optional
        Size of the neutron star (default: 0.1).
    column_height : float, optional
        Height of the accretion columns (default: 0.4).
    column_width : float, optional
        Width of the columns at base (default: 0.08).
    label_text : str, optional
        Text label to display (default: 'Accretion Column').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    # Draw upper accretion column
    column_up = Polygon([
        [x - column_width/2, y + ns_size*0.8],
        [x + column_width/2, y + ns_size*0.8],
        [x + column_width*1.5, y + ns_size + column_height],
        [x - column_width*1.5, y + ns_size + column_height]
    ], facecolor=colors['stream'], alpha=0.6,
       edgecolor='steelblue', linewidth=0.5, zorder=4)
    ax.add_patch(column_up)
    
    # Draw lower accretion column
    column_down = Polygon([
        [x - column_width/2, y - ns_size*0.8],
        [x + column_width/2, y - ns_size*0.8],
        [x + column_width*1.5, y - ns_size - column_height],
        [x - column_width*1.5, y - ns_size - column_height]
    ], facecolor=colors['stream'], alpha=0.6,
       edgecolor='steelblue', linewidth=0.5, zorder=4)
    ax.add_patch(column_down)
    
    # Draw the neutron star
    compact.NS(x, y, size=ns_size, label_text='', ax=ax)
    
    # Draw hotspots at poles
    hotspot_size = ns_size * 0.25
    ax.add_patch(Circle((x, y + ns_size*0.85), hotspot_size, 
                        facecolor='yellow', edgecolor='none', alpha=0.9, zorder=5))
    ax.add_patch(Circle((x, y - ns_size*0.85), hotspot_size, 
                        facecolor='yellow', edgecolor='none', alpha=0.9, zorder=5))
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=ns_size + column_height + 0.15)


def tidal_tail(x, y, star_size=0.25, tail_length=0.8, tail_direction=45,
               label_text='Tidal Tail', ax=None):
    """Draw a tidally distorted star with tail.
    
    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    star_size : float, optional
        Size of the star (default: 0.25).
    tail_length : float, optional
        Length of the tidal tail (default: 0.8).
    tail_direction : float, optional
        Direction of the tail in degrees (default: 45).
    label_text : str, optional
        Text label to display (default: 'Tidal Tail').
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on.
    
    Returns
    -------
    None
    """
    ax = ax or plt.gca()
    
    theta = np.radians(tail_direction)
    
    # Draw tidal tail as tapering stream
    n_segments = 15
    for i in range(n_segments):
        t = i / n_segments
        seg_x = x + (star_size + tail_length * t) * np.cos(theta)
        seg_y = y + (star_size + tail_length * t) * np.sin(theta)
        seg_size = star_size * 0.3 * (1 - t * 0.8)
        alpha = 0.5 * (1 - t * 0.7)
        
        segment = Circle((seg_x, seg_y), seg_size, facecolor=colors['ZAMS'],
                         edgecolor='none', alpha=alpha, zorder=1)
        ax.add_patch(segment)
    
    # Draw the distorted star (slightly elliptical)
    star_ellipse = Ellipse((x, y), width=star_size*2.2, height=star_size*1.8,
                           angle=tail_direction, facecolor=colors['ZAMS'],
                           edgecolor='darkorange', linewidth=0.5, zorder=2)
    ax.add_patch(star_ellipse)
    
    if label_text:
        label(ax, x, y, label_text, label_position='bottom',
              label_offset=star_size + 0.2)
