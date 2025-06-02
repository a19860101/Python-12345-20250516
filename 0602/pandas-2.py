import pandas as pd

users = pd.DataFrame([
    {'name': 'Zac', 'age': 32, 'gender': 'M'},
    {'name': 'Max', 'age': 28, 'gender': 'M'},
    {'name': 'Andy', 'age': 30, 'gender': 'M'},
    {'name': 'Amy', 'age': 22, 'gender': 'F'},
    {'name': 'Laura', 'age': 26, 'gender': 'F'}
])

print(users['age'])
print(users['age'].min())
print(users['age'].max())
print(users['age'].mean())
print(users['age'].std())
print(users['age'].median())