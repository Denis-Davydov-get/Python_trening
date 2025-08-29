import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_avg_price_from_mc(page: str) -> dict:
    dict_sku_done = {}
    list_done_sku_price = []
    list_done_sku_name = []
    page = requests.get(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_all_sku_name = soup.find_all("div", attrs={"class": 'refstr'})
    list_all_sku_price = soup.find_all("div", attrs={"class": 'pr'})
    for i in range(len(list_all_sku_name)):
        list_done_sku_name.append(list_all_sku_name[i].text.strip())
    for i in range(len(list_all_sku_price)):
        list_done_sku_price.append(list_all_sku_price[i].text.strip().replace("\r\n\r\n\t", ""))
    for k, v in zip(list_done_sku_name, list_done_sku_price):
        dict_sku_done[k] = v
    return dict_sku_done


def pagination(agent: int) -> dict:
    try:
        for i in range(1, agent):
            return get_avg_price_from_mc(f"https://mc.ru/metalloprokat/stal_listovaya_g_k/PageN/{i}")
    except Exception as e:
        return print(e)


df = pd.DataFrame.from_dict(pagination(2), orient='index')
print(df)
df.to_excel('mc_list_gk.xlsx', index=True)