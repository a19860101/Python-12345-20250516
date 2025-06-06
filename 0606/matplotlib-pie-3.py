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

plt.rc('font', family='Microsoft Jhenghei')

plt.pie([dog_n,cat_n,other_n],
        autopct='%.1f%%',
        labels=['狗','貓','其他'],
        explode=[.1,.1,.2],
        startangle=15
        )

plt.legend()

plt.show()