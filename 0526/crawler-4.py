# kkday

import urllib.request as req
import openpyxl
import ssl
import json
import os

wb = openpyxl.Workbook()
ws = wb.active

title = ['行程','原價','最高價','最低價']
ws.append(title)
# ws.append(['123','123','123','123'])

# wb.save('test.xlsx')

ssl._create_default_https_context = ssl._create_unverified_context

for i in range(10):

    # url = f'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&destination=D-JP-3231&keyword=&currency=TWD&sort=prec&page={i+1}&start=0&count=10'
    url = f'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&destination=D-JP-3261&keyword=&currency=TWD&sort=prec&page={i+1}&start=0&count=10'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    request = req.Request(url, headers=header)

    with req.urlopen(request) as res:
        result = res.read().decode('utf-8')

    json_datas = json.loads(result)

    os.makedirs('output', exist_ok=True)

    for data in json_datas['data']['data']:
        ct = [data['name'],data['official_price'],data['max_price'],data['min_price']]
        ws.append(ct)

    wb.save('output/kkday.xlsx')
