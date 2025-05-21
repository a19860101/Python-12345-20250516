# import PIL
from PIL import Image
import glob

image = glob.glob('../images/*.[Jj][Pp][Gg]')

# print(image[0])
img = Image.open(image[0])

print(img)