from PIL import Image,ImageFont, ImageDraw

img = Image.open('./IMG_8615.JPEG')

exi = img._getexif()
# print(e)
# print(exi[36867])
date = exi[36867]

w = img.size[0]
h = img.size[1]

font = ImageFont.truetype('Roboto-SemiBold.ttf', 42)   # 設定字型
draw = ImageDraw.Draw(img)

left, top, right, bottom = font.getmask(date).getbbox()
print(left,top,right,bottom)
# d =  font.getmask(date).getbbox()
# print(d)
# draw.text((w - right - 20, h - bottom - 20), date, fill='#fa0', font=font)

# img.save('q.jpg')

# img.show()
# for k,v in e.items():
    # k = TAGS[k]
    # print(f'{k}:{v}')
    # print(k['36867'])
    # DateTimeOriginal`