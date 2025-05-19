mode = input('台幣轉日幣請按 0\n台幣轉美金請按 1\n日幣轉台幣請按 2\n美金轉台幣請按 3\n')

d = input('請輸入金額:')
#
jrate = 0.206
usrate = 30.23
#
match mode:
    case '0':
        result = int(d) // jrate
        print(f'{d}元台幣約等於{result}日幣')
    case '1':
        result = int(d) // usrate
        print(f'{d}元台幣約等於{result}美金')
    case '2':
        result = int(d) * jrate
        print(f'{d}元日幣約等於{result}台幣')
    case '3':
        result = int(d) * usrate
        print(f'{d}元美金約等於{result}台幣')
