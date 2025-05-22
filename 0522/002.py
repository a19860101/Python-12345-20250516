from PIL import Image, ImageFont, ImageDraw

img = Image.open('../images/19-2500x1667.jpg')

draw = ImageDraw.Draw(img)

w = img.size[0]
h = img.size[1]

# draw.line([(0,0),(300,300)], 'red', 10)
# draw.line(xy=[(0,0),(300,300)], fill='red', width=10)
draw.line(xy=[(0,0),(w,h)], fill='red', width=70)
draw.line(xy=[(0,h),(w,0)], fill='red', width=10)

img.show()