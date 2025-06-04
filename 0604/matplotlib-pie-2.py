import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./travel.csv', header=1)
print(data)

asia = data['Asia'].loc[0]
total = data['Total'].loc[0]
other = asia - total

label = ['日本','南韓','香港','中國','澳門','其他國家']
color = ['red','green','blue','purple','orange','pink']
n = list(data.loc[0][2:7])
n.append(other)

plt.rc('font', family='Microsoft Jhenghei')
plt.pie(n,labels=label, autopct='%.1f%%', radius=1.2, colors=color)

plt.legend(bbox_to_anchor=(1,1))
plt.show()