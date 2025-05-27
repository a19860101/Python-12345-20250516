import openpyxl
import requests

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['行程','原價','最高價','最低價'])

url = f'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&destination=D-JP-3261&keyword=&currency=TWD&sort=prec&page=1&start=0&count=10'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}
request = requests.get(url, headers=header, verify=False)

json_datas = request.json()

for data in json_datas['data']['data']:
    ct = [data['name'], data['official_price'], data['max_price'], data['min_price']]
    ws.append(ct)

wb.save('kkday.xlsx')