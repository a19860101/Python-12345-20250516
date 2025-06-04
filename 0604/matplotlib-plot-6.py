import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./STOCK_DAY_2330_202505.csv', encoding='big5', header=1)
# print(data.columns)
# print(data['日期'])
# print(data['收盤價'][:20])

close_ = list(data['收盤價'][:20])
open_ = list(data['開盤價'][:20])
max_ = list(data['最高價'][:20])
min_ = list(data['最低價'][:20])

open_ = [ float(i.replace(',','')) for i in open_]
max_ = [ float(i.replace(',','')) for i in max_]

date = list(data['日期'][:20])
x = [f'{d[-2:]}日' for d in date]
print(x)

plt.rc('font', family='Microsoft Jhenghei')

plt.plot(x,close_, marker='.', markersize=8, linewidth=1, label='收盤價')
plt.plot(x,open_,marker='.', markersize=8, linewidth=1,label='開盤價')
plt.plot(x,max_,marker='.', markersize=8, linewidth=1,label='最高價')
plt.plot(x,min_,marker='.', markersize=8, linewidth=1,label='最低價')

plt.ylim(900,1100)

plt.xlabel('日期')
plt.ylabel('股價')
plt.xticks(rotation=45)

plt.title('台積電(2330)114年5月')
plt.legend()

plt.show()