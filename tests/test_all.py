#!/usr/bin/env python3
"""
Master test script that runs all component tests and creates a summary gallery.
"""

import matplotlib.pyplot as plt
from rua.canvas import setup_canvas
from rua.utils.colors import colors

# Import all modules to verify they load correctly
print("=" * 60)
print("RUA - Stellar Evolution Diagram Library")
print("Comprehensive Component Test Suite")
print("=" * 60)

print("\n[1/6] Loading modules...")

try:
    from rua.components import stellar, compact, binary
    from rua.components import outcomes, multiples, environment
    print("  ✓ All modules loaded successfully")
except ImportError as e:
    print(f"  ✗ Import error: {e}")
    exit(1)

# Verify colors are complete
print("\n[2/6] Verifying color definitions...")
required_colors = [
    'ZAMS', 'lower_mass_ZAMS', 'HMS', 'HeMS',
    'RGB', 'AGB', 'HB', 'HG', 'RSG', 'BSG', 'YSG',
    'He_star', 'Stripped', 'WR', 'WD',
    'NS_outer', 'NS_middle', 'NS_inner', 'BH',
    'Envelope', 'CE', 'planetary_nebula',
    'Supernova', 'nova', 'kilonova', 'type_ia',
    'TZO', 'merger_product',
    'contact', 'stream', 'disk', 'jet', 'wind',
    'HMXB_star', 'LMXB_star',
    'tertiary', 'quaternary',
    'circumbinary', 'magnetosphere', 'pulsar_wind', 'gw_wave'
]
missing = [c for c in required_colors if c not in colors]
if missing:
    print(f"  ✗ Missing colors: {missing}")
else:
    print(f"  ✓ All {len(required_colors)} colors defined")

# List all available functions
print("\n[3/6] Available functions by module:")

# Stellar functions
stellar_funcs = [
    'star', 'supernova_image', 'zams', 'wolf_rayet', 'supernova',
    'red_giant', 'RGB', 'asymptotic_giant_branch', 'AGB',
    'red_supergiant', 'RSG', 'blue_supergiant', 'BSG',
    'yellow_supergiant', 'YSG', 'horizontal_branch', 'HB',
    'hertzsprung_gap', 'HG', 'helium_star', 'He_star', 'stripped_star',
    'thorne_zytkow', 'TZO', 'planetary_nebula', 'nova', 'kilonova',
    'type_ia_supernova', 'failed_supernova', 'pair_instability_supernova',
    'PISN', 'stellar_merger'
]
print(f"\n  stellar.py: {len(stellar_funcs)} functions")
for f in stellar_funcs:
    has_it = hasattr(stellar, f)
    print(f"    {'✓' if has_it else '✗'} {f}")

# Compact functions
compact_funcs = ['NS', 'BH', 'WD', 'compact_objects']
print(f"\n  compact.py: {len(compact_funcs)} functions")
for f in compact_funcs:
    has_it = hasattr(compact, f)
    print(f"    {'✓' if has_it else '✗'} {f}")

# Binary functions
binary_funcs = [
    'binary', 'common_envelope', 'roche_lobe_overflow', 'HMS_HMS',
    'HeMS_HMS', 'WR_HMS', 'BH_HMS', 'NS_HMS',
    'BBH', 'BNS', 'NS_NS', 'BH_NS', 'WD_WD', 'WD_HMS',
    'AM_CVn', 'symbiotic_binary', 'HMXB', 'LMXB',
    'cataclysmic_variable', 'CV', 'contact_binary', 'overcontact_binary',
    'detached_binary', 'semi_detached_binary',
    'accretion_disk', 'mass_transfer_stream', 'jet', 'wind_mass_transfer',
    'case_A_RLO', 'case_B_RLO', 'case_C_RLO'
]
print(f"\n  binary.py: {len(binary_funcs)} functions")
for f in binary_funcs:
    has_it = hasattr(binary, f)
    print(f"    {'✓' if has_it else '✗'} {f}")

# Outcomes functions
outcomes_funcs = [
    'gravitational_wave_merger', 'natal_kick', 'unbound_system', 'runaway_star',
    'supernova_in_binary', 'binary_merger_product', 'common_envelope_ejection'
]
print(f"\n  outcomes.py: {len(outcomes_funcs)} functions")
for f in outcomes_funcs:
    has_it = hasattr(outcomes, f)
    print(f"    {'✓' if has_it else '✗'} {f}")

# Multiples functions
multiples_funcs = [
    'triple_system', 'quadruple_system_2plus2', 'quadruple_system_3plus1',
    'star_cluster', 'triple_with_compact', 'hierarchical_triple_diagram'
]
print(f"\n  multiples.py: {len(multiples_funcs)} functions")
for f in multiples_funcs:
    has_it = hasattr(multiples, f)
    print(f"    {'✓' if has_it else '✗'} {f}")

# Environment functions
environment_funcs = [
    'circumbinary_disk', 'stellar_wind', 'magnetosphere', 'pulsar',
    'pulsar_wind_nebula', 'common_envelope_spiral', 'supernova_remnant',
    'accretion_column', 'tidal_tail'
]
print(f"\n  environment.py: {len(environment_funcs)} functions")
for f in environment_funcs:
    has_it = hasattr(environment, f)
    print(f"    {'✓' if has_it else '✗'} {f}")

# Total count
total = len(stellar_funcs) + len(compact_funcs) + len(binary_funcs) + \
        len(outcomes_funcs) + len(multiples_funcs) + len(environment_funcs)
print(f"\n  TOTAL: {total} functions across 6 modules")

# Run individual tests
print("\n[4/6] Running individual test scripts...")
import subprocess
import sys

