"""
Rua - Tools for creating stellar evolution diagrams for binary systems.

A comprehensive library for visualizing stellar evolution, binary interactions,
and multi-star systems.

Modules:
    canvas: Canvas setup for diagrams
    grid: Grid system for organizing stellar objects
    components.stellar: Single stellar objects and phases
    components.compact: Compact objects (NS, BH, WD)
    components.binary: Binary star systems
    components.outcomes: Binary evolution outcomes
    components.multiples: Multi-star systems
    components.environment: Environment and structure components
    utils.colors: Color definitions for stellar types
"""

from rua.canvas import setup_canvas
from rua.grid import Grid
from rua.utils.colors import colors

__version__ = "0.2.0"

__all__ = ['setup_canvas', 'Grid', 'colors']
