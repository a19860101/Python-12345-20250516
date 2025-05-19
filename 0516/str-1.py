s = 'hEllO pYtHon'

# print(s[0])
# print(s[1])
# print(s[-1])
# print(s[-2])
#
# print(s[2:7])
# print(s[3:-1])
# print(s[2:])
# print(s[:7])

# 計算文字長度(文字數量包含空格)
# print(len(s))

# upper() 大寫
# print(s.upper())

# lower() 小寫
# print(s.lower())

# capitalize() 首字大寫
# print(s.capitalize())

# title() 每個單字首字大寫
# print(s.title())

# replace() 取代文字
# print(s.replace('pYtHon','World'))

# index() 取得字串索引值 若找不到會報錯
q = 'hello world'
# print(q.index('a'))

# find() 取得字串索引值 若找不到會回傳-1
# print(q.find('a'))

# isalpha() 判斷字串是否為英文
print(q.isalpha())
# isdigit() 判斷字串是否為數字
print(q.isdigit())
q2 = '12345'
print(q2.isdigit())
# endswith() 判斷字串最後一個字母是否為指定字母
print(q.endswith('a'))
# startswith() 判斷字串第一個字母是否為指定字母
print(q.startswith('s'))

# split() 字串轉列表
# print(q.split())
# print(q.split('w'))

# strip() 去除前後空白
q3 = ' asdf asdf '
print(q3)
print(q3.strip())

# lstrip() 去除開頭空白
print(q3.lstrip())

# rstrip() 去除結尾空白
print(q3.rstrip())
