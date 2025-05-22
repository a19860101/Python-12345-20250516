from PIL import Image, ImageDraw, ImageFont

# layer = Image.new(mode='RGB',size=(600,400), color='gray')
layer = Image.new(mode='RGBA', size=(600,400), color=(255,0,0,255))

font = ImageFont.truetype('../font/Anton-Regular.ttf', 100)

draw = ImageDraw.Draw(layer)

# draw.text((0,0),'HELLO',fill='white', font_size=100)
draw.text((250,150),'HELLO',fill='white', font=font)

layer = layer.rotate(45, expand=1)

layer.show()