import qrcode

url = input("Enter the URL: ")
file_path = "C:/Users/prath/OneDrive/Desktop/qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated! ")