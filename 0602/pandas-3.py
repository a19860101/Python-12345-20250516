import pandas as pd

datas = pd.read_csv('./Restaurant_C_f.csv')
# print(datas)
print(datas.columns)
# print(datas['Name'])
# print(datas.loc[1])

# condition = datas['Add'].str.contains('中壢')
condition = datas['Town'].str.contains('中壢').fillna(False)
result = datas[condition]

# print(result)

# 保留需要的欄位
# result = result[['Name', 'Add', 'Town']]
# print(result)
# 移除不要的欄位
# result = result.drop(['Id', 'Description'], axis=1)

result.to_excel('a.xlsx')