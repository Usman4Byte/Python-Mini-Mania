import qrcode
import os
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
script_dir = os.path.dirname(os.path.abspath(__file__))

qr.add_data('https://github.com/usman4byte')
img = qr.make_image(fill_color="green", back_color="gray")
img.save(os.path.join(script_dir, 'github_qr2.png'))