# 修改圖片尺寸
import os
import glob
from PIL import Image

images = glob.glob('../images/*.[Jj][Pp][Gg]')

image = Image.open(images[0])

small_image = image.resize((400,900))

os.makedirs('images',exist_ok=True)

small_image.save('images/small.jpg')