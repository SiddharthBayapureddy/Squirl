import qrcode # Python QR Code Generator

# Creating an instance

# Function
def qr(url : str):
    qr_gen = qrcode.QRCode(box_size=10, border=4)
    qr_gen.add_data(url)
    qr_gen.make(fit=True)
    img = qr_gen.make_image()
    return img


if __name__ == "__main__":
    image = qr("https://www.youtube.com/@BroCodez") # Testing
    image.save("sample_qr.png")