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
dog_variety = dog['animal_Variety'].value_counts()
print(dog_variety)
v = dog_variety.index.tolist()
n = dog_variety.values.tolist()

plt.pie(n)
# plt.show()
