import random
a = 1
b = 100
ans = random.randint(a,b)
print(ans)
# inp = int(input('請輸入數字:'))

inp = input('請輸入數字:')
inp = int(inp)

while inp != ans:
    if inp > ans:
        b = inp
        print('數字太大')
        print(f'{a}以上{b}以下')
        inp = int(input('請輸入數字:'))
    else:
        a = inp
        print('數字太小')
        print(f'{a}以上{b}以下')
        inp = int(input('請輸入數字:'))

print('Bingo!!!')





# if inp > ans:
#     print('數字太大')
#
# if inp < ans:
#     print('數字太小')
#
# if inp == ans:
#     print('猜對')
