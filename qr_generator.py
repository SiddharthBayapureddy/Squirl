import qrcode # Python QR Code Generator

# Creating an instance
qr_gen = qrcode.QRCode()

# Function
def qr(url : str):
    qr_gen.add_data(url)
    img = qr_gen.make_image()
    return img


if __name__ == "__main__":
    image = qr("https://www.youtube.com/@BroCodez") # Testing
    image.save("sample_qr.png")