# q = input('請輸入文字:')
#
# print(q)

# 台幣轉美金

x = input('請輸入台幣:')
rate = 30.2

result = int(x) / rate
result = round(result, 2)
# result = round(int(x) / rate,2)

# round() 四捨五入

# result = int(x) // rate

print(f'{x}元台幣約等於{result}美金')