from PIL import Image, ImageFont, ImageDraw

img = Image.open('../images/19-2500x1667.jpg')

font = ImageFont.truetype('NotoSansTC-SemiBold.ttf', 200)

draw = ImageDraw.Draw(img)

draw.text((100,200), 'HELLO', fill='red', font=font)

img.show()