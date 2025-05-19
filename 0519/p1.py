# 1oz = 29.573ml

s = input('請輸入換算單位:(oz/cc)')
x = input('請輸入轉換的容量:')

if s=='oz':
    result = float(x) * 29.573
    result = round(result,2)
    print(f'您的換算結果為{x}oz約{result}cc')
else:
    result = float(x) / 29.573
    result = round(result,2)
    print(f'您的換算結果為{x}c約{result}oz')