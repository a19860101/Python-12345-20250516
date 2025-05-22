from PIL import Image, ImageFont, ImageDraw

img = Image.open('../images/19-2500x1667.jpg').convert('RGBA')
w,h = img.size
text = Image.new(mode='RGBA', size=img.size, color=(255,0,0,0))

font = ImageFont.truetype('../font/Anton-Regular.ttf', 200)

draw = ImageDraw.Draw(text)

l,t,r,b = draw.textbbox((0,0), text='HELLO', font=font)
print(l,t,r,b)

# 右下角
# draw.text((w-r-50, h-b-50),'HELLO', font=font, fill=(255,0,0,255))

# 正中間
draw.text((w/2-r/2 , h/2-b/2),'HELLO', font=font, fill=(255,0,0,255))

result = Image.alpha_composite(img, text)

result.convert('RGB').save('result.jpg')
