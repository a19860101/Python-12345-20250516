import requests
import matplotlib.pyplot as plt
import datetime

url = 'https://api.openweathermap.org/data/2.5/forecast?q=taipei&appid=b1ecbccd638b763d489602917ba47cc3&units=metric&lang=zh_TW'

res = requests.get(url)

result = res.json()

temp = []
x = []

for data in result['list']:
    # print(data['main']['temp'])
    temp.append(data['main']['temp'])
    d = datetime.datetime.fromtimestamp(data['dt'])
    x.append(f'{d.day}日{d.hour}時')
print(x)
plt.rc('font', family='Microsoft Jhenghei')

plt.plot(x,temp,marker='.', markersize='6')
plt.ylim(0,50)

plt.title('天氣預報')
plt.ylabel('溫度(攝氏)')

plt.xticks(
    rotation=45,
    fontsize=8,
    color='red'
)

plt.show()