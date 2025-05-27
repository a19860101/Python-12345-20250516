import os
from urllib.parse import urljoin

import bs4
import requests

url = 'https://www.vscinemas.com.tw/film/index.aspx'

res = requests.get(url, verify=False)

htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')

# imgs = htmlfile.find_all('img')
imgs = htmlfile.select('body > article > ul > li > figure > a > img')
# body > article > ul > li:nth-child(1) > figure > a > img
for idx,img in enumerate(imgs):
    # print(img['title'])
    img_url = urljoin(url, img['src'])
    # print(img_url)
    im = requests.get(img_url, verify=False)
    os.makedirs('movie', exist_ok=True)
    with open(f'movie/{img['title']}.jpg', 'wb')as f:
        f.write(im.content)