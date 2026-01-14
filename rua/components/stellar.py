"""
Single stellar object drawing functions.
Contains functions for drawing individual stars and stellar phases.
"""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from rua.components.decorator import label
from rua.utils.colors import colors


def star(x, y, size=0.3, color='yellow', edgecolor='black',
         label_text='', label_position='bottom', label_offset=None, ax=None, **kwargs):
    """
    Draw a cartoon star representation.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.3).
    color : str, optional
        Fill color of the star (default: 'yellow').
    edgecolor : str, optional
        Edge color of the star (default: 'black').
    label_text : str, optional
        Text label to display near the star (default: '').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the star to place the label.
        If None, automatically scales with size (default: None).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    **kwargs
        Additional keyword arguments passed to matplotlib Circle patch.

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    if ax is None:
        ax = plt.gca()

    circle = Circle((x, y), size, facecolor=color, edgecolor=edgecolor,
                    linewidth=0.5, zorder=3, **kwargs)
    ax.add_patch(circle)

    if label_text:
        # Auto-scale label offset with size if not specified
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)

    return circle


def zams(x, y, size=0.4, label_text='ZAMS\n(Main Sequence)',
         label_position='bottom', label_offset=None, ax=None):
    """Draw a ZAMS (Zero Age Main Sequence) star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.4).
    label_text : str, optional
        Text label to display near the star (default: 'ZAMS (Main Sequence)').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the star to place the label.
        If None, automatically scales with size (default: None).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    star(x, y, size=size, color=colors['ZAMS'], edgecolor='black',
         label_text=label_text, label_position=label_position,
         label_offset=label_offset, ax=ax)


def wolf_rayet(x, y, size=0.45, label_text='WR Phase\n(He-burning)',
               label_position='right', label_offset=None, ax=None):
    """Draw a Wolf-Rayet phase star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.45).
    label_text : str, optional
        Text label to display near the star (default: 'WR Phase (He-burning)').
    label_position : str, optional
        Position of the label relative to the star (default: 'right').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the star to place the label.
        If None, automatically scales with size (default: None).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    star(x, y, size=size, color=colors['WR'], edgecolor='black',
         label_text=label_text, label_position=label_position,
         label_offset=label_offset, ax=ax)


def supernova(x, y, size=1.2, label_text='Supernova\n(BH/NS)',
              label_position='right', label_offset=None, image_path=None, ax=None):
    """Draw a supernova explosion.

    Parameters
    ----------
    x : float
        X-coordinate of the supernova center.
    y : float
        Y-coordinate of the supernova center.
    size : float, optional
        Size of the supernova image (default: 1.2).
    label_text : str, optional
        Text label to display near the supernova (default: 'Supernova (BH/NS)').
    label_position : str, optional
        Position of the label relative to the supernova (default: 'right').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the supernova to place the label.
        If None, automatically scales with size (default: None).
    image_path : str, optional
        Path to supernova image file (default: uses package resources).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()


    # Draw layered explosion using circles
    # Outermost shockwave (very faint)
    outer = Circle((x, y), size * 0.6, facecolor='red',
                   edgecolor='darkred', linewidth=1, alpha=0.2, zorder=2)
    ax.add_patch(outer)

    # Outer explosion layer
    outer2 = Circle((x, y), size * 0.5, facecolor='orangered',
                    edgecolor='none', alpha=0.4, zorder=2)
    ax.add_patch(outer2)

    # Middle explosion layer
    middle = Circle((x, y), size * 0.35, facecolor='orange',
                    edgecolor='none', alpha=0.6, zorder=3)
    ax.add_patch(middle)

    # Inner bright region
    inner = Circle((x, y), size * 0.2, facecolor='yellow',
                   edgecolor='none', alpha=0.8, zorder=4)
    ax.add_patch(inner)

    # Core - very bright center
    core = Circle((x, y), size * 0.08, facecolor='white',
                  edgecolor='none', alpha=0.95, zorder=5)
    ax.add_patch(core)

    if label_text:
        # Auto-scale label offset with size if not specified
        if label_offset is None:
            label_offset = size * 0.6 + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


# ============================================================================
# GIANT BRANCH STARS
# ============================================================================

