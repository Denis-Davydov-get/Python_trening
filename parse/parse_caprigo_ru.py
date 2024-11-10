import requests
from bs4 import BeautifulSoup

url = 'https://www.caprigo.ru/catalog/19f69068-cd49-11e7-99d1-005056c00008?inRow=four&priceMax=330010&priceMin=10278&withStockBalance=1'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
# with open('1.txt', 'w', encoding="utf-8") as f:
#     f.write(soup)
mydivs = soup.find_all("div", {"class": "products-item__footer"})
print(soup)