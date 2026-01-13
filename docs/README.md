# Rua Documentation

This directory contains the Sphinx documentation for Rua.

## Building the Documentation

### Install Dependencies

```bash
pip install -e ".[docs]"
```

Or:

```bash
pip install -r docs/requirements.txt
```

### Build HTML

```bash
cd docs
make html
```

The built documentation will be in `docs/_build/html/`. Open `docs/_build/html/index.html` in your browser.

### Clean Build

```bash
cd docs
make clean
```

## Documentation Structure

- `index.rst` - Main documentation entry point
- `installation.rst` - Installation instructions
- `quickstart.rst` - Quick start guide
- `building.rst` - Documentation building guide
- `api/` - API reference documentation (auto-generated from docstrings)
  - `index.rst` - API overview
  - `stellar.rst` - Stellar components API
  - `binary.rst` - Binary systems API
  - `compact.rst` - Compact objects API
  - `utils.rst` - Utilities API
- `conf.py` - Sphinx configuration
- `_static/` - Static files (CSS, images, etc.)
- `_templates/` - Custom templates
