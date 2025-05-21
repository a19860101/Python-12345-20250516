#
import os
import glob
from PIL import Image, ImageEnhance

images = glob.glob('./images/*.[Jj][Pp][Gg]')

image = Image.open(images[0])

# 亮度
brightness = ImageEnhance.Brightness(image)
# 對比
contrast = ImageEnhance.Contrast(image)
# 飽和度
color = ImageEnhance.Color(image)

# image = color.enhance(0)
image = brightness.enhance(1.6)
image = contrast.enhance(0.6)

image.show('heelo')






