from PIL import Image

image = Image.open('./images/img-1.jpg')

image = image.rotate(180, expand=1)

image.show()