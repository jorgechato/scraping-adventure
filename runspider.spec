# -*- mode: python -*-
a = Analysis(['runspider.py'],
             pathex=['/Users/Orggue/Github/comorebajarlabarriga'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='runspider',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='icon.png')
app = BUNDLE(exe,
             name='runspider.app',
             icon='icon.png')
