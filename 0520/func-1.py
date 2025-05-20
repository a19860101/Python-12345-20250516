def foo():
    print('hello function')

def foo2(x):
    r = x * 1.1
    return r

def area(w,h):
    return w * h

a1 = area(h=14, w=14)
print(a1)

def twToUs(dollar, rate=31.2):
    result = round(dollar / rate , 2)
    return result

# d1 = twToUs(100000)
# print(d1)
#
# d2 = twToUs(100000, 30.8)
# print(d2)

# 圓面積 pir^2

import math
def circleArea(r):
    result = math.pi * (r ** 2)
    result = round(result, 1)
    return result

c1 = circleArea(18)
print(c1)

def cir(r):
    result = math.pi * r * 2
    result = round(result, 1)
    return result

c2 = cir(12)
print(c2)

# for i in range(10,0,-1):
#     print(i)

import time
def count(end, start=0):
    for i in range(end, start, -1):
        print(i)
        time.sleep(1)
    print('倒數結束!')

s = input('請輸入秒數:')
print('開始倒數:')
count(int(s))