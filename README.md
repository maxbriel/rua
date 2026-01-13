# Binary Diagrams

A Python package for creating stellar evolution diagrams, particularly for binary systems evolving to Wolf-Rayet phases.

📚 **[Quick Start Guide](QUICKSTART.md)** | 🛠️ **[Setup Guide](SETUP_GUIDE.md)** | 📖 **[Examples](examples/)**

## Features

- Create diagrams for single star evolution to Wolf-Rayet phase
- Create complex diagrams for binary star evolution
- Visualize various stellar phenomena:
  - Roche lobe overflow
  - Common envelope phases
  - Mass transfer
  - Supernova explosions
  - Compact object formation (neutron stars, black holes)

## Installation

### From source

```bash
pip install -e .
```

### For development

```bash
pip install -e ".[dev]"
```

## Usage

### As a library

```python
from binary_diagrams import create_binary_diagram, create_single_star_diagram

# Create a binary star evolution diagram
create_binary_diagram()

# Create a single star evolution diagram
create_single_star_diagram()
```

### Using individual drawing functions

```python
import matplotlib.pyplot as plt
from binary_diagrams import draw_roche_lobe_overflow, draw_wr_star

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis('off')

# Draw a Roche lobe overflow system
draw_roche_lobe_overflow(ax, 4, 3, donor_size=0.35, accretor_size=0.25)

# Draw a Wolf-Rayet star
draw_wr_star(ax, 2, 4, size=0.5, label_text='WR Phase')

plt.savefig('my_diagram.png', dpi=300, bbox_inches='tight')
plt.show()
```

### Command-line interface

After installation, you can use the command-line tools:

```bash
# Create binary evolution diagram
create-binary-diagram

# Create single star evolution diagram
create-single-star-diagram
```

## Available Drawing Functions

The package provides many reusable drawing functions:

- `draw_star()` - Draw a basic star
- `draw_binary()` - Draw a binary star system
- `draw_zams_star()` - Draw a zero-age main sequence star
- `draw_zams_binary()` - Draw a ZAMS binary system
- `draw_wr_star()` - Draw a Wolf-Rayet star
- `draw_supernova()` - Draw a supernova explosion
- `draw_compact_object()` - Draw a compact object (NS/BH)
- `draw_roche_lobe_overflow()` - Draw a mass transfer system
- `draw_common_envelope()` - Draw a common envelope phase
- `draw_arrow()` - Draw labeled arrows for transitions
- And more...

## Color Scheme

The package includes a predefined color scheme for different stellar phases:

```python
from binary_diagrams import colors

print(colors['zams'])  # ZAMS stars
print(colors['wr'])    # Wolf-Rayet stars
print(colors['black_hole'])  # Black holes
# ... and more
```

## Requirements

- Python >= 3.8
- matplotlib >= 3.5.0
- numpy >= 1.20.0

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
