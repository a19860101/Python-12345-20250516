import urllib.request as req
import openpyxl
import ssl
import json
import os

wb = openpyxl.Workbook()
ws = wb.active

title = ['名稱','地址']
ws.append(title)

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://media.taiwan.net.tw/XMLReleaseALL_public/hotel_C_f.json'
# url = 'https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&IsTransData=1'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8-sig')

print(result)

json_datas = json.loads(result)

# print(json_datas)

os.makedirs('output', exist_ok=True)

for data in json_datas['XML_Head']['Infos']['Info']:
    print(data)
    ct = [data['Name'],data['Add']]
    ws.append(ct)

wb.save('output/hotel.xlsx')