# import PIL
from PIL import Image
import glob
import os

image = glob.glob('../images/*.[Jj][Pp][Gg]')

# print(image[0])
img = Image.open(image[0])

os.makedirs('images', exist_ok=True)

img.save('images/test.jpg',quality=50, subsampling=0)
# quality 0-100
# subsampling 0,1,2