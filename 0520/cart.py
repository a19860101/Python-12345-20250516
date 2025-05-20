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

while True:
    selected = input('請輸入商品名稱(按q完成購買):')
    if selected == 'q':
        break
    elif selected not in products:
        print('沒有這個商品')
    elif selected in products:
        cart.append(selected)

print(cart)