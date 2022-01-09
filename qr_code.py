# import qr_code
# # String which represent the QR code
# img = qr_code.make("https://www.youtube.com/channel/UCBLxylYz7roM4CiB9munLqw")
# img.save("de.jpg")
import pyqrcode
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "www.geeksforgeeks.org"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)