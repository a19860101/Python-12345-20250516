import pandas as pd

datas = pd.read_csv('./Restaurant_C_f.csv')
# print(datas)
print(datas.columns)
# print(datas['Name'])
# print(datas.loc[1])

condition = datas['Add'].str.contains('中壢')
result = datas[condition]

# result = result[['Name', 'Add']]

result = result.drop(['Id', 'Description'], axis=1)

result.to_excel('a.xlsx')