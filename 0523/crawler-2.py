# 使用User-Agent

import urllib.request as req

url = 'https://www.ptt.cc/bbs/NBA/index.html'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

request = req.Request(url, headers=header)

res = req.urlopen(request)

result = res.read().decode('utf-8')

print(result)