from PIL import Image, ImageFont, ImageDraw

img = Image.open('../images/19-2500x1667.jpg').convert('RGBA')
w,h = img.size
text = Image.new(mode='RGBA', size=img.size, color=(255,0,0,0))

font = ImageFont.truetype('../font/Anton-Regular.ttf', 100)

draw = ImageDraw.Draw(text)

draw.text((0,0),'HELLO', font=font, fill=(255,255,255,100))

result = Image.alpha_composite(img, text)

result.show()