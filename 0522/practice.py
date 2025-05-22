from PIL import Image, ImageFont, ImageDraw
import glob
import os

images = glob.glob('../images/*.[Jj][Pp][Gg]')

qu = int(input('請輸入壓縮品質(0-100):'))
resize_w = int(input('請輸入縮圖寬度:'))
watermark = input('請輸入浮水印文字:')
size = int(input('請輸入文字大小:'))
o = int(input('請輸入文字透明度(0-255):'))
x = int(input('請輸入x軸偏移:'))
y = int(input('請輸入y軸偏移:'))

for idx, image in enumerate(images):

    img = Image.open(image).convert('RGBA')

    w,h = img.size

    resize_h = int(h * resize_w / w)

    img = img.resize((resize_w,resize_h))

    text = Image.new(mode='RGBA', size=img.size, color=(255,0,0,0))

    font = ImageFont.truetype('../font/Anton-Regular.ttf', size)

    draw = ImageDraw.Draw(text)

    l,t,r,b = draw.textbbox((0,0), text=watermark, font=font)

    draw.text((resize_w-r-x, resize_h-b-y),watermark, font=font, fill=(255,255,255,o))

    result = Image.alpha_composite(img, text)

    os.makedirs('images', exist_ok=True)

    result.convert('RGB').save(f'images/result-{idx + 1}.jpg', quality=qu)
