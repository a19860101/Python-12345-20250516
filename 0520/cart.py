products = {
    'apple': 100,
    'banana' : 120,
    'kiwi': 150
}

cart = []
total = 0

print('-----商品項目-----')
for k,v in products.items():
    print(f'{k:10}: {v}元')
print('---------------')