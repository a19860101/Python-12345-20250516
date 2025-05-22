from PIL import Image, ImageDraw

img = Image.open('../images/19-2500x1667.jpg')

w, h = img.size

# print(w,h)

draw = ImageDraw.Draw(img)

draw.circle((w/2,h/2),radius=200, outline='white', width=20)

img.show()
