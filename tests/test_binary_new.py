#!/usr/bin/env python3
"""
Test script for new binary system types.
Demonstrates all new binary functions from binary.py module.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.components.binary import (
    # Existing
    binary, common_envelope, roche_lobe_overflow, HMS_HMS,
    # New binary types
    HeMS_HMS, WR_HMS, BH_HMS, NS_HMS,
    BBH, BNS, NS_NS, BH_NS,
    WD_WD, WD_HMS, AM_CVn, symbiotic_binary,
    HMXB, LMXB, cataclysmic_variable, CV,
    contact_binary, overcontact_binary,
    detached_binary, semi_detached_binary
)

# Create figure for compact object binaries
fig, ax = setup_canvas(width=14, height=12, xlim=(0, 14), ylim=(0, 12))
ax.set_title('Binary System Types - Compact Object Binaries', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Double compact objects
y1 = 10
BBH(2, y1, size1=0.18, size2=0.15, separation=0.6, label_text='Binary Black Holes (BBH)')
BNS(6, y1, size1=0.12, size2=0.1, separation=0.5, label_text='Binary Neutron Stars (BNS)')
BH_NS(10, y1, size_bh=0.18, size_ns=0.1, separation=0.6, label_text='BH + NS')

# Row 2: Double white dwarfs and WD systems
y2 = 7.5
WD_WD(2, y2, size1=0.12, size2=0.1, separation=0.5, label_text='Double WD')
WD_HMS(5.5, y2, size_wd=0.1, size_star=0.3, separation=0.7, label_text='WD + MS')
AM_CVn(9, y2, size_accretor=0.1, size_donor=0.08, separation=0.5, label_text='AM CVn')
symbiotic_binary(12.5, y2, size_wd=0.1, size_giant=0.45, separation=0.9, label_text='Symbiotic Binary')

# Row 3: Compact object + star
y3 = 5
BH_HMS(2, y3, size_bh=0.15, size_star=0.35, separation=0.8, label_text='BH + MS')
NS_HMS(6, y3, size_ns=0.1, size_star=0.35, separation=0.8, label_text='NS + MS')
HeMS_HMS(10, y3, size_primary=0.25, size_secondary=0.3, separation=0.8, label_text='HeMS + HMS')

# Row 4: X-ray binaries and CVs
y4 = 2.5
HMXB(2, y4, size_co=0.12, size_star=0.4, separation=0.9, co_type='BH', label_text='HMXB')
LMXB(6, y4, size_co=0.1, size_star=0.25, separation=0.7, co_type='NS', label_text='LMXB')
cataclysmic_variable(10, y4, size_wd=0.1, size_donor=0.25, separation=0.6, label_text='Cataclysmic Variable')

plt.tight_layout()
plt.savefig('tests/output_binary_compact.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_binary_compact.png")
plt.close()


# Create figure for stellar binaries and interaction types
fig, ax = setup_canvas(width=14, height=10, xlim=(0, 14), ylim=(0, 10))
ax.set_title('Binary System Types - Stellar Binaries & Configurations', fontsize=16, fontweight='bold', y=1.02)

# Row 1: Different binary configurations
y1 = 8
HMS_HMS(2, y1, size_primary=0.3, size_secondary=0.25, separation=0.8, label_text='HMS + HMS')
WR_HMS(6, y1, size_primary=0.2, size_secondary=0.35, separation=0.8, label_text='WR + HMS')
detached_binary(10, y1, size1=0.3, size2=0.25, separation=1.2, label_text='Detached Binary')

# Row 2: Contact and semi-detached
y2 = 5.5
contact_binary(2.5, y2, size1=0.35, size2=0.3, overlap=0.12, label_text='Contact Binary')
overcontact_binary(7, y2, size=0.5, label_text='Overcontact Binary')
semi_detached_binary(11, y2, size_donor=0.35, size_accretor=0.3, separation=0.9, label_text='Semi-Detached')

# Row 3: Roche lobe overflow and common envelope
y3 = 2.5
roche_lobe_overflow(3, y3, donor_size=0.4, accretor_size=0.3, separation=1.0, label_text='RLO (default)')
common_envelope(9, y3, envelope_size=0.6, primary_size=0.2, secondary_size=0.15, 
                separation=0.5, label_text='Common Envelope')

plt.tight_layout()
plt.savefig('tests/output_binary_stellar.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved: tests/output_binary_stellar.png")
plt.close()

print("\nBinary system types tests completed!")
print("Functions tested:")
print("  - BBH(), BNS(), NS_NS(), BH_NS()")
print("  - WD_WD(), WD_HMS(), AM_CVn(), symbiotic_binary()")
print("  - BH_HMS(), NS_HMS(), HeMS_HMS(), WR_HMS()")
print("  - HMXB(), LMXB(), cataclysmic_variable(), CV()")
print("  - contact_binary(), overcontact_binary()")
print("  - detached_binary(), semi_detached_binary()")
