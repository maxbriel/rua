"""Binary Diagrams - Tools for creating stellar evolution diagrams.

This package provides tools for visualizing stellar evolution,
particularly for binary systems evolving to Wolf-Rayet phases.
"""

__version__ = "0.1.0"

from .wr_common import (
    draw_star,
    draw_binary,
    draw_zams_star,
    draw_zams_binary,
    draw_wr_star,
    draw_supernova,
    draw_arrow,
    draw_compact_object,
    draw_roche_lobe_overflow,
    draw_common_envelope,
    draw_CO_binary,
    draw_BBH,
    draw_BH,
    draw_BH_binary,
    draw_supernova_image,
    draw_SN_and_CO,
    draw_SN_and_star,
    draw_roche_lobe_overflow_BH,
    colors,
)

from .diagrams import (
    create_binary_diagram,
    create_single_star_diagram,
)

__all__ = [
    "draw_star",
    "draw_binary",
    "draw_zams_star",
    "draw_zams_binary",
    "draw_wr_star",
    "draw_supernova",
    "draw_arrow",
    "draw_compact_object",
    "draw_roche_lobe_overflow",
    "draw_common_envelope",
    "draw_CO_binary",
    "draw_BBH",
    "draw_BH",
    "draw_BH_binary",
    "draw_supernova_image",
    "draw_SN_and_CO",
    "draw_SN_and_star",
    "draw_roche_lobe_overflow_BH",
    "colors",
    "create_binary_diagram",
    "create_single_star_diagram",
]
