'''

QR Code Generation in Python
'''

#Import the module

import pyqrcode

#Enter the  data/website that you need QR Code for

data = 'https://github.com/Gokul-Raja84'

#create qrcode

img = pyqrcode.create(data)

#save the qrcode in png format with proper scaling

img.png('Github.png', scale= 10) #You can change the image file name to be saved as you like