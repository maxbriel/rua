"""
Grid system for organizing and connecting stellar objects.

Provides a grid layout system for arranging stars and binaries with automatic
spacing and directional arrow connections between elements.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


class Grid:
    """
    A grid system for organizing stellar objects and their connections.
    
    The grid provides automatic spacing and positioning for stars and binaries,
    with support for directional arrows between grid elements.
    
    Parameters
    ----------
    rows : int
        Number of rows in the grid.
    cols : int
        Number of columns in the grid.
    cell_width : float, optional
        Width of each grid cell (default: 2.0).
    cell_height : float, optional
        Height of each grid cell (default: 2.0).
    padding : float, optional
        Extra padding between cells for arrows (default: 0.5).
    ax : matplotlib.axes.Axes, optional
        The matplotlib axis to draw on (default: None, uses current axes).
    
    Attributes
    ----------
    rows : int
        Number of rows in the grid.
    cols : int
        Number of columns in the grid.
    cell_width : float
        Width of each grid cell.
    cell_height : float
        Height of each grid cell.
    padding : float
        Padding between cells.
    ax : matplotlib.axes.Axes
        The matplotlib axis to draw on.
    elements : dict
        Dictionary storing grid elements at (row, col) positions.
    connections : list
        List of connection definitions between grid elements.
    
    Examples
    --------
    >>> from rua.canvas import setup_canvas
    >>> from rua.grid import Grid
    >>> from rua.components.stellar import star
    >>> from rua.components.binary import binary
    >>> 
    >>> fig, ax = setup_canvas(width=15, height=10)
    >>> grid = Grid(rows=2, cols=3, ax=ax)
    >>> 
    >>> # Add stars to grid
    >>> grid.add_element(0, 0, star, size=0.3, color='yellow')
    >>> grid.add_element(0, 1, star, size=0.4, color='orange')
    >>> 
    >>> # Add connection between elements
    >>> grid.add_connection(0, 0, 0, 1)
    >>> 
    >>> # Render the grid
    >>> grid.render()
    >>> plt.show()
    """
    
    def __init__(self, rows, cols, cell_width=2.0, cell_height=2.0, 
                 padding=0.5, ax=None):
        """Initialize the grid system."""
        self.rows = rows
        self.cols = cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.padding = padding
        self.ax = ax if ax is not None else plt.gca()
        
        # Storage for grid elements and connections
        self.elements = {}  # (row, col): element_info
        self.connections = []  # List of (from_row, from_col, to_row, to_col, arrow_props)
        
    def _get_cell_center(self, row, col):
        """
        Calculate the center position of a grid cell.
        
        Parameters
        ----------
        row : int
            Row index (0-based).
        col : int
            Column index (0-based).
        
        Returns
        -------
        tuple
            (x, y) coordinates of the cell center.
        """
        x = col * (self.cell_width + self.padding) + self.cell_width / 2
        y = (self.rows - 1 - row) * (self.cell_height + self.padding) + self.cell_height / 2
        return x, y
    
    def _get_arrow_anchor(self, row, col, direction):
        """
        Get the anchor point for an arrow at one of 8 positions around a cell.
        
        Parameters
        ----------
        row : int
            Row index of the cell.
        col : int
            Column index of the cell.
        direction : str
            Direction of the arrow: 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'.
        
        Returns
        -------
        tuple
            (x, y) coordinates of the anchor point.
        """
        cx, cy = self._get_cell_center(row, col)
        
        # Define offset for each direction (as fraction of cell size)
        # Using a slightly smaller radius to keep arrows away from edges
        radius_x = self.cell_width * 0.4
        radius_y = self.cell_height * 0.4
        
        direction_offsets = {
            'N':  (0, radius_y),
            'NE': (radius_x * 0.7, radius_y * 0.7),
            'E':  (radius_x, 0),
            'SE': (radius_x * 0.7, -radius_y * 0.7),
            'S':  (0, -radius_y),
            'SW': (-radius_x * 0.7, -radius_y * 0.7),
            'W':  (-radius_x, 0),
            'NW': (-radius_x * 0.7, radius_y * 0.7),
        }
        
        offset_x, offset_y = direction_offsets.get(direction, (0, 0))
        return cx + offset_x, cy + offset_y
    
    def _calculate_arrow_direction(self, from_row, from_col, to_row, to_col):
        """
        Calculate the optimal arrow direction based on relative positions.
        
        Parameters
        ----------
        from_row : int
            Starting row index.
        from_col : int
            Starting column index.
        to_row : int
            Ending row index.
        to_col : int
            Ending column index.
        
        Returns
        -------
        tuple
            (from_direction, to_direction) as strings.
        """
        row_diff = to_row - from_row
        col_diff = to_col - from_col
        
        # Determine primary and secondary directions
        if row_diff == 0 and col_diff > 0:
            return 'E', 'W'
        elif row_diff == 0 and col_diff < 0:
            return 'W', 'E'
        elif col_diff == 0 and row_diff > 0:
            return 'S', 'N'
        elif col_diff == 0 and row_diff < 0:
            return 'N', 'S'
        elif row_diff > 0 and col_diff > 0:
            return 'SE', 'NW'
        elif row_diff > 0 and col_diff < 0:
            return 'SW', 'NE'
        elif row_diff < 0 and col_diff > 0:
            return 'NE', 'SW'
        elif row_diff < 0 and col_diff < 0:
            return 'NW', 'SE'
        else:
            return 'E', 'W'  # Default
    
    def add_element(self, row, col, draw_func, **kwargs):
        """
        Add a star or binary element to a grid cell.
        
        Parameters
        ----------
        row : int
            Row index (0-based, 0 is top).
        col : int
            Column index (0-based, 0 is left).
        draw_func : callable
            Function to draw the element (e.g., star, binary).
        **kwargs
            Additional keyword arguments passed to the draw function.
        
        Returns
        -------
        Grid
            Returns self for method chaining.
        
        Examples
        --------
        >>> grid.add_element(0, 0, star, size=0.3, color='yellow')
        >>> grid.add_element(0, 1, binary, primary=star, secondary=star)
        """
        if row < 0 or row >= self.rows:
            raise ValueError(f"Row {row} is out of bounds (0 to {self.rows-1})")
        if col < 0 or col >= self.cols:
            raise ValueError(f"Column {col} is out of bounds (0 to {self.cols-1})")
        
        self.elements[(row, col)] = {
            'draw_func': draw_func,
            'kwargs': kwargs
        }
        return self
    
    def add_connection(self, from_row, from_col, to_row, to_col, 
                      from_direction=None, to_direction=None,
                      arrow_style='->', color='black', linewidth=2,
                      linestyle='solid', label='', **kwargs):
        """
        Add a directional arrow connection between two grid elements.
        
        Parameters
        ----------
        from_row : int
            Starting row index.
        from_col : int
            Starting column index.
        to_row : int
            Ending row index.
        to_col : int
            Ending column index.
        from_direction : str, optional
            Direction anchor for arrow start: 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'.
            If None, automatically calculated (default: None).
        to_direction : str, optional
            Direction anchor for arrow end: 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'.
            If None, automatically calculated (default: None).
        arrow_style : str, optional
            Matplotlib arrow style (default: '->').
        color : str, optional
            Arrow color (default: 'black').
        linewidth : float, optional
            Arrow line width (default: 2).
        linestyle : str, optional
            Line style: 'solid', 'dashed', 'dotted', 'dashdot' (default: 'solid').
        label : str, optional
            Label text for the arrow (default: '').
        **kwargs
            Additional keyword arguments passed to FancyArrowPatch.
        
        Returns
        -------
        Grid
            Returns self for method chaining.
        
        Examples
        --------
        >>> # Auto-calculated directions
        >>> grid.add_connection(0, 0, 0, 1)
        >>> 
        >>> # Explicit directions
        >>> grid.add_connection(0, 0, 1, 1, from_direction='SE', to_direction='NW')
        >>> 
        >>> # Styled arrow
        >>> grid.add_connection(0, 0, 0, 1, color='red', linewidth=3, 
        ...                     linestyle='dashed', label='evolution')
        """
        # Auto-calculate directions if not provided
        if from_direction is None or to_direction is None:
            auto_from, auto_to = self._calculate_arrow_direction(
                from_row, from_col, to_row, to_col
            )
            from_direction = from_direction or auto_from
            to_direction = to_direction or auto_to
        
        self.connections.append({
            'from_row': from_row,
            'from_col': from_col,
            'to_row': to_row,
            'to_col': to_col,
            'from_direction': from_direction,
            'to_direction': to_direction,
            'arrow_style': arrow_style,
            'color': color,
            'linewidth': linewidth,
            'linestyle': linestyle,
            'label': label,
            'kwargs': kwargs
        })
        return self
    
    def render(self):
        """
        Render all grid elements and connections.
        
        This method draws all added stars, binaries, and arrows onto the
        matplotlib axes.
        
        Returns
        -------
        Grid
            Returns self for method chaining.
        
        Examples
        --------
        >>> grid.add_element(0, 0, star, size=0.3)
        >>> grid.add_element(0, 1, star, size=0.3)
        >>> grid.add_connection(0, 0, 0, 1)
        >>> grid.render()
        """
        # Draw all elements first
        for (row, col), element_info in self.elements.items():
            x, y = self._get_cell_center(row, col)
            draw_func = element_info['draw_func']
            kwargs = element_info['kwargs'].copy()
            
            # Add ax parameter if not already present
            if 'ax' not in kwargs:
                kwargs['ax'] = self.ax
            
            # Call the drawing function
            draw_func(x, y, **kwargs)
        
        # Draw all connections
        for conn in self.connections:
            x1, y1 = self._get_arrow_anchor(
                conn['from_row'], conn['from_col'], conn['from_direction']
            )
            x2, y2 = self._get_arrow_anchor(
                conn['to_row'], conn['to_col'], conn['to_direction']
            )
            
            # Create arrow
            arrow = FancyArrowPatch(
                (x1, y1), (x2, y2),
                arrowstyle=conn['arrow_style'],
                color=conn['color'],
                linewidth=conn['linewidth'],
                linestyle=conn['linestyle'],
                mutation_scale=20,
                zorder=1,
                **conn['kwargs']
            )
            self.ax.add_patch(arrow)
            
            # Add label if provided
            if conn['label']:
                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2
                self.ax.text(mid_x, mid_y, conn['label'],
                           ha='center', va='center',
                           bbox=dict(boxstyle='round,pad=0.3', 
                                   facecolor='white', edgecolor='none', alpha=0.8))
        
        return self
    
    def get_grid_dimensions(self):
        """
        Get the total dimensions of the grid.
        
        Returns
        -------
        tuple
            (total_width, total_height) of the entire grid.
        
        Examples
        --------
        >>> grid = Grid(rows=2, cols=3, cell_width=2.0, cell_height=2.0)
        >>> width, height = grid.get_grid_dimensions()
        """
        total_width = self.cols * self.cell_width + (self.cols - 1) * self.padding
        total_height = self.rows * self.cell_height + (self.rows - 1) * self.padding
        return total_width, total_height
    
    def clear(self):
        """
        Clear all elements and connections from the grid.
        
        Returns
        -------
        Grid
            Returns self for method chaining.
        """
        self.elements = {}
        self.connections = []
        return self
