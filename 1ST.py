import qrcode

def generate_qr_code(data, file_name='qrcode.png'):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)

if __name__ == "__main__":
    # Example usage
    data_to_encode = "https://github.com/"
    generate_qr_code(data_to_encode)
