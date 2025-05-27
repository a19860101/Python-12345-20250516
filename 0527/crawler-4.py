import os

import bs4
import requests

url = 'https://www.tenlong.com.tw/'

res = requests.get(url)

htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')

imgs = htmlfile.find_all('img')

for idx,img in enumerate(imgs):
    # print(img['src'])
    try:
        img_src = requests.get(img['src'])
        os.makedirs('tenlong', exist_ok=True)
        with open(f'tenlong/{idx}.jpg', 'wb')as f:
            f.write(img_src.content)
    except Exception as e:
        print(e)
        pass