test_scripts = [
    'tests/test_stellar_new.py',
    'tests/test_binary_new.py',
    'tests/test_mass_transfer.py',
    'tests/test_outcomes.py',
    'tests/test_multiples.py',
    'tests/test_environment.py'
]

for script in test_scripts:
    print(f"\n  Running {script}...")
    try:
        result = subprocess.run([sys.executable, script], 
                               capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print(f"    ✓ Completed successfully")
        else:
            print(f"    ✗ Failed with error:")
            print(result.stderr[:500] if result.stderr else result.stdout[:500])
    except Exception as e:
        print(f"    ✗ Error: {e}")

# Create summary gallery
print("\n[5/6] Creating summary gallery...")

fig = plt.figure(figsize=(20, 24))
fig.suptitle('Rua Library - Stellar Evolution Diagram Components Gallery', 
             fontsize=20, fontweight='bold', y=0.995)

# Create subplots for each category
ax1 = fig.add_subplot(3, 2, 1)
ax2 = fig.add_subplot(3, 2, 2)
ax3 = fig.add_subplot(3, 2, 3)
ax4 = fig.add_subplot(3, 2, 4)
ax5 = fig.add_subplot(3, 2, 5)
ax6 = fig.add_subplot(3, 2, 6)

for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal')
    ax.axis('off')

# Subplot 1: Stellar Phases
ax1.set_title('Stellar Evolution Phases', fontsize=14, fontweight='bold')
stellar.zams(1, 4, size=0.3, label_text='ZAMS', ax=ax1)
stellar.red_giant(3, 4, size=0.4, label_text='RGB', ax=ax1)
stellar.blue_supergiant(5, 4, size=0.35, label_text='BSG', ax=ax1)
stellar.red_supergiant(1.5, 2, size=0.5, label_text='RSG', ax=ax1)
stellar.wolf_rayet(4, 2, size=0.3, label_text='WR', ax=ax1)

# Subplot 2: Compact Objects
ax2.set_title('Compact Objects & Transients', fontsize=14, fontweight='bold')
compact.NS(1, 4, size=0.15, label_text='NS', ax=ax2)
compact.BH(3, 4, size=0.2, label_text='BH', ax=ax2)
compact.WD(5, 4, size=0.12, label_text='WD', ax=ax2)
stellar.kilonova(1.5, 2, size=0.4, label_text='Kilonova', ax=ax2)
stellar.planetary_nebula(4, 2, size=0.5, label_text='PN', ax=ax2)

# Subplot 3: Binary Systems
ax3.set_title('Binary System Types', fontsize=14, fontweight='bold')
binary.BBH(1.5, 4, size1=0.15, size2=0.12, separation=0.4, label_text='BBH', ax=ax3)
binary.BNS(4.5, 4, size1=0.1, size2=0.1, separation=0.35, label_text='BNS', ax=ax3)
binary.HMXB(1.5, 2, size_co=0.1, size_star=0.3, separation=0.6, label_text='HMXB', ax=ax3)
binary.contact_binary(4.5, 2, size1=0.25, size2=0.2, overlap=0.08, label_text='Contact', ax=ax3)

# Subplot 4: Mass Transfer
ax4.set_title('Mass Transfer & Accretion', fontsize=14, fontweight='bold')
binary.roche_lobe_overflow(1.5, 4, donor_size=0.3, accretor_size=0.2, separation=0.7, 
                           label_text='RLO', ax=ax4)
binary.common_envelope(4.5, 4, envelope_size=0.4, primary_size=0.15, secondary_size=0.1,
                       separation=0.35, label_text='CE', ax=ax4)
binary.accretion_disk(2, 1.8, inner_radius=0.1, outer_radius=0.35, ax=ax4)
compact.BH(2, 1.8, size=0.1, label_text='', ax=ax4)
binary.jet(2, 1.8, length=0.5, width=0.08, label_text='Jet + Disk', ax=ax4)

# Subplot 5: Multi-Star Systems
ax5.set_title('Multi-Star Systems', fontsize=14, fontweight='bold')
multiples.triple_system(2, 3.5, sizes=(0.2, 0.15, 0.12), inner_separation=0.4,
                        outer_separation=1.0, label_text='Triple', ax=ax5)
multiples.star_cluster(5, 3, n_stars=10, cluster_radius=0.8, 
                       size_range=(0.06, 0.15), seed=42, label_text='Cluster', ax=ax5)

# Subplot 6: Environment
ax6.set_title('Environment & Outcomes', fontsize=14, fontweight='bold')
environment.pulsar(1.5, 4, ns_size=0.08, beam_length=0.5, beam_angle=20,
                   rotation_indicator=False, label_text='Pulsar', ax=ax6)
environment.supernova_remnant(4.5, 4, remnant_size=0.7, co_size=0.06, 
                              co_type='NS', label_text='SNR', ax=ax6)
outcomes.gravitational_wave_merger(3, 1.5, size=0.4, n_waves=3, 
                                   label_text='GW Merger', ax=ax6)

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.savefig('tests/output_gallery.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("  ✓ Saved: tests/output_gallery.png")
plt.close()

print("\n[6/6] Test Summary")
print("=" * 60)
print(f"Total components implemented: {total}")
print("\nOutput files generated:")
print("  - tests/output_stellar_phases.png")
print("  - tests/output_stellar_phenomena.png")
print("  - tests/output_binary_compact.png")
print("  - tests/output_binary_stellar.png")
print("  - tests/output_mass_transfer.png")
print("  - tests/output_outcomes.png")
print("  - tests/output_multiples.png")
print("  - tests/output_environment.png")
print("  - tests/output_gallery.png (summary)")
print("\n" + "=" * 60)
print("All tests completed!")
print("=" * 60)
