# Beautiful Soup
# 安裝套件 pip install beautifulsoup4

import urllib.request as req
import bs4

# from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/NBA/index.html'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'cookie': 'over18=1',
}

request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

source = bs4.BeautifulSoup(result, 'html.parser')

s = source.find('a',class_='board')
logo = source.find('a', id='logo')

# print(s)
# print(s.string)
# print(s.text)
titles = source.find_all('div', class_='title')

for title in titles:
    print(title.text)
    # print(title.a.string)
