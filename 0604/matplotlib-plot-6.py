import pandas as pd

data = pd.read_csv('./STOCK_DAY_2330_202505.csv', encoding='big5', header=1)
print(data.columns)
# print(data['日期'])
print(data['收盤價'][:20])

