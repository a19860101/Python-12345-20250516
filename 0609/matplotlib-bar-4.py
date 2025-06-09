import matplotlib.pyplot as plt

# color = ['red','lightgreen','#ff7f50','#708090','#aaff2f']

label = ['A','B','C','D','E']
w = 0.2

plt.rc('font', family='Microsoft Jhenghei')
plt.title('某某分布圖')

plt.bar([i for i in range(1,len(label)+1)],[10,30,20,50,80], width=w, color='red', align='edge', label='女')
plt.bar([i - w / 2 for i in range(1,len(label)+1)],[12,34,25,56,87], width=w, color='blue', label='男')

plt.xticks(range(1,6), label)
plt.yticks(range(0,100,10))

plt.xlabel('項目')
plt.ylabel('數量')

plt.legend()

plt.grid(axis='y', linestyle='--')

plt.show()