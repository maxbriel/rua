Installation
============

From Source
-----------

To install Rua from source::

    git clone https://github.com/maxbriel/rua.git
    cd rua
    pip install -e .

Requirements
------------

Rua requires:

- Python >= 3.8
- matplotlib >= 3.5.0
- numpy >= 1.20.0

Development Installation
------------------------

For development, install with the optional development dependencies::

    pip install -e ".[dev]"

This will install additional tools for testing and code formatting:

- pytest >= 7.0
- black >= 22.0
- flake8 >= 4.0
