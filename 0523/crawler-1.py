# 基礎爬蟲
import urllib.request as req

url = 'https://exiv2.org/tags.html'

request = req.Request(url)

res = req.urlopen(request)

result = res.read().decode('utf-8')

print(result)