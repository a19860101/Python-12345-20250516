import matplotlib.pyplot as plt

color = ['red','lightgreen','#ff7f50','#708090','#aaff2f']

label = ['A','B','C','D','E']

plt.bar([1,2,3,4,5],[10,30,20,50,80], width=.8,color=color, tick_label=label)

plt.show()