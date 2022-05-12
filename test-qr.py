import qrcode
img = qrcode.make("https://cdn.i-scmp.com/sites/default/files/d8/images/canvas/2021/10/30/85f2cb5f-44f8-4f2f-a813-63e657e11acc_5065cac7.jpg")
img.save("qr-file.png")
