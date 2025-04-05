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

