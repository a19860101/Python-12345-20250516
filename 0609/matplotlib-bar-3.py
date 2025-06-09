import matplotlib.pyplot as plt

# color = ['red','lightgreen','#ff7f50','#708090','#aaff2f']

label = ['A','B','C','D','E']

plt.bar([1,2,3,4,5],[10,30,20,50,80], width=.4, color='red', align='edge')
plt.bar([0.8,1.8,2.8,3.8,4.8],[12,34,25,56,87], width=.4, color='blue')

plt.xticks(range(1,6), label)

plt.show()