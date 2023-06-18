# Import QRCode from pyqrcode

import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code

s = "https://github.com/Gokul-Raja84"

# Generate QR code

url = pyqrcode.create(s)

# Create and save the svg file name " " / Change it the way you want
url.svg("mygit.svg", scale = 8)

# Create and save the png file name " .png"

url.png('mygit.png', scale = 6)
