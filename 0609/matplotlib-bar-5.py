import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./travel.csv', header=1)
print(data)

asia = data.loc[0]['Asia']
total = data.loc[0]['Total']
other = asia - total

x_label = ['日本','韓國','香港','中國','澳門','其他']
y_data = list(data.loc[0][2:-1])
y_data.append(other)
print(y_data)
plt.rc('font',family='Microsoft Jhenghei')
plt.bar(x_label, y_data)

plt.show()