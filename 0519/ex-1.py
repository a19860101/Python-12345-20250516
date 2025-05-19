mode = input('請問要換算的是美金還是台幣? (換算美金按0,換算台幣按1):')
d = input('請輸入金額:')

rate = 30.2

if mode == '0':
    result = int(d) * rate
    print(f'{d}元美金約等於{result}台幣')
else:
    result = int(d) // rate
    print(f'{d}元台幣約等於{result}美金')