import qrcode
from backend.app.utils import generate_short_code

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(generate_short_code())
qr.make(fit=True)

# image generation
img = qr.make_image(fill="black", back_color="white")
