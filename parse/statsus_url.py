import requests
from bs4 import BeautifulSoup

for i in range(1, 3):
    page = requests.get(f"https://mc.ru/metalloprokat/stal_listovaya_g_k/PageN/{i}")
    print(page.status_code())
