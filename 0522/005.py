from PIL import Image, ImageDraw

img = Image.open('../images/19-2500x1667.jpg')

draw = ImageDraw.Draw(img)

draw.polygon([(100,100),(1800,1200),(1600,900),(10,1200)],outline='red', width=10, fill='white')

img.show()