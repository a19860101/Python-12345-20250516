# dictionary 字典

# users = {
#     'key':'value',
#     'key1':'value1'
# }

users = {
    'name': 'John',
    'email': 'asdf@gmail.com',
    'phone': '0987654321',
}

# print(users)
# print(users['name'])
# print(users['email'])
# print(users['phone'])
# print(users.keys())
# print(users.values())
# print(users.items())

# users['age'] = '20'
# users.setdefault('age','20')

# del users['email']
# users.pop('age')

# print(list(users.keys()))
# print(list(users.values()))
# print(list(users.items()))

# for k in users.keys():
#     print(k)
#
# for v  in users.values():
#     print(v)

# for k,v in users.items():
#     print(f'{k}:{v}')

datas = [
    {
        'name': 'John',
        'email': 'asdf@gmail.com',
        'phone': '0987654321',
        'skill': ['photoshop','illustrator']
    },
    {
        'name': 'Mary',
        'email': 'ewgwegwegweg@gmail.com',
        'phone': '09122424242',
        'skill': ['Python']
    }
]
# print(datas[1])
# for data in datas:
    # print(data['name'])
    # print(data['email'])
    # print(data)

for data in datas:
    for k,v in data.items():
        print(f'{k}:{v}')
    print('=================================')

