#!/usr/bin/env python3
"""
Diagram creation functions for stellar evolution.

This module provides high-level functions to create complete diagrams
for single star and binary star evolution to Wolf-Rayet phases.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from .wr_common import (
    draw_BBH, draw_BH, draw_BH_binary, draw_star, draw_binary,
    draw_arrow, draw_supernova_image, draw_zams_binary, draw_wr_star,
    draw_common_envelope, draw_compact_object, draw_roche_lobe_overflow, colors,
    draw_CO_binary, draw_SN_and_CO, draw_SN_and_star, draw_roche_lobe_overflow_BH,
    draw_zams_star, draw_supernova
)


def create_binary_diagram():
    """Create diagram for binary star evolution to WR phase
    
    Returns:
        matplotlib.figure.Figure: The created figure
    """
    width = 3.38*2  # inches for single column
    height = 12  # inches
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    ax.set_aspect('equal')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Title
    ax.text(width/2, 11.95, 'Binary Star Evolution to Wolf-Rayet Phase', 
            ha='center', va='top', fontsize=16, fontweight='bold')
    
    # Starting point - Binary ZAMS
    y_start = 11
    draw_zams_binary(ax, 1.3, y_start, size1=0.3, size2=0.25, separation=0.7, 
                     label_text='Binary ZAMS')
    
    # DECISION POINT 1
    y_wide = 8
    # non-interacting
    draw_arrow(ax, 1.3, y_start-0.7, 1.3, y_wide+0.3,
               label='Wide\nNon-interacting\nEffectively Single',
               label_position='left')
    
    # WR + MS star
    draw_binary(ax, 1.3, y_wide, size1=0.15, size2=0.25, separation=0.7, 
                colors=(colors['wr'], colors['lower_mass_zams']), label='WR + MS/evolved\ncompanion')

    # interacting
    draw_arrow(ax, 2.0, y_start, 3.0, y_start, label='Close\ninteracting', label_position='top')
    draw_roche_lobe_overflow(ax, 3.8, y_start, donor_size=0.38, accretor_size=0.25, separation=0.8,
                            donor_color= '#ffd3ac',
                            accretor_color='#c97889', 
                            label_text='Roche Lobe Overflow')

    # Stable arrow
    draw_arrow(ax, 3.2, y_start - 0.7, 1.9, y_wide+0.3, label='Stable', label_position='left')
    
    # unstable arrow
    draw_arrow(ax, 4, y_start - 0.7, 4, y_wide+0.4, label='Unstable', label_position='left')
    
    # CE image
    draw_common_envelope(ax, 4, y_wide, envelope_size=0.5, star_sizes=(0.15, 0.15),
                        label_text='Common Envelope')
    
    # CE outcomes
    # 1. arrow to WR + MS/evolved companion
    draw_arrow(ax, 3.4, y_wide, 2.05, y_wide, label='Spiral-in\neject CE', label_position='top')
    
    # 2. Merger
    draw_arrow(ax, 4.6, y_wide, 5.5, y_wide, label='Merger', label_position='top')
    
    # Draw rectangle with rounded corners for single star evolution
    single_star_evolution_color = "#f4f4f4"
    single_star_edge_color = "#848484"
    
    draw_rectangle = FancyBboxPatch((5.4, y_wide - 3.3),
                                    1,
                                    4.05,
                                    boxstyle="round,pad=0.05",
                                    linewidth=1,
                                    edgecolor=single_star_edge_color,
                                    facecolor=single_star_evolution_color,
                                    zorder=-10,
                                    linestyle='--')
    ax.add_patch(draw_rectangle)
    # single star evolution inside rectangle
    draw_star(ax, 5.9, y_wide, size=0.35, color=colors['zams'], edgecolor='darkred')
    ax.text(5.9, y_wide+0.4, 'Single star\nevolution', ha='center', va='bottom', fontweight='bold')
    
    # arrow from single star evolution to WR
    draw_arrow(ax, 5.9, y_wide - 0.4, 5.9, y_wide - 0.9, label='', label_position='right')
    # WR star
    draw_wr_star(ax, 5.9, y_wide - 1.2, size=0.25, label_text='', label_position='bottom')
    # arrow WR star to SN
    draw_arrow(ax, 5.9, y_wide - 1.5, 5.9, y_wide - 2.0, label_position='right')
    # SN
    draw_supernova_image(ax, 5.9, y_wide - 2.2, size=0.4, image_path='supernova.png')
    # draw BH
    draw_arrow(ax, 5.9, y_wide - 2.4, 5.9, y_wide - 2.75, label_position='right')
    draw_BH(ax, 5.9, y_wide - 2.9, size=0.15)
    ax.text(5.9, y_wide - 3.25, 'BH', ha='center', fontweight='bold')
    
    y_SN = y_wide - 1.8
    
    # arrow to SN
    draw_arrow(ax, 1.3, y_wide - 0.8, 1.3, y_SN+0.3, label='Late burning stages', label_position='right')

    # WR+MS/evolved companion to SN
    draw_SN_and_star(ax,
                     1.3,
                     y_SN,
                     size_sn=0.5,
                     size_star=0.25,
                     separation=0.6,
                     star_color=colors['lower_mass_zams'])
    ax.text(1.3, y_SN - 0.5, 'Supernova 1', ha='center', fontweight='bold')
    
    # arrow unbound system after SN
    draw_arrow(ax, 1.3+0.6, y_SN, 5.48, y_wide-0.25, label='Unbound system', label_position='bottom')
    
    y_star_BH = y_SN - 1.5
    
    # Non-interacting path to WR+BH binary
    draw_arrow(ax, 1.3, y_SN-0.6, 1.3, y_star_BH+0.3, label='Bound system', label_position='right')
    draw_BH_binary(ax, 1.3, y_star_BH,
                   size_bh=0.15,
                   size_star=0.25,
                   separation=0.6,
                   star_color=colors['lower_mass_zams'])
    
    y_WR_BH = y_star_BH - 2
    
    # arrow to WR+BH
    draw_arrow(ax, 1.3, y_star_BH - 0.8, 1.3, y_WR_BH+0.2,
               label='Wide\nNon-interacting\nEffectively Single', label_position='left')
    draw_BH_binary(ax, 1.3, y_WR_BH, 
                   size_bh=0.15,
                   size_star=0.2,
                   separation=0.6,
                   star_color=colors['wr'],
                   label_text='BH + WR')
    
    # interacting path RLO BH
    draw_arrow(ax, 2.0, y_star_BH, 3.0, y_star_BH, label='Close\ninteracting', label_position='top')
    draw_roche_lobe_overflow_BH(ax, 3.8, y_star_BH, donor_size=0.3, accretor_size=0.15, separation=0.6,
                            donor_color= colors['lower_mass_zams'],
                            accretor_color='#888888', 
                            label_text='Roche Lobe Overflow')
    
    # arrow to WR+BH from RLOF BH
    draw_arrow(ax, 3.2, y_star_BH - 0.7, 1.9, y_WR_BH+0.2, label='Stable', label_position='left')
    
    # arrow from RLO to unstable CE
    draw_arrow(ax, 4, y_star_BH - 0.7, 4, y_WR_BH+0.4, label='Unstable', label_position='left')
    
    # unstable CE image
    draw_common_envelope(ax, 4, y_WR_BH, envelope_size=0.5, star_sizes=(0.15, 0.15),
                         colors=(colors['zams'], colors['black_hole'], colors['wr']),
                         label_text='Common Envelope')
    
    # From CE to WR+BH
    draw_arrow(ax, 3.4, y_WR_BH, 2.05, y_WR_BH, label='Spiral-in\neject CE', label_position='top')
    
    # Failed CE
    draw_arrow(ax, 4.6, y_WR_BH, 5.5, y_WR_BH, label='Merger', label_position='top')
    draw_star(ax, 5.9, y_WR_BH, size=0.2, color='lightgray', edgecolor='grey',hatch='ooo')
    ax.text(5.9, y_WR_BH+0.4, 'TZO', ha='center', va='bottom', fontweight='bold')
    
    # BH+WR to SN
    y_final_SN = y_WR_BH - 1.1
    draw_arrow(ax, 1.3, y_WR_BH - 0.6, 1.3, y_final_SN+0.2, label='Late burning stages', label_position='right')
    draw_SN_and_CO(ax,
                   1.3,
                   y_final_SN,
                   size_sn=0.5,
                   size_compact=0.15,
                   separation=0.6,
                   flip=False, 
                   co_type='BH')
    ax.text(1.3, y_final_SN - 0.4, 'Supernova 2', ha='center', fontweight='bold')
    
    # final arrow to double compact
    draw_arrow(ax, 1.3, y_final_SN-0.4, 1.3, y_final_SN-0.9, label='Bound system', label_position='right')
    
    draw_BBH(ax, 1.3, y_final_SN-1,
                size_compact1=0.15,
                size_compact2=0.15,
                separation=0.5,
                label_text='BH + BH')
    
    # Draw boxes around WR phases
    wr_box1 = FancyBboxPatch((0.6, y_wide - 0.8),
                             1.4,
                             1.2,
                             boxstyle="round,pad=0.1",
                             linewidth=1,
                             edgecolor='darkorange',
                             facecolor='none',
                             zorder=-5,
                             linestyle='--')
    ax.add_patch(wr_box1)
    
    wr_box2 = FancyBboxPatch((5.0, y_wide - 1.5),
                             1.6,
                             0.6,
                             boxstyle="round,pad=0.1",
                             linewidth=1,
                             edgecolor='darkorange',
                             facecolor='none',
                             zorder=-5,
                             linestyle='--')
    ax.add_patch(wr_box2)

    wr_box3 = FancyBboxPatch((0.6, y_WR_BH - 0.45),
                             1.4,
                             0.7,
                             boxstyle="round,pad=0.1",
                             linewidth=1,
                             edgecolor='darkorange',
                             facecolor='none',
                             zorder=-5,
                             linestyle='--')
    ax.add_patch(wr_box3)

    return fig


def create_single_star_diagram():
    """Create diagram for single star evolution to WR phase
    
    Returns:
        matplotlib.figure.Figure: The created figure
    """
    width = 3.38  # inches for single column
    height = 7  # inches
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    ax.set_aspect('equal')
    
    # remove additional whitespace
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # Title
    ax.text(1.69, 6.95, 'Single Star WR phase', 
            ha='center',va='top', fontsize=15, fontweight='bold')
    
    # ZAMS at top
    draw_zams_star(ax, 1.0, 5.8, size=0.6, label_text='ZAMS\n(Main Sequence)', label_position='right')
    
    # Arrow to WR
    draw_arrow(ax, 1.0, 5.15, 1.0, 4.2, label='Stellar wind mass loss', width=2.5)
    
    # WR phase in middle
    draw_wr_star(ax, 1., 3.7, size=0.45, label_text='WR Phase\n(He-burning)')
    
    # Arrow to SN
    draw_arrow(ax, 1.0, 3.2, 1.0, 2.5, label='Late burning stages', width=2.5)
    
    # Supernova explosion at bottom (using PNG image)
    draw_supernova(ax, 1.0, 2.1, size=1, label_text='Supernova', 
                   image_path='supernova.png')
    
    draw_arrow(ax, 1.0, 1.6, 1.0, 0.8, label='Remnant formation', width=2.5)
    
    draw_compact_object(ax, 1.0, 0.5, size=0.2, label_text='NS / BH')
    
    return fig
