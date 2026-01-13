Welcome to Rua's documentation!
==================================

Rua is a Python package for creating stellar evolution diagrams of binary systems.
It provides tools to visualize various stellar phenomena including Roche lobe overflow,
common envelope phases, mass transfer, supernova explosions, and compact object formation.

Features
--------

- Create diagrams for single star evolution
- Create complex diagrams for binary star evolution
- Visualize various stellar phenomena:
  
  - Roche lobe overflow
  - Common envelope phases
  - Mass transfer
  - Supernova explosions
  - Compact object formation (neutron stars, black holes)

Installation
------------

From source::

    pip install -e .

For development::

    pip install -e ".[dev]"

Quick Start
-----------

Here's a simple example to get you started::

    import matplotlib.pyplot as plt
    from rua.components.stellar import star, zams
    from rua.components.binary import binary, HMS_HMS
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw a single star
    star(0, 0, size=0.5, color='yellow')
    
    # Draw a binary system
    HMS_HMS(3, 0, size_primary=0.4, size_secondary=0.3)
    
    plt.axis('equal')
    plt.show()

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
