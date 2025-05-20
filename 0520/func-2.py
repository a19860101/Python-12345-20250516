def foo(*args):
    for i in args:
        print(i)

def foo2(*args):
    return args

datas = foo2('apple',123,'banana',999)

for data in datas:
    print(data)