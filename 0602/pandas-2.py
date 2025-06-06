import pandas as pd

users = pd.DataFrame([
    {'name': 'Zac', 'age': 32, 'gender': 'M'},
    {'name': 'Max', 'age': 28, 'gender': 'M'},
    {'name': 'Andy', 'age': 30, 'gender': 'M'},
    {'name': 'Amy', 'age': 22, 'gender': 'F'},
    {'name': 'Laura', 'age': 26, 'gender': 'F'}
])

print(users['age'])
# 最小值
print(users['age'].min())
# 最大值
print(users['age'].max())
# 平均數
print(users['age'].mean())
# 標準差
print(users['age'].std())
# 中位數
print(users['age'].median())


condition = users['age'] >= 30
print(users[condition])
print(users[users['age'] < 30])
print(users[users['gender']=='M'])

print(users['name'].str.contains('A'))

print(users[users['name'].str.contains('A')])
a = users['name'].str.contains('a')
print(users[a])