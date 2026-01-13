"""
Single stellar object drawing functions.
Contains functions for drawing individual stars and stellar phases.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.image as mpimg
import os

from rua.utils.colors import colors
from rua.components.decorator import label

# Get the path to the resources directory
_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_RESOURCES_DIR = os.path.join(os.path.dirname(_MODULE_DIR), 'resources')
_DEFAULT_SUPERNOVA_PATH = os.path.join(_RESOURCES_DIR, 'supernova.png')


def star(ax, x, y, size=0.3, color='yellow', edgecolor='black', 
         label_text='', label_position='bottom', label_offset=None, **kwargs):
    """
    Draw a cartoon star representation.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
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
    **kwargs
        Additional keyword arguments passed to matplotlib Circle patch.

    Returns
    -------
    circle : matplotlib.patches.Circle
        The Circle patch object added to the axis.
    """
    circle = Circle((x, y), size, facecolor=color, edgecolor=edgecolor, 
                    linewidth=0.5, zorder=3, **kwargs)
    ax.add_patch(circle)
    
    if label_text:
        # Auto-scale label offset with size if not specified
        if label_offset is None:
            label_offset = size + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)
    
    return circle


def supernova_image(ax, x, y, size=1.0, label_text='', label_position='bottom', 
                    label_offset=None, image_path=None):
    """
    Display supernova PNG image at specified location.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
    x : float
        X-coordinate of the supernova center.
    y : float
        Y-coordinate of the supernova center.
    size : float, optional
        Size of the supernova image (default: 1.0).
    label_text : str, optional
        Text label to display near the supernova (default: '').
    label_position : str, optional
        Position of the label relative to the supernova (default: 'bottom').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the supernova to place the label.
        If None, automatically scales with size (default: None).
    image_path : str, optional
        Path to supernova image file (default: uses package resources).

    Returns
    -------
    None
    """
    if image_path is None:
        image_path = _DEFAULT_SUPERNOVA_PATH

    if os.path.exists(image_path):
        img = mpimg.imread(image_path)
        # Calculate extent to center the image at (x, y) with given size
        extent = [x - size/2, x + size/2, y - size/2, y + size/2]
        ax.imshow(img, extent=extent, aspect='auto', zorder=3)
    else:
        # Fallback to drawing a simple star if image not found
        star(ax, x, y, size=size/2, color='orange', edgecolor='red')
    
    if label_text:
        # Auto-scale label offset with size if not specified
        if label_offset is None:
            label_offset = size/2 + 0.15
        label(ax, x, y, label_text, label_position, label_offset=label_offset)


def zams(ax, x, y, size=0.4, label_text='ZAMS\n(Main Sequence)', 
         label_position='bottom', label_offset=None):
    """
    Draw a ZAMS (Zero Age Main Sequence) star.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.4).
    label_text : str, optional
        Text label to display near the star (default: 'ZAMS\n(Main Sequence)').
    label_position : str, optional
        Position of the label relative to the star (default: 'bottom').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the star to place the label.
        If None, automatically scales with size (default: None).

    Returns
    -------
    None
    """
    star(ax, x, y, size=size, color=colors['ZAMS'], edgecolor='black',
         label_text=label_text, label_position=label_position, 
         label_offset=label_offset)


def wolf_rayet(ax, x, y, size=0.45, label_text='WR Phase\n(He-burning)', 
               label_position='right', label_offset=None):
    """
    Draw a Wolf-Rayet phase star.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
    x : float
        X-coordinate of the star center.
    y : float
        Y-coordinate of the star center.
    size : float, optional
        Radius of the star (default: 0.45).
    label_text : str, optional
        Text label to display near the star (default: 'WR Phase\n(He-burning)').
    label_position : str, optional
        Position of the label relative to the star (default: 'right').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the star to place the label.
        If None, automatically scales with size (default: None).

    Returns
    -------
    None
    """
    star(ax, x, y, size=size, color=colors['WR'], edgecolor='black',
         label_text=label_text, label_position=label_position,
         label_offset=label_offset)


def supernova(ax, x, y, size=1.2, label_text='Supernova\n(BH/NS)', 
              label_position='right', label_offset=None, image_path=None):
    """
    Draw a supernova explosion.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
    x : float
        X-coordinate of the supernova center.
    y : float
        Y-coordinate of the supernova center.
    size : float, optional
        Size of the supernova image (default: 1.2).
    label_text : str, optional
        Text label to display near the supernova (default: 'Supernova\n(BH/NS)').
    label_position : str, optional
        Position of the label relative to the supernova (default: 'right').
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the supernova to place the label.
        If None, automatically scales with size (default: None).
    image_path : str, optional
        Path to supernova image file (default: uses package resources).

    Returns
    -------
    None
    """
    supernova_image(ax, x, y, size=size, label_text=label_text, 
                    label_position=label_position, label_offset=label_offset,
                    image_path=image_path)
