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

plt.rc('font', family='Microsoft Jhenghei')

plt.plot(close_, marker='.', markersize=8, linewidth=1, label='收盤價')
plt.plot(open_,marker='.', markersize=8, linewidth=1,label='開盤價')
plt.plot(max_,marker='.', markersize=8, linewidth=1,label='最高價')
plt.plot(min_,marker='.', markersize=8, linewidth=1,label='最低價')

plt.ylim(900,1100)

plt.legend()

plt.show()