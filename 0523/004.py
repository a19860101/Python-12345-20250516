from PIL import Image, ImageDraw, ImageFont
import os
import glob

images = glob.glob('./images/*')

date_offset = 15
font_size = 40
color = 'red'

for idx, image in enumerate(images):

    img = Image.open(image)

    exif = img._getexif()

    if 36867 in exif.keys():
        date = exif[36867]
    else:
        # date = '00/00/00 00:00:00'
        date = ''
    draw = ImageDraw.Draw(img)

    l,t,r,b = draw.textbbox((0,0), text=date, font_size=font_size)

    w,h = img.size

    font = ImageFont.truetype('../font/Anton-Regular.ttf', font_size)

    draw.text((w - r - date_offset, h - b - date_offset), text=date, font_size=font_size, fill=color)

    os.makedirs('output',exist_ok=True)

    img.save(f'output/img-{idx}.jpg')
