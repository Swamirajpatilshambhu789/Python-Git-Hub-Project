import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data_to_encode = "https://www.youtube.com/"  # Replace this with your data

    output_filename = "generated_qr_code.png"  # Replace this with your desired filename

    generate_qr_code(data_to_encode, output_filename)
    print(f"A QR code has been generated and saved as '{output_filename}'")
