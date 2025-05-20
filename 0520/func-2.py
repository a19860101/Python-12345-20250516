def foo(*args):
    for i in args:
        print(i)

def foo2(*args):
    return args

# datas = foo2('apple',123,'banana',999)

# for data in datas:
#     print(data)

def foo3(**kwargs):
    return kwargs

# datas = foo3(name='John',email='asdf@gmail.com')
# for k,v in datas.items():
#     print(f'{k}:{v}')

def foo4(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')

# foo4(name='John',email='asdf@gmail.com',phone='98798798798')

def foo5(*args, **kwargs):
    return [args, kwargs]

r = foo5(1,2,3,name='john')
print(r)
