import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./travel2.csv', header=1)
print(data)
#112
asia_112 = data.loc[0]['Asia']
total_112 = data.loc[0]['Total']
other_112 = asia_112 - total_112

#113
asia_113 = data.loc[1]['Asia']
total_113 = data.loc[1]['Total']
other_113 = asia_113 - total_113

print(data.columns)
label = ['日本','韓國','香港','中國','澳門','越南','泰國','其他']
