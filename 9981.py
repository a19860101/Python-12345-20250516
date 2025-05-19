# 九九乘法表
#
# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i}x{j}={i*j}')


# for i in range(1,5):
#     print('*'*i)

for i in range(10):
    for a in range(1,10-i):
        print('-' * a)
    for b in range(10-i,10):
        print('Q' * b)
    print('\n', end='')