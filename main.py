import qrcode
import sys

def generate_qr(user_input, filename=None):
    if filename is None:
        filename = 'qr_code.jpg'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_input)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

    print(f"QR code generated and saved as {filename}")

def main():
    if len(sys.argv) > 1:
        user_input = ' '.join(sys.argv[1:])
    else:
        user_input = input("Please enter the text, URL, or any string: ")

    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = None

    generate_qr(user_input, filename)

if __name__ == "__main__":
    main()
