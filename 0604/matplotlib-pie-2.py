import pandas as pd

data = pd.read_csv('./travel.csv', header=1)

d = data.loc[0]

print(d)