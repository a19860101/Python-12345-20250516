import pandas as pd

data = pd.read_csv('./travel.csv', header=1)
print(data)

asia = data['Asia'].loc[0]
total = data['Total'].loc[0]
other = asia - total

label = ['日本','南韓','香港','中國','澳門','其他國家']
