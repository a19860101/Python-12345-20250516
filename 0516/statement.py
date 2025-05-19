# 判斷式
x = 0

if x > 0:
    print('success')

if x > 0:
    print('success')
else:
    print('error')

if x > 0:
    print('正')
elif x < 0:
    print('負')
else:
    print('0')

# 3.10之後

s = 'tue'

match s:
    case 'sun':
        print('日')
    case 'mon':
        print('一')
    case 'tue':
        print('二')

if s is 'sun':
    print('日')
elif s is 'mon':
    print('一')
elif s is 'tue':
    print('二')

