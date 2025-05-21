# 修改圖片尺寸
import os
import glob
from PIL import Image

images = glob.glob('./images/*.[Jj][Pp][Gg]')
# 打包的路徑
# images = glob.glob('./images/*.[Jj][Pp][Gg]')
resize_w = int(input('請輸入縮圖寬度:'))
qu = int(input('請輸入品質(0-100):'))

for idx, image in enumerate(images):
    img = Image.open(image)

    # print(image.size)
    # print(image.size[0])
    # print(image.size[1])

    w = img.size[0]
    h = img.size[1]

    resize_h = int(h * resize_w / w)

    print(resize_h)

    small_image = img.resize((resize_w,resize_h))

    os.makedirs('small',exist_ok=True)

    small_image.save(f'small/small-{idx + 1}.jpg',quality=qu, subsampling=1)