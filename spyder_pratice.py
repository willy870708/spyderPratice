import requests 
from bs4 import BeautifulSoup
import re
link = 'https://www.dcard.tw/f'
resp = requests.get(link)

soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
print('Dcard 前二十熱門文章：')
for num, title in enumerate(dcard_title[:20]):
    print("{0:2d}. {1}".format(num+1, title.text))