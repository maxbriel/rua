"""
Test and demonstration of the Grid system.

This script shows various examples of using the grid system for organizing
stellar objects and creating evolution diagrams.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.grid import Grid
from rua.components.stellar import star
from rua.components.binary import binary
from rua.components.compact import black_hole, neutron_star, white_dwarf
from rua.utils.colors import colors


def test_simple_grid():
    """Test a simple 2x3 grid with stars."""
    fig, ax = setup_canvas(width=12, height=8)
    
    # Create grid
    grid = Grid(rows=2, cols=3, cell_width=2.0, cell_height=2.0, padding=0.8, ax=ax)
    
    # Add stars to different positions
    grid.add_element(0, 0, star, size=0.3, color=colors['ZAMS'])
    grid.add_element(0, 1, star, size=0.35, color=colors['RGB'])
    grid.add_element(0, 2, star, size=0.4, color=colors['AGB'])
    grid.add_element(1, 0, star, size=0.25, color=colors['lower_mass_ZAMS'])
    grid.add_element(1, 2, white_dwarf, size=0.2)
    
    # Add connections showing evolution
    grid.add_connection(0, 0, 0, 1, label='evolve')
    grid.add_connection(0, 1, 0, 2)
    grid.add_connection(0, 2, 1, 2, label='collapse')
    
    # Render the grid
    grid.render()
    
    plt.savefig('test_grid_simple.png', dpi=150, bbox_inches='tight')
    print("✓ Simple grid test saved as test_grid_simple.png")
    plt.close()


def test_binary_grid():
    """Test grid with binary systems."""
    fig, ax = setup_canvas(width=14, height=6)
    
    # Create grid
    grid = Grid(rows=1, cols=4, cell_width=2.5, cell_height=2.5, padding=0.6, ax=ax)
    
    # Add binary systems at different stages
    grid.add_element(0, 0, binary,
                    primary=star,
                    secondary=star,
                    size_primary=0.25,
                    size_secondary=0.2,
                    separation=0.6,
                    colors_tuple=(colors['ZAMS'], colors['lower_mass_ZAMS']))
    
    grid.add_element(0, 1, binary,
                    primary=star,
                    secondary=star,
                    size_primary=0.35,
                    size_secondary=0.2,
                    separation=0.65,
                    colors_tuple=(colors['RGB'], colors['ZAMS']))
    
    grid.add_element(0, 2, binary,
                    primary=white_dwarf,
                    secondary=star,
                    size_primary=0.15,
                    size_secondary=0.25,
                    separation=0.6)
    
    grid.add_element(0, 3, binary,
                    primary=neutron_star,
                    secondary=star,
                    size_primary=0.12,
                    size_secondary=0.3,
                    separation=0.7)
    
    # Add evolution arrows
    grid.add_connection(0, 0, 0, 1, label='MT1')
    grid.add_connection(0, 1, 0, 2, label='SN')
    grid.add_connection(0, 2, 0, 3, label='MT2')
    
    grid.render()
    
    plt.savefig('test_grid_binary.png', dpi=150, bbox_inches='tight')
    print("✓ Binary grid test saved as test_grid_binary.png")
    plt.close()


def test_complex_grid():
    """Test a more complex grid with multiple connections."""
    fig, ax = setup_canvas(width=15, height=10)
    
    # Create a 3x3 grid
    grid = Grid(rows=3, cols=3, cell_width=2.0, cell_height=2.0, padding=0.7, ax=ax)
    
    # Top row - initial states
    grid.add_element(0, 0, star, size=0.3, color=colors['ZAMS'], label_text='ZAMS')
    grid.add_element(0, 1, binary, primary=star, secondary=star,
                    size_primary=0.25, size_secondary=0.2, separation=0.6,
                    colors_tuple=(colors['ZAMS'], colors['lower_mass_ZAMS']))
    grid.add_element(0, 2, star, size=0.4, color=colors['RGB'])
    
    # Middle row - intermediate states
    grid.add_element(1, 0, star, size=0.35, color=colors['RGB'])
    grid.add_element(1, 1, binary, primary=star, secondary=star,
                    size_primary=0.35, size_secondary=0.2, separation=0.65,
                    colors_tuple=(colors['RGB'], colors['ZAMS']))
    grid.add_element(1, 2, white_dwarf, size=0.2)
    
    # Bottom row - final states
    grid.add_element(2, 0, white_dwarf, size=0.2)
    grid.add_element(2, 1, binary, primary=neutron_star, secondary=star,
                    size_primary=0.12, size_secondary=0.25, separation=0.6)
    grid.add_element(2, 2, black_hole, size=0.25)
    
    # Add connections - vertical evolution
    grid.add_connection(0, 0, 1, 0, color='blue')
    grid.add_connection(1, 0, 2, 0, color='blue')
    grid.add_connection(0, 1, 1, 1, color='green')
    grid.add_connection(1, 1, 2, 1, color='green')
    grid.add_connection(0, 2, 1, 2, color='red')
    grid.add_connection(1, 2, 2, 2, color='red')
    
    # Add some diagonal connections
    grid.add_connection(0, 0, 1, 1, linestyle='dashed', color='gray')
    grid.add_connection(1, 1, 2, 2, linestyle='dashed', color='gray')
    
    grid.render()
    
    plt.savefig('test_grid_complex.png', dpi=150, bbox_inches='tight')
    print("✓ Complex grid test saved as test_grid_complex.png")
    plt.close()


def test_directional_arrows():
    """Test the 8-directional arrow system."""
    fig, ax = setup_canvas(width=12, height=12)
    
    # Create a 3x3 grid with center element
    grid = Grid(rows=3, cols=3, cell_width=2.5, cell_height=2.5, padding=0.5, ax=ax)
    
    # Place star in center
    grid.add_element(1, 1, star, size=0.4, color='yellow', label_text='Center')
    
    # Place stars in all 8 directions
    grid.add_element(0, 1, star, size=0.25, color=colors['lower_mass_ZAMS'])  # N
    grid.add_element(0, 2, star, size=0.25, color=colors['lower_mass_ZAMS'])  # NE
    grid.add_element(1, 2, star, size=0.25, color=colors['lower_mass_ZAMS'])  # E
    grid.add_element(2, 2, star, size=0.25, color=colors['lower_mass_ZAMS'])  # SE
    grid.add_element(2, 1, star, size=0.25, color=colors['lower_mass_ZAMS'])  # S
    grid.add_element(2, 0, star, size=0.25, color=colors['lower_mass_ZAMS'])  # SW
    grid.add_element(1, 0, star, size=0.25, color=colors['lower_mass_ZAMS'])  # W
    grid.add_element(0, 0, star, size=0.25, color=colors['lower_mass_ZAMS'])  # NW
    
    # Add arrows from center to all directions
    grid.add_connection(1, 1, 0, 1, color='red')      # to N
    grid.add_connection(1, 1, 0, 2, color='orange')   # to NE
    grid.add_connection(1, 1, 1, 2, color='yellow')   # to E
    grid.add_connection(1, 1, 2, 2, color='green')    # to SE
    grid.add_connection(1, 1, 2, 1, color='cyan')     # to S
    grid.add_connection(1, 1, 2, 0, color='blue')     # to SW
    grid.add_connection(1, 1, 1, 0, color='purple')   # to W
    grid.add_connection(1, 1, 0, 0, color='magenta')  # to NW
    
    grid.render()
    
    plt.savefig('test_grid_directions.png', dpi=150, bbox_inches='tight')
    print("✓ Directional arrows test saved as test_grid_directions.png")
    plt.close()


def test_evolution_pathway():
    """Test creating a stellar evolution pathway."""
    fig, ax = setup_canvas(width=18, height=6)
    
    # Create a horizontal evolution pathway
    grid = Grid(rows=1, cols=6, cell_width=2.0, cell_height=2.0, padding=0.8, ax=ax)
    
    # Add evolutionary stages
    grid.add_element(0, 0, star, size=0.25, color=colors['ZAMS'], label_text='ZAMS')
    grid.add_element(0, 1, star, size=0.3, color=colors['MS'], label_text='MS')
    grid.add_element(0, 2, star, size=0.35, color=colors['RGB'], label_text='RGB')
    grid.add_element(0, 3, star, size=0.4, color=colors['CHeB'], label_text='CHeB')
    grid.add_element(0, 4, star, size=0.45, color=colors['AGB'], label_text='AGB')
    grid.add_element(0, 5, white_dwarf, size=0.2, label_text='WD')
    
    # Add evolution arrows
    for i in range(5):
        grid.add_connection(0, i, 0, i+1, color='black', linewidth=2.5)
    
    grid.render()
    
    plt.savefig('test_grid_evolution.png', dpi=150, bbox_inches='tight')
    print("✓ Evolution pathway test saved as test_grid_evolution.png")
    plt.close()


if __name__ == '__main__':
    print("Running Grid system tests...\n")
    
    test_simple_grid()
    test_binary_grid()
    test_complex_grid()
    test_directional_arrows()
    test_evolution_pathway()
    
    print("\n✓ All tests completed successfully!")
    print("Check the generated PNG files to see the results.")
