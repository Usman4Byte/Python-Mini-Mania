import qrcode as qr
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
img = qr.make('https://github.com/usman4byte')
img.save(os.path.join(script_dir, 'github_qr.png'))