import matplotlib.pyplot as plt

data = [10,20,30,40]
label = ['A','B','C','D']

plt.pie(data, radius=1.2, labels=label)

plt.show()