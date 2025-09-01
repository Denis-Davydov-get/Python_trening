import requests
from bs4 import BeautifulSoup

for i in range(1, 13):
    url = f"https://mc.ru/metalloprokat/stal_listovaya_g_k/PageN/{i}"
    page = requests.get(url)
    print(page, url)