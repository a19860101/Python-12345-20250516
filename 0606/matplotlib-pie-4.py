import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./animal.csv')

# print(data.columns)
# print(data['animal_kind'])
# print(data['animal_Variety'])

# total = len(data)
total, col = data.shape

dog = data[data['animal_kind'].str.contains('狗')]

# 計算元素種類
t = dog['animal_Variety'].nunique()
print(t)

# 計算個別元素數量
# dog_variety = dog['animal_Variety'].value_counts()
# dog_variety = dog['animal_Variety'].value_counts(dropna=False)
# dropna 移除nan
dog_variety = dog['animal_Variety'].value_counts(ascending=False)
# ascending, sort
print(dog_variety)
v = dog_variety.index.tolist()
n = dog_variety.values.tolist()

plt.pie(n)
# plt.show()



#https://blog.csdn.net/qq_18351157/article/details/105993752
#https://stackoverflow.com/questions/35523635/extract-values-in-pandas-value-counts