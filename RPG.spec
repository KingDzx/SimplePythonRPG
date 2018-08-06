# -*- mode: python -*-

block_cipher = None


a = Analysis(['RPG.py'],
             pathex=['C:\\Users\\dzach\\AppData\\Local\\Programs\\Python\\Python37,C:\\Users\\dzach\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\dzach\\Desktop\\Github Folder\\SimplePythonRPG'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='RPG',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )
