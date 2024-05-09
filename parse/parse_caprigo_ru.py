import requests
from bs4 import BeautifulSoup

url = 'https://www.caprigo.ru/catalog/19f69068-cd49-11e7-99d1-005056c00008?inRow=four&priceMax=330010&priceMin=10278&withStockBalance=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser').encode('utf-8')
soup = str(soup)
with open('1.txt', 'w', encoding="utf-8") as f:
    f.write(soup)