def red_giant(x, y, size=0.5, label_text='Red Giant',
              label_position='bottom', label_offset=None, ax=None):
    """Draw a Red Giant Branch (RGB) star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.5).
    label_text : str, optional
        Text label to display near the star (default: 'Red Giant').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['RGB'], edgecolor='darkred',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for red_giant
RGB = red_giant


def asymptotic_giant_branch(x, y, size=0.55, label_text='AGB Star',
                            label_position='bottom', label_offset=None, ax=None):
    """Draw an Asymptotic Giant Branch (AGB) star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.55).
    label_text : str, optional
        Text label to display near the star (default: 'AGB Star').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['AGB'], edgecolor='darkred',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for asymptotic_giant_branch
AGB = asymptotic_giant_branch


def red_supergiant(x, y, size=0.6, label_text='Red Supergiant',
                   label_position='bottom', label_offset=None, ax=None):
    """Draw a Red Supergiant (RSG) star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.6).
    label_text : str, optional
        Text label to display near the star (default: 'Red Supergiant').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['RSG'], edgecolor='darkred',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for red_supergiant
RSG = red_supergiant


def blue_supergiant(x, y, size=0.45, label_text='Blue Supergiant',
                    label_position='bottom', label_offset=None, ax=None):
    """Draw a Blue Supergiant (BSG) star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.45).
    label_text : str, optional
        Text label to display near the star (default: 'Blue Supergiant').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['BSG'], edgecolor='darkblue',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for blue_supergiant
BSG = blue_supergiant


def yellow_supergiant(x, y, size=0.5, label_text='Yellow Supergiant',
                      label_position='bottom', label_offset=None, ax=None):
    """Draw a Yellow Supergiant (YSG) star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.5).
    label_text : str, optional
        Text label to display near the star (default: 'Yellow Supergiant').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['YSG'], edgecolor='goldenrod',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for yellow_supergiant
YSG = yellow_supergiant


def horizontal_branch(x, y, size=0.35, label_text='Horizontal Branch',
                      label_position='bottom', label_offset=None, ax=None):
    """Draw a Horizontal Branch (HB) star.

    Core helium-burning star after the RGB phase.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.35).
    label_text : str, optional
        Text label to display near the star (default: 'Horizontal Branch').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['HB'], edgecolor='darkgoldenrod',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for horizontal_branch
HB = horizontal_branch


def hertzsprung_gap(x, y, size=0.45, label_text='Hertzsprung Gap',
                    label_position='bottom', label_offset=None, ax=None):
    """Draw a Hertzsprung Gap (HG) star.

    Rapid transition phase between main sequence and red giant.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.45).
    label_text : str, optional
        Text label to display near the star (default: 'Hertzsprung Gap').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['HG'], edgecolor='darkorange',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for hertzsprung_gap
HG = hertzsprung_gap


# ============================================================================
# STRIPPED AND HELIUM STARS
# ============================================================================

def helium_star(x, y, size=0.3, label_text='He Star',
                label_position='bottom', label_offset=None, ax=None):
    """Draw a Helium star (stripped envelope, He-burning core).

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.3).
    label_text : str, optional
        Text label to display near the star (default: 'He Star').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['He_star'], edgecolor='steelblue',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# Alias for helium_star
He_star = helium_star


def stripped_star(x, y, size=0.25, label_text='Stripped Star',
                  label_position='bottom', label_offset=None, ax=None):
    """Draw a stripped envelope star.

    Parameters
    ----------
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.25).
    label_text : str, optional
        Text label to display near the star (default: 'Stripped Star').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
    label_offset : float, optional
        Distance offset from the star to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['Stripped'], edgecolor='slategray',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)


# ============================================================================
# EXOTIC OBJECTS
# ============================================================================

def thorne_zytkow(x, y, size=0.55, core_size=0.1, label_text='TŻO',
                  label_position='bottom', label_offset=None, ax=None):
    """Draw a Thorne-Żytkow Object (TŻO).

    A red supergiant with a neutron star core.

    Parameters
    ----------
    x : float
        X-coordinate of the object center.
    y : float
        Y-coordinate of the object center.
    size : float, optional
        Radius of the envelope (default: 0.55).
    core_size : float, optional
        Radius of the NS core (default: 0.1).
    label_text : str, optional
        Text label to display near the object (default: 'TŻO').
    label_position : str, optional
        Position of the label relative to the object (default: 'bottom').
    label_offset : float, optional
        Distance offset from the object to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()

    # Draw the red supergiant envelope
    star(x, y, size=size, color=colors['TZO'], edgecolor='darkred', ax=ax)

    # Draw the neutron star core
    star(x, y, size=core_size, color=colors['TZO_core'], edgecolor='steelblue', ax=ax)

    if label_text:
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


