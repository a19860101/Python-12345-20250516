import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

dataX = [1, 3, 5, 7, 9]
dataY = [20, 24, 32, 18, 26]

# (1,20)(3,24)(5,32)(7,18)(9,26)
plt.plot(dataX,dataY,
         color='red',
         linewidth=1.5,
         linestyle='-',
         marker=".",
         markersize=15,
         label='六月')

# plt.plot([20, 24, 32, 18, 26])

plt.title('Python圖表')
plt.xlabel('日期')
plt.ylabel('溫度')

plt.xlim(0,30)
plt.xticks(range(1,31,7))

plt.ylim(0, 40)
plt.yticks(range(0, 41, 10))

#圖例顯示
plt.legend()

plt.show()