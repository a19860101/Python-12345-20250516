import random
a = 1
b = 100
ans = random.randint(a,b)
print(ans)
# inp = int(input('請輸入數字:'))

inp = input('請輸入數字:')
inp = int(inp)

if inp > ans:
    print('數字太大')

if inp < ans:
    print('數字太小')

if inp == ans:
    print('猜對')
