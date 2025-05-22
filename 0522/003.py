from PIL import Image, ImageDraw

img = Image.open('../images/19-2500x1667.jpg')

draw = ImageDraw.Draw(img)

draw.rectangle([(100,100),(500,500)],fill='red',outline='green',width=20)
draw.rectangle([(500,100),(1500,500)],outline='white',width=20)

img.show()