# requests模組

import requests

# url = 'https://www.ptt.cc/bbs/NBA/index.html'
url = 'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&destination=D-JP-3231&keyword=&currency=TWD&sort=prec&page=1&start=0&count=10'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

res = requests.get(url, headers=header, verify=False)

print(res.json())
json_datas = res.json()

for data in json_datas['data']['data']:
    print(data['name'])