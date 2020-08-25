import pytesseract
from PIL import Image, ImageDraw, ImageFont


text = '0123456789'

im = Image.new("RGB", (300, 50), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype('mpepc5unpb.woff', 18)
dr.text((10, 5), text, font=font, fill='#000000')
# im.show()
im.save('t.png')
image = Image.open('t.png')

text = pytesseract.image_to_string(image)
print(text)
