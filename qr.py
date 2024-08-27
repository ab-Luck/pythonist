import qrcode

# Data to be encoded
data = "wishal Bhai"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image object
img = qr.make_image(fill='black', back_color='white')

# Save the QR code as an image file
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
