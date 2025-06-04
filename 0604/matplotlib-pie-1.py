import matplotlib.pyplot as plt

data = [23,41,55,17]
label = ['A','B','C','D']
e = [.1,0,0,0]

plt.pie(data,
        radius=1.2,
        labels=label,
        labeldistance=1.1,
        startangle=15,
        explode=e,
        autopct='%.2f%%'
        )

plt.show()