def foo():
    print('hello function')

def foo2(x):
    r = x * 1.1
    return r

def area(w,h):
    return w * h

def twToUs(dollar, rate=31.2):
    result = round(dollar / rate , 2)
    return result

d1 = twToUs(100000)
print(d1)

d2 = twToUs(100000, 30.8)
print(d2)