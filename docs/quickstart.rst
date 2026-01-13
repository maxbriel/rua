Quick Start Guide
=================

This guide will help you get started with Rua for creating stellar evolution diagrams.

Basic Usage
-----------

Single Stars
~~~~~~~~~~~~

Drawing individual stars is straightforward::

    import matplotlib.pyplot as plt
    from rua.components.stellar import star, zams, wolf_rayet
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw a basic star
    star(0, 0, size=0.5, color='yellow', ax=ax)
    
    # Draw a ZAMS star
    zams(2, 0, size=0.4, ax=ax)
    
    # Draw a Wolf-Rayet star
    wolf_rayet(4, 0, size=0.45, ax=ax)
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    plt.show()

Binary Systems
~~~~~~~~~~~~~~

Creating binary star systems::

    import matplotlib.pyplot as plt
    from rua.components.binary import binary, HMS_HMS
    from rua.components.stellar import star
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw a basic binary
    binary(0, 0,
           primary=star,
           secondary=star,
           size_primary=0.3,
           size_secondary=0.25,
           separation=1.0,
           ax=ax)
    
    # Draw a high-mass binary
    HMS_HMS(3, 0,
            size_primary=0.35,
            size_secondary=0.3,
            separation=1.2,
            ax=ax)
    
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    plt.show()

Special Binary Phases
~~~~~~~~~~~~~~~~~~~~~

Visualizing advanced binary evolution phases::

    import matplotlib.pyplot as plt
    from rua.components.binary import common_envelope, roche_lobe_overflow
    from rua.components.stellar import star
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw common envelope phase
    common_envelope(0, 0,
                    primary=star,
                    secondary=star,
                    envelope_size=1.0,
                    ax=ax)
    
    # Draw Roche lobe overflow
    roche_lobe_overflow(3, 0,
                        accretor=star,
                        donor_size=0.35,
                        accretor_size=0.25,
                        ax=ax)
    
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    plt.show()

Compact Objects
~~~~~~~~~~~~~~~

Drawing compact objects::

    import matplotlib.pyplot as plt
    from rua.components.compact import NS, BH, WD, compact_objects
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw a neutron star
    NS(0, 0, size=0.1, ax=ax)
    
    # Draw a black hole
    BH(1.5, 0, size=0.2, ax=ax)
    
    # Draw a white dwarf
    WD(3, 0, size=0.15, ax=ax)
    
    # Draw NS/BH either-or representation
    compact_objects(5, 0, size=0.2, ax=ax)
    
    ax.set_xlim(-1, 6)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    plt.show()

Customization
-------------

Colors
~~~~~~

You can customize colors using the built-in color palette or your own::

    from rua.components.stellar import star
    from rua.utils.colors import colors
    
    # Using built-in colors
    star(0, 0, size=0.5, color=colors['ZAMS'])
    
    # Using custom colors
    star(2, 0, size=0.5, color='#FF6B6B')

Labels
~~~~~~

Add labels to your objects::

    from rua.components.stellar import zams
    
    zams(0, 0, 
         size=0.5,
         label_text='Main Sequence',
         label_position='bottom')

Next Steps
----------

For detailed API documentation, see the :doc:`api/index` section.
