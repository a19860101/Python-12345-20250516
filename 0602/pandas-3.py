import pandas as pd

datas = pd.read_csv('./Restaurant_C_f.csv')
# print(datas)
# print(datas.columns)
# print(datas['Name'])
# print(datas.loc[1])

condition = datas['Add'].str.contains('中壢')
# condition = datas['Town'].str.contains('中壢')
result = datas[condition]

# print(result)
result.to_excel('a.xlsx')