import pandas as pd

# 一維資料
data = pd.Series([12,35,26,43,71])

# print(data)

# 二維資料
# data2 = pd.DataFrame([12,35,26,43,71])

data3 = pd.DataFrame([
    [1,2,3,4,5],
    ['A','B','C','D','E']
])

data4 = pd.DataFrame([
    ['商品一','199'],
    ['商品二', '299']
])

data5 = pd.DataFrame([
    {
        '名稱':'商品一',
        '價格': '299',
        '庫存': 2
    },
    {
        '名稱':'商品二',
        '價格':'499',
        '庫存': 6
    },
    {
        '名稱':'商品三',
        '價格':'999',
        '庫存': 12
    },
    {
        '名稱':'商品四',
        '價格':'999',
        '庫存': 1
    },
], index=['A','B','C','D'])

print(data5)
print(data5.size)
print(data5.columns)
print(data5.index)
print(data5.shape)