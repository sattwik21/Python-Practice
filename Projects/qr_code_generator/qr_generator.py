import pyqrcode
from pyqrcode import QRCode


# String which represent the qr code
input_ = str(input("Enter the link you want to convert: "))

# Generate qrcode
url = pyqrcode.create(input_)

# Create and Save as SVG
url.svg("myqr.svg", scale = 8)