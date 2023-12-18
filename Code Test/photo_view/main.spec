# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('whole/best.pt', 'whole/best.pt'), ('icons/placeholder-square.jpg', 'icons/placeholder-square.jpg')],
    hiddenimports=['ultralytics'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Oizoos',
          debug=False,
          bootloader_ignore_signals=False,
          bootloader_additional_files=[],
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)
