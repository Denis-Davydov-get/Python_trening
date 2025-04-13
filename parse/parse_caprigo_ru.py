<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup

url = 'https://mc.ru/price/msk'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
mydivs = soup.find_all("ul", {"class": "pagePriceList"})
links = soup.find_all('a')
for link in links:
    if "https://mc.ru/" in link.get('href') and ".zip" in link.get('href'):
        with open(link, "wb") as f:
            f.write(requests.get(src).content)

=======
import requests
from bs4 import BeautifulSoup

url = 'https://www.caprigo.ru/catalog/19f69068-cd49-11e7-99d1-005056c00008?inRow=four&priceMax=330010&priceMin=10278&withStockBalance=1'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
# with open('1.txt', 'w', encoding="utf-8") as f:
#     f.write(soup)
# mydivs = soup.find_all("div", {"class": "products-item__footer"})
my_divs = soup.find_all("div")
print(my_divs)
>>>>>>> 24dc66684f30afe3ba5cce7e4311dc8c449aabcc
