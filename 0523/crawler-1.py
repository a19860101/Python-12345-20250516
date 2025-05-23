import urllib.request as req

url = 'https://exiv2.org/tags.html'

request = req.Request(url)

print(request)