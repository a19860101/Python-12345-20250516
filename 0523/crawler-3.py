# 使用 cookie

import urllib.request as req

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'cookie': 'over18=1',
}

request = req.Request(url, headers=header)
"""
使用with...as的res變數會自動關閉
"""

# res = req.urlopen(request)
#
# result = res.read().decode('utf-8')
#
# res.close()

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')
"""
使用 with...as 時 res 會自動關閉，不用手動關閉 res.close()
"""
# print(result)

if res.closed:
    print('closed')
else:
    print('not close')