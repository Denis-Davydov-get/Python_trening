import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_avg_price_from_mc(page: str) -> dict:
    dict_sku_done = {}
    list_done_sku_price = []
    list_done_sku_name = []
    page = requests.get(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_all_sku_name = soup.find_all("div", attrs={"class": 'refstr _nm'})
    list_all_sku_price = soup.find_all("div", attrs={"class": 'pr'})
    for i in range(len(list_all_sku_name)):
        list_done_sku_name.append(list_all_sku_name[i].text)
    for i in range(len(list_all_sku_price)):
        list_done_sku_price.append(list_all_sku_price[i].text)
    for k, v in zip(list_done_sku_name, list_done_sku_price):
        dict_sku_done[k] = v
    return dict_sku_done


data_dict = get_avg_price_from_mc("https://mc.ru/metalloprokat/stal_listovaya_g_k/Page200/2")
df = pd.DataFrame.from_dict(data_dict).fillna(0, inplace=True)
df.to_csv('output.csv', index=False)

