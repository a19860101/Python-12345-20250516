from PIL import Image, ImageDraw, ImageFont

img = Image.open('./images/IMG_8439.JPEG')

date_offset = 15
font_size = 40
color = 'red'

exif = img._getexif()
date = exif[36867]

draw = ImageDraw.Draw(img)

l,t,r,b = draw.textbbox((0,0), text=date, font_size=font_size)

w,h = img.size

font = ImageFont.truetype('../font/Anton-Regular.ttf', font_size)

draw.text((w - r - date_offset, h - b - date_offset), text=date, font_size=font_size, fill=color)

img.save('a.jpg')
