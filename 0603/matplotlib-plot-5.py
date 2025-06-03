import requests
url = 'https://api.openweathermap.org/data/2.5/forecast?q=taipei&appid=b1ecbccd638b763d489602917ba47cc3&units=metric&lang=zh_TW'

res = requests.get(url)

result = res.json()

for data in result['list']:
    print(data)