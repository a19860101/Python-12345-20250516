from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('./images/IMG_8439.JPEG')

data = img.getexif()
data2 = img._getexif()

print(data2)

for k,v in data2.items():
    k = TAGS[k]
    print(f'{k}:{v}')

print(data2[36867])