import os
import urllib.request as req

import bs4

url = 'https://www.tenlong.com.tw/'

request = req.Request(url)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

imgs = htmlfile.find_all('img')

for idx,img in enumerate(imgs):
    print(img['src'])
    try:
        os.makedirs('tenlong2', exist_ok=True)
        req.urlretrieve(img['src'], f'tenlong2/img-{idx}.jpg')
    except Exception as e:
        print(e)
        pass