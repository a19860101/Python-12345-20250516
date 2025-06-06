import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./animal.csv')

# print(data.columns)
# print(data['animal_kind'])
# print(data['animal_Variety'])

# total = len(data)
total, col = data.shape

dog = data[data['animal_kind'].str.contains('狗')]
cat = data[data['animal_kind'].str.contains('貓')]

dog_n = len(dog)
cat_n = len(cat)
other_n = total - dog_n - cat_n

print(other_n)