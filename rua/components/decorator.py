"""
Decorator and annotation functions for stellar diagrams.

Contains utilities for labels, arrows, and other visual elements.
"""

from matplotlib.patches import FancyArrowPatch


def label(ax, x, y, label_text, label_position='bottom', label_offset=0.6):
    """
    Add a label to an object at the specified position.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
    x : float
        X-coordinate of the object.
    y : float
        Y-coordinate of the object.
    label_text : str
        The text to display in the label.
    label_position : str
        Position of the label relative to the object.
        Options: 'top', 'bottom', 'left', 'right'.
    label_offset : float, optional
        Distance offset from the object to place the label (default: 0.4).

    Returns
    -------
    None
    """
    offset = label_offset
    
    # Define position mappings
    if label_position == 'bottom':
        label_x, label_y, ha, va = x, y - offset, 'center', 'top'
    elif label_position == 'top':
        label_x, label_y, ha, va = x, y + offset, 'center', 'bottom'
    elif label_position == 'left':
        label_x, label_y, ha, va = x - offset, y, 'right', 'center'
    elif label_position == 'right':
        label_x, label_y, ha, va = x + offset, y, 'left', 'center'
    else:
        # Default to bottom
        label_x, label_y, ha, va = x, y - offset, 'center', 'top'
    
    ax.text(label_x, label_y, label_text, ha=ha, va=va, fontweight='bold')


def arrow(ax, x1, y1, x2, y2,
               label='', style='solid', color='black',
               width=2, label_position='right', label_offset=0.4):
    """
    Draw an arrow between two points with optional label.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
    x1 : float
        X-coordinate of arrow start position.
    y1 : float
        Y-coordinate of arrow start position.
    x2 : float
        X-coordinate of arrow end position.
    y2 : float
        Y-coordinate of arrow end position.
    label : str, optional
        Text label to display at the midpoint of the arrow (default: '').
    style : str, optional
        Line style for the arrow (default: 'solid').
        Options: 'solid', 'dashed', 'dotted', 'dashdot'.
    color : str, optional
        Color of the arrow (default: 'black').
    width : int or float, optional
        Line width of the arrow (default: 2).
    label_position : str, optional
        Position of the label relative to the arrow midpoint (default: 'right').
        Options: 'top', 'bottom', 'left', 'right'.

    Returns
    -------
    None
    """
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle='->', mutation_scale=20,
                            linewidth=width, color=color,
                            linestyle=style, zorder=2)
    ax.add_patch(arrow)
    
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        # Label position offsets
        label_offset = label_offset
        
        if label_position == 'right':
            label_x = mid_x + label_offset - 0.2
            label_y = mid_y
            ha = 'left'
            va = 'center'
        elif label_position == 'left':
            label_x = mid_x - label_offset + 0.2
            label_y = mid_y
            ha = 'right'
            va = 'center'
        elif label_position == 'top':
            label_x = mid_x
            label_y = mid_y + label_offset - 0.2
            ha = 'center'
            va = 'bottom'
        elif label_position == 'bottom':
            label_x = mid_x
            label_y = mid_y - label_offset + 0.2
            ha = 'center'
            va = 'top'
        else:
            # Default to right
            label_x = mid_x + label_offset - 0.2
            label_y = mid_y
            ha = 'left'
            va = 'center'
        
        ax.text(label_x, label_y, label, ha=ha,
                va=va, fontsize=8,
                style='italic',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                         alpha=0.8))
