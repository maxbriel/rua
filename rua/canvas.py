"""
Canvas setup functions for creating clean diagram figures.
"""

import matplotlib.pyplot as plt


def setup_canvas(width=10, height=6, xlim=(-5, 5), ylim=(-3, 3), 
                 aspect='equal', remove_axes=True):
    """Create a clean canvas for drawing stellar evolution diagrams.

    Sets up a matplotlib figure with no padding, no axes/ticks, and 
    specified dimensions and limits.

    Parameters
    ----------
    width : float, optional
        Width of the figure in inches (default: 10).
    height : float, optional
        Height of the figure in inches (default: 6).
    xlim : tuple, optional
        X-axis limits as (min, max) (default: (-5, 5)).
    ylim : tuple, optional
        Y-axis limits as (min, max) (default: (-3, 3)).
    aspect : str, optional
        Aspect ratio of the plot (default: 'equal').
        Options: 'equal', 'auto', or numeric ratio.
    remove_axes : bool, optional
        If True, remove axis lines, ticks, and labels (default: True).

    Returns
    -------
    fig : matplotlib.figure.Figure
        The created figure object.
    ax : matplotlib.axes.Axes
        The axes object for drawing.

    Examples
    --------
    >>> from rua.canvas import setup_canvas
    >>> from rua.components.stellar import star
    >>> 
    >>> fig, ax = setup_canvas(width=12, height=8)
    >>> star(0, 0, size=0.5, color='yellow', ax=ax)
    >>> plt.show()
    """
    fig, ax = plt.subplots(figsize=(width, height))
    
    # Set axis limits
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
    # Set aspect ratio
    ax.set_aspect(aspect)
    
    if remove_axes:
        # Remove axes, ticks, and labels
        ax.axis('off')
    
    # Remove padding around the plot
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    return fig, ax
