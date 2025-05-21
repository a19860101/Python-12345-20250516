# import PIL
from PIL import Image
import glob
import os

image = glob.glob('../images/*.[Jj][Pp][Gg]')

# 單一照片壓縮
# print(image[0])
# img = Image.open(image[0])
#
# os.makedirs('images', exist_ok=True)
#
# img.save('images/test.jpg',quality=50, subsampling=0)
# quality 0-100
# subsampling 0,1,2

# 批次圖片壓縮

for idx,img in enumerate(image):
    im = Image.open(img)
    print(im)
    os.makedirs('images', exist_ok=True)
    im.save(f'images/img-{idx+1}.jpg', quality=50, subsampling=0)

