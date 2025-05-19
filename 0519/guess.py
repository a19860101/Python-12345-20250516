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
        print('數字太大')
        print(f'{inp}以下')
        inp = int(input('請輸入數字:'))
    else:
        print('數字太小')
        print(f'{inp}以上')
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
