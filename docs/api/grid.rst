Grid System
===========

The Grid system provides an organized layout for arranging stellar objects and binaries with automatic spacing and directional arrow connections.

Overview
--------

The Grid class allows you to:

1. Create a grid with n columns and m rows
2. Assign stars or binaries to grid cells
3. Create directional arrow connections between cells
4. Automatically position elements with appropriate spacing for arrows

Basic Usage
-----------

Creating a Simple Grid
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from rua.canvas import setup_canvas
    from rua.grid import Grid
    from rua.components.stellar import star
    from rua.utils.colors import colors
    import matplotlib.pyplot as plt

    # Setup canvas
    fig, ax = setup_canvas(width=12, height=8)
    
    # Create a 2x3 grid
    grid = Grid(rows=2, cols=3, cell_width=2.0, cell_height=2.0, padding=0.8, ax=ax)
    
    # Add stars to grid positions
    grid.add_element(0, 0, star, size=0.3, color=colors['ZAMS'])
    grid.add_element(0, 1, star, size=0.35, color=colors['RGB'])
    grid.add_element(0, 2, star, size=0.4, color=colors['AGB'])
    
    # Add arrows between elements
    grid.add_connection(0, 0, 0, 1, label='evolve')
    grid.add_connection(0, 1, 0, 2)
    
    # Render the grid
    grid.render()
    plt.show()

Grid Parameters
~~~~~~~~~~~~~~~

When creating a Grid, you can specify:

* ``rows``: Number of rows (0-indexed from top)
* ``cols``: Number of columns (0-indexed from left)
* ``cell_width``: Width of each cell in plot units
* ``cell_height``: Height of each cell in plot units
* ``padding``: Extra space between cells for arrows
* ``ax``: Matplotlib axes to draw on

Adding Elements
---------------

Stars
~~~~~

Add individual stars to grid cells:

.. code-block:: python

    grid.add_element(row, col, star, size=0.3, color='yellow', label_text='ZAMS')

Binary Systems
~~~~~~~~~~~~~~

Add binary systems to grid cells:

.. code-block:: python

    from rua.components.binary import binary
    
    grid.add_element(0, 1, binary,
                    primary=star,
                    secondary=star,
                    size_primary=0.25,
                    size_secondary=0.2,
                    separation=0.6,
                    colors_tuple=(colors['ZAMS'], colors['lower_mass_ZAMS']))

Compact Objects
~~~~~~~~~~~~~~~

Add compact objects like white dwarfs, neutron stars, or black holes:

.. code-block:: python

    from rua.components.compact import white_dwarf, neutron_star, black_hole
    
    grid.add_element(1, 2, white_dwarf, size=0.2)
    grid.add_element(2, 0, neutron_star, size=0.15)
    grid.add_element(2, 1, black_hole, size=0.2)

Adding Connections
------------------

Automatic Direction Calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The grid automatically calculates optimal arrow directions based on element positions:

.. code-block:: python

    # Arrow automatically positioned from cell (0,0) to cell (0,1)
    grid.add_connection(0, 0, 0, 1)

8-Direction System
~~~~~~~~~~~~~~~~~~

Arrows can originate from 8 positions around each element:

* ``'N'``: North (top)
* ``'NE'``: Northeast
* ``'E'``: East (right)
* ``'SE'``: Southeast
* ``'S'``: South (bottom)
* ``'SW'``: Southwest
* ``'W'``: West (left)
* ``'NW'``: Northwest

Custom Arrow Directions
~~~~~~~~~~~~~~~~~~~~~~~~

Explicitly specify arrow anchor points:

.. code-block:: python

    grid.add_connection(0, 0, 1, 1, 
                       from_direction='SE', 
                       to_direction='NW')

Styled Arrows
~~~~~~~~~~~~~

Customize arrow appearance:

.. code-block:: python

    grid.add_connection(0, 0, 0, 1,
                       color='red',
                       linewidth=3,
                       linestyle='dashed',
                       label='mass transfer')

Available styles:
* ``linestyle``: 'solid', 'dashed', 'dotted', 'dashdot'
* ``color``: Any matplotlib color
* ``linewidth``: Line thickness
* ``arrow_style``: '->', '-|>', '-[', etc.

Method Chaining
---------------

The Grid class supports method chaining for cleaner code:

.. code-block:: python

    (Grid(rows=1, cols=5, cell_width=2.0, cell_height=2.0, ax=ax)
     .add_element(0, 0, star, size=0.25, color=colors['ZAMS'])
     .add_element(0, 1, star, size=0.3, color=colors['MS'])
     .add_element(0, 2, star, size=0.35, color=colors['RGB'])
     .add_connection(0, 0, 0, 1)
     .add_connection(0, 1, 0, 2)
     .render())

Examples
--------

Binary Evolution Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fig, ax = setup_canvas(width=14, height=6)
    grid = Grid(rows=1, cols=4, cell_width=2.5, cell_height=2.5, padding=0.6, ax=ax)
    
    # Stage 1: Initial binary
    grid.add_element(0, 0, binary,
                    primary=star, secondary=star,
                    size_primary=0.25, size_secondary=0.2,
                    colors_tuple=(colors['ZAMS'], colors['lower_mass_ZAMS']))
    
    # Stage 2: After mass transfer
    grid.add_element(0, 1, binary,
                    primary=star, secondary=star,
                    size_primary=0.35, size_secondary=0.2,
                    colors_tuple=(colors['RGB'], colors['ZAMS']))
    
    # Stage 3: After supernova
    grid.add_element(0, 2, binary,
                    primary=white_dwarf, secondary=star,
                    size_primary=0.15, size_secondary=0.25)
    
    # Stage 4: Final state
    grid.add_element(0, 3, binary,
                    primary=neutron_star, secondary=star,
                    size_primary=0.12, size_secondary=0.3)
    
    # Evolution arrows
    grid.add_connection(0, 0, 0, 1, label='MT1', color='blue')
    grid.add_connection(0, 1, 0, 2, label='SN', color='red')
    grid.add_connection(0, 2, 0, 3, label='MT2', color='green')
    
    grid.render()
    plt.show()

Complex Evolution Network
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fig, ax = setup_canvas(width=15, height=10)
    grid = Grid(rows=3, cols=3, cell_width=2.0, cell_height=2.0, padding=0.7, ax=ax)
    
    # Top row - initial states
    grid.add_element(0, 0, star, size=0.3, color=colors['ZAMS'])
    grid.add_element(0, 1, binary, primary=star, secondary=star,
                    size_primary=0.25, size_secondary=0.2)
    grid.add_element(0, 2, star, size=0.4, color=colors['RGB'])
    
    # Middle row - intermediate states
    grid.add_element(1, 0, star, size=0.35, color=colors['RGB'])
    grid.add_element(1, 2, white_dwarf, size=0.2)
    
    # Bottom row - final states
    grid.add_element(2, 0, white_dwarf, size=0.2)
    grid.add_element(2, 2, black_hole, size=0.25)
    
    # Vertical evolution paths
    grid.add_connection(0, 0, 1, 0, color='blue')
    grid.add_connection(1, 0, 2, 0, color='blue')
    grid.add_connection(0, 2, 1, 2, color='red')
    grid.add_connection(1, 2, 2, 2, color='red')
    
    # Diagonal connections
    grid.add_connection(0, 0, 1, 1, linestyle='dashed', color='gray')
    
    grid.render()
    plt.show()

API Reference
-------------

.. autoclass:: rua.grid.Grid
   :members:
   :undoc-members:
   :show-inheritance:
