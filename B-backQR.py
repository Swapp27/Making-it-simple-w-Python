>>> import pyqrcode
>>> import png
>>> from pyqrcode import QRCode
>>> link = "https://github.com/Swapp27"
>>> my_QR = pyqrcode.create(link)
>>> my_QR.svg("MyGit.svg", scale = 8)
>>> my_QR.png("MyGit.png", scale = 10)