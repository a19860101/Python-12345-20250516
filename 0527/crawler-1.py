# requests模組
import bs4
import requests

url = 'https://www.ptt.cc/bbs/NBA/index.html'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

res = requests.get(url, headers=header, verify=False)

result = res.text

source = bs4.BeautifulSoup(result, 'html.parser')

datas = source.find_all('div', class_='r-ent')

for data in datas:
    if data.a and data.span is not None:
        title = data.a.string
        author = data.find('div', class_='author').string
        date = data.find('div', class_='date').string
        nrec = data.span.string

        print(f'{nrec}-{title}-{author}-{date}')

        with open('ptt.txt','a',encoding='utf-8') as f:
            f.write(f'{nrec}-{title}-{author}-{date} \n')
