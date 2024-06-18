import qrcode as qr
from PIL import Image
img = qr.make("hello, i am aparna anand")
img.save("qr_code_generated.png")

# qr=qrcode.QRCode(version=1,
#              error_correction=qrcode.constants.ERROR_CORRECT_H,
#              box_size=10,
#              border=4)
 
# qr.add_data("https://web.whatsapp.com/")
# qr.make(fit=True)
# img=qr.make_image(fill_color="Blue",
#                   back_color="pink")
# img.save("qr_code_whatsapp.png")