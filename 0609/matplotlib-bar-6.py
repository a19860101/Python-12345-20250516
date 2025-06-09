import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./travel2.csv', header=1)
print(data)
#112
asia_112 = data.loc[0]['Asia']
total_112 = data.loc[0]['Total']
other_112 = asia_112 - total_112
data_112 = list(data.loc[0][2:-1])
data_112.append(other_112)

print(data_112)

#113
asia_113 = data.loc[1]['Asia']
total_113 = data.loc[1]['Total']
other_113 = asia_113 - total_113
data_113 = list(data.loc[1][2:-1])
data_113.append(other_113)

print(data.columns)
label = ['日本','韓國','香港','中國','澳門','越南','泰國','其他']

w = 0.4
plt.rc('font', family='Microsoft Jhenghei')
plt.bar([i for i in range(1, len(label) + 1)],data_112,width=w,label='112年', align='edge', color='blue')
plt.bar([i-w/2 for i in range(1, len(label) + 1)],data_113,width=w,label='113年', color='red')

plt.xticks(range(1, len(label) + 1), label)
plt.legend()

plt.title('112/113年出國人數統計')
plt.xlabel('國家')
plt.ylabel('出國人數/百萬')

plt.grid(axis='y', linestyle='--')

plt.show()