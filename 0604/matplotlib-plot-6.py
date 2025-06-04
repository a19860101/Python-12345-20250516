import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./STOCK_DAY_2330_202505.csv', encoding='big5', header=1)
# print(data.columns)
# print(data['日期'])
# print(data['收盤價'][:20])

d = list(data['收盤價'][:20])
d2 = list(data['開盤價'][:20])
print(d)
print(d2)

plt.plot(d, marker='.', markersize=8)
plt.plot(d2,marker='.', markersize=8, color='red')

plt.ylim(800,1100)

plt.show()