# kkday

import urllib.request as req
import ssl
import json
import os

ssl._create_default_https_context = ssl._create_unverified_context

for i in range(5):

    url = f'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&destination=D-JP-3231&keyword=&currency=TWD&sort=prec&page={i+1}&start=0&count=10'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    request = req.Request(url, headers=header)

    with req.urlopen(request) as res:
        result = res.read().decode('utf-8')

    json_datas = json.loads(result)

    os.makedirs('output', exist_ok=True)

    with open('output/kkday2.txt','a',encoding='utf-8') as f:
        for idx,data in enumerate(json_datas['data']['data']):
            print(f'{i * 10 + (idx + 1)}.{data['name']} \n 原價{data['official_price']} \\ 最高價格{data['max_price']} \\ 最低價格{data['min_price']}')
            print('----------------------------------------')
            ct = f'{i * 10 + (idx + 1)}. {data['name']} \n 原價{data['official_price']} \n 最高價格{data['max_price']} \\ 最低價格{data['min_price']} \n ---------------------------------------- \n'
            f.write(ct)