"""
Color definitions for various stellar evolution stages.
"""

colors = {
    # Main Sequence Stars
    'ZAMS': '#ffd3ac',  # light orange
    'lower_mass_ZAMS': '#c97889',  # light pink
    'HMS': '#ffd3ac',  # hydrogen main sequence (same as ZAMS)
    'HeMS': '#87CEEB',  # helium main sequence (sky blue)
    
    # Giant Branch Stars
    'RGB': '#FF6347',  # tomato red (Red Giant Branch)
    'AGB': '#D64545',  # deeper red (Asymptotic Giant Branch)
    'HB': '#FFD700',  # gold (Horizontal Branch)
    'HG': '#FFA07A',  # light salmon (Hertzsprung Gap)
    
    # Supergiants
    'RSG': "#F34545",  # orange-red (Red Supergiant)
    'BSG': "#5579E7",  # royal blue (Blue Supergiant)
    'YSG': "#CBB224",  # gold (Yellow Supergiant)
    
    # Stripped/Evolved Stars
    'He_star': '#87CEEB',  # sky blue (Helium star)
    'Stripped': '#B0C4DE',  # light steel blue (Stripped envelope)
    'WR': '#C3D0D8',    # light gray-blue (Wolf-Rayet)
    
    # Compact Objects
    'WD': '#FFFFFF',  # white (White Dwarf)
    'NS_outer': '#B0E0E6',  # powder blue
    'NS_middle': '#D4EFF5',  # very light blue
    'NS_inner': '#F0F8FF',  # alice blue
    'BH': '#3E3E3E',  # dark gray
    
    # Envelopes and Extended Structures
    'Envelope': '#95ACBF',  # gray-blue
    'CE': '#95ACBF',  # common envelope (same as Envelope)
    'planetary_nebula': '#98FB98',  # pale green
    'planetary_nebula_outer': '#90EE90',  # light green
    
    # Explosions and Transients
    'Supernova': '#FFA500',  # orange
    'nova': '#FFE4B5',  # moccasin (classical nova)
    'kilonova': '#DA70D6',  # orchid
    'type_ia': '#FF4500',  # orange-red
    'pair_instability': '#FF0000',  # red
    'failed_sn': '#696969',  # dim gray
    
    # Exotic Objects
    'TZO': '#CD5C5C',  # indian red (Thorne-Żytkow Object)
    'TZO_core': '#B0E0E6',  # powder blue (NS core inside)
    'merger_product': '#FF69B4',  # hot pink
    
    # Binary Interaction Features
    'contact': '#FF8C00',  # dark orange (contact binaries)
    'stream': '#ADD8E6',  # light blue (mass transfer stream)
    'disk': '#DDA0DD',  # plum (accretion disk)
    'disk_inner': '#EE82EE',  # violet
    'jet': '#9400D3',  # dark violet
    'wind': '#E6E6FA',  # lavender
    
    # X-ray Binaries
    'HMXB_star': '#FF6B6B',  # coral red
    'LMXB_star': '#FFB347',  # pastel orange
    
    # Multi-star Systems
    'tertiary': '#9370DB',  # medium purple
    'quaternary': '#20B2AA',  # light sea green
    
    # Environment
    'circumbinary': '#DEB887',  # burlywood
    'magnetosphere': '#4169E1',  # royal blue
    'pulsar_wind': '#00CED1',  # dark turquoise
    
    # Gravitational Waves
    'gw_wave': '#7B68EE',  # medium slate blue
}


