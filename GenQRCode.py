import pyqrcode
import png
import time

from pyqrcode import QRCode

#banner
print("    🅶🅴🅽 🆀🆁🅲🅾🅳🅴   \n")
time.sleep(1.5)

print("QRCode Generator \n")
time.sleep(1)

#input url
QRstr = str(input("URL: "))
time.sleep(0.6)

print("\nGenerating... \n")
time.sleep(1)

#QRcode + image creating
url= pyqrcode.create(QRstr)
url.png("qr.png", scale=8)

#finishing
time.sleep(1)
print("    _Finish QRCode_  ")

