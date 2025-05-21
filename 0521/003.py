# 修改圖片尺寸
import os
import glob
from PIL import Image

images = glob.glob('../images/*.[Jj][Pp][Gg]')

image = Image.open(images[0])

# print(image.size)
# print(image.size[0])
# print(image.size[1])

w = image.size[0]
h = image.size[1]

resize_w = 1200
resize_h = int(h * resize_w / w)

print(resize_h)

small_image = image.resize((resize_w,resize_h))

os.makedirs('images',exist_ok=True)

small_image.save('images/small.jpg',quality=60, subsampling=0)