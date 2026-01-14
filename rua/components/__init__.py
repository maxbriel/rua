"""
Rua components for drawing stellar evolution diagrams.

Available modules:
- stellar: Single stellar objects and phases
- compact: Compact objects (NS, BH, WD)
- binary: Binary star systems
- outcomes: Binary evolution outcomes (mergers, kicks, etc.)
- multiples: Multi-star systems (triples, clusters)
- environment: Environment and structure components
- decorator: Labels and arrows
"""

from rua.components import stellar
from rua.components import compact
from rua.components import binary
from rua.components import outcomes
from rua.components import multiples
from rua.components import environment
from rua.components import decorator

__all__ = [
    'stellar',
    'compact', 
    'binary',
    'outcomes',
    'multiples',
    'environment',
    'decorator'
]
