# kkday

import urllib.request as req
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&destination=D-JP-3231&keyword=&currency=TWD&sort=prec&page=1&start=0&count=10'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

# print(result)

json_datas = json.loads(result)

print(json_datas)
