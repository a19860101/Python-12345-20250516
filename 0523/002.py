from PIL import Image, ImageDraw, ImageFont

img = Image.open('./images/IMG_8439.JPEG')

exif = img._getexif()
date = exif[36867]
model = exif[316]
print(exif)

draw = ImageDraw.Draw(img)

text = f'{date} shot by {model}'

font = ImageFont.truetype('../font/Anton-Regular.ttf', 60)

# draw.text((0,0), text=text, font_size=60, fill='red')
draw.text((0,0), text=text, font=font, fill='red')

img.save('a.jpg')