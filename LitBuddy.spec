# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files

# Collect audio files and config files
datas = [
    ('admin_config.json', '.'),
    ('difficulty_config.json', '.'),
    ('litbuddy_config.json', '.'),
    ('syllables.json', '.'),
    ('wordlists/main_wordlist_game_ready.json', 'wordlists'),
    ('profiles/litbuddy.json', 'profiles'),
    ('config/config.json', 'config'),
    ('config/phonics_audio_map.json', 'config'),
]

# Include all files from audio/_phonograms2
for root, dirs, files in os.walk('audio/_phonograms2'):
    for file in files:
        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, '.')
        datas.append((full_path, os.path.dirname(rel_path)))

block_cipher = None

a = Analysis(
    ['LitBuddy.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='LitBuddy',
    debug=False,
    strip=False,
    upx=True,
    console=False,  # Set to True if you want a terminal window
)
