#
import os
import glob
from PIL import Image, ImageEnhance

images = glob.glob('./images/*.[Jj][Pp][Gg]')

image = Image.open(images[0])

brightness = ImageEnhance.Brightness(image)
contrast = ImageEnhance.Contrast(image)
color = ImageEnhance.Color(image)

image = brightness.enhance(1.6)
image = contrast.enhance(3)
image = color.enhance(0.5)

image.show()






