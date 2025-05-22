from PIL import Image, ImageFont, ImageDraw
import glob
import os

images = glob.glob('../images/*.[Jj][Pp][Gg]')

for idx, image in enumerate(images):

    img = Image.open(image).convert('RGBA')

    w,h = img.size

    text = Image.new(mode='RGBA', size=img.size, color=(255,0,0,0))

    font = ImageFont.truetype('../font/Anton-Regular.ttf', 200)

    draw = ImageDraw.Draw(text)

    l,t,r,b = draw.textbbox((0,0), text='HELLO', font=font)

    draw.text((w-r-50, h-b-50),'HELLO', font=font, fill=(255,255,255,255))

    result = Image.alpha_composite(img, text)

    os.makedirs('images', exist_ok=True)

    result.convert('RGB').save(f'images/result-{idx + 1}.jpg')