# Alias for thorne_zytkow
TZO = thorne_zytkow


# ============================================================================
# STELLAR PHENOMENA - EXPLOSIONS AND TRANSIENTS
# ============================================================================

def planetary_nebula(x, y, size=0.6, wd_size=0.08, label_text='Planetary Nebula',
                     label_position='bottom', label_offset=None, ax=None):
    """Draw a planetary nebula with central white dwarf.

    Parameters
    ----------
    x : float
        X-coordinate of the nebula center.
    y : float
        Y-coordinate of the nebula center.
    size : float, optional
        Radius of the nebula (default: 0.6).
    wd_size : float, optional
        Radius of the central white dwarf (default: 0.08).
    label_text : str, optional
        Text label to display near the nebula (default: 'Planetary Nebula').
    label_position : str, optional
        Position of the label relative to the nebula (default: 'bottom').
    label_offset : float, optional
        Distance offset from the nebula to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()

    # Outer nebula shell
    outer = Circle((x, y), size, facecolor=colors['planetary_nebula_outer'],
                   edgecolor='forestgreen', linewidth=0.5, alpha=0.4, zorder=2)
    ax.add_patch(outer)

    # Inner nebula shell
    inner = Circle((x, y), size * 0.7, facecolor=colors['planetary_nebula'],
                   edgecolor='none', alpha=0.5, zorder=2)
    ax.add_patch(inner)

    # Central white dwarf
    star(x, y, size=wd_size, color=colors['WD'], edgecolor='lightgray', ax=ax)

    if label_text:
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def nova(x, y, size=0.4, label_text='Nova',
         label_position='bottom', label_offset=None, ax=None):
    """Draw a classical nova explosion.

    Parameters
    ----------
    x : float
        X-coordinate of the nova center.
    y : float
        Y-coordinate of the nova center.
    size : float, optional
        Size of the nova (default: 0.4).
    label_text : str, optional
        Text label to display near the nova (default: 'Nova').
    label_position : str, optional
        Position of the label relative to the nova (default: 'bottom').
    label_offset : float, optional
        Distance offset from the nova to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()

    # Outer nova glow
    outer = Circle((x, y), size, facecolor=colors['nova'],
                   edgecolor='orange', linewidth=0.5, alpha=0.6, zorder=2)
    ax.add_patch(outer)

    # Bright center
    inner = Circle((x, y), size * 0.4, facecolor='white',
                   edgecolor='none', alpha=0.8, zorder=3)
    ax.add_patch(inner)

    if label_text:
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def kilonova(x, y, size=0.5, label_text='Kilonova',
             label_position='bottom', label_offset=None, ax=None):
    """Draw a kilonova (NS-NS or NS-BH merger transient).

    Parameters
    ----------
    x : float
        X-coordinate of the kilonova center.
    y : float
        Y-coordinate of the kilonova center.
    size : float, optional
        Size of the kilonova (default: 0.5).
    label_text : str, optional
        Text label to display near the kilonova (default: 'Kilonova').
    label_position : str, optional
        Position of the label relative to the kilonova (default: 'bottom').
    label_offset : float, optional
        Distance offset from the kilonova to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()

    # Outer kilonova glow (r-process ejecta)
    outer = Circle((x, y), size, facecolor=colors['kilonova'],
                   edgecolor='purple', linewidth=0.5, alpha=0.5, zorder=2)
    ax.add_patch(outer)

    # Inner brighter region
    inner = Circle((x, y), size * 0.5, facecolor='violet',
                   edgecolor='none', alpha=0.7, zorder=3)
    ax.add_patch(inner)

    # Bright core
    core = Circle((x, y), size * 0.2, facecolor='white',
                  edgecolor='none', alpha=0.9, zorder=4)
    ax.add_patch(core)

    if label_text:
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def type_ia_supernova(x, y, size=1.0, label_text='Type Ia SN',
                      label_position='bottom', label_offset=None, ax=None):
    """Draw a Type Ia (thermonuclear) supernova.

    Parameters
    ----------
    x : float
        X-coordinate of the supernova center.
    y : float
        Y-coordinate of the supernova center.
    size : float, optional
        Size of the supernova (default: 1.0).
    label_text : str, optional
        Text label to display near the supernova (default: 'Type Ia SN').
    label_position : str, optional
        Position of the label relative to the supernova (default: 'bottom').
    label_offset : float, optional
        Distance offset from the supernova to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()

    # Outer explosion
    outer = Circle((x, y), size, facecolor=colors['type_ia'],
                   edgecolor='darkred', linewidth=0.5, alpha=0.4, zorder=2)
    ax.add_patch(outer)

    # Middle layer
    middle = Circle((x, y), size * 0.6, facecolor='orange',
                    edgecolor='none', alpha=0.6, zorder=3)
    ax.add_patch(middle)

    # Bright center
    inner = Circle((x, y), size * 0.25, facecolor='yellow',
                   edgecolor='none', alpha=0.9, zorder=4)
    ax.add_patch(inner)

    if label_text:
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def failed_supernova(x, y, size=0.3, label_text='Failed SN\n(Direct Collapse)',
                     label_position='bottom', label_offset=None, ax=None):
    """Draw a failed supernova (direct collapse to black hole).

    Parameters
    ----------
    x : float
        X-coordinate of the object center.
    y : float
        Y-coordinate of the object center.
    size : float, optional
        Size of the black hole (default: 0.3).
    label_text : str, optional
        Text label to display near the object (default: 'Failed SN (Direct Collapse)').
    label_position : str, optional
        Position of the label relative to the object (default: 'bottom').
    label_offset : float, optional
        Distance offset from the object to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()

    # Fading envelope remnant
    envelope = Circle((x, y), size * 1.5, facecolor=colors['failed_sn'],
                      edgecolor='none', alpha=0.3, zorder=1)
    ax.add_patch(envelope)

    # Black hole
    bh = Circle((x, y), size, facecolor=colors['BH'],
                edgecolor='black', linewidth=0.5, zorder=3)
    ax.add_patch(bh)

    if label_text:
        if label_offset is None:
            label_offset = size * 1.5 + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def pair_instability_supernova(x, y, size=1.5, label_text='PISN',
                               label_position='bottom', label_offset=None, ax=None):
    """Draw a Pair-Instability Supernova (PISN).

    Complete disruption of a very massive star.

    Parameters
    ----------
    x : float
        X-coordinate of the supernova center.
    y : float
        Y-coordinate of the supernova center.
    size : float, optional
        Size of the supernova (default: 1.5).
    label_text : str, optional
        Text label to display near the supernova (default: 'PISN').
    label_position : str, optional
        Position of the label relative to the supernova (default: 'bottom').
    label_offset : float, optional
        Distance offset from the supernova to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    None
    """
    if ax is None:
        ax = plt.gca()

    # Massive outer explosion
    outer = Circle((x, y), size, facecolor=colors['pair_instability'],
                   edgecolor='darkred', linewidth=0.5, alpha=0.3, zorder=1)
    ax.add_patch(outer)

    # Middle layer
    middle = Circle((x, y), size * 0.6, facecolor='orangered',
                    edgecolor='none', alpha=0.5, zorder=2)
    ax.add_patch(middle)

    # Inner bright region
    inner = Circle((x, y), size * 0.3, facecolor='orange',
                   edgecolor='none', alpha=0.7, zorder=3)
    ax.add_patch(inner)

    # Bright core
    core = Circle((x, y), size * 0.1, facecolor='white',
                  edgecolor='none', alpha=0.9, zorder=4)
    ax.add_patch(core)

    if label_text:
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


# Alias
PISN = pair_instability_supernova


def stellar_merger(x, y, size=0.5, label_text='Merger Product',
                   label_position='bottom', label_offset=None, ax=None):
    """Draw a stellar merger product.

    Parameters
    ----------
    x : float
        X-coordinate of the merger product center.
    y : float
        Y-coordinate of the merger product center.
    size : float, optional
        Size of the merger product (default: 0.5).
    label_text : str, optional
        Text label to display near the merger product (default: 'Merger Product').
    label_position : str, optional
        Position of the label relative to the merger product (default: 'bottom').
    label_offset : float, optional
        Distance offset from the merger product to place the label.
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    return star(x, y, size=size, color=colors['merger_product'], edgecolor='deeppink',
                label_text=label_text, label_position=label_position,
                label_offset=label_offset, ax=ax)
