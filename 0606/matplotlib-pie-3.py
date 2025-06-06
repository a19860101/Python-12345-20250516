import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./animal.csv')

# print(data.columns)
print(data['animal_kind'])
print(data['animal_Variety'])
