import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_avg_price_from_mc(page: str) -> dict:
    dict_sku_done = {}
    list_done_sku_price = []
    list_done_sku_name = []
    page = requests.get(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_all_sku_name = soup.find_all("a", attrs={"class": 'js_h_pua'})
    list_all_sku_price = soup.find_all("strong", attrs={"class": 'product-item__price'})
    for i in range(len(list_all_sku_name)):
        list_done_sku_name.append(list_all_sku_name[i].text.strip())
    for i in range(len(list_all_sku_price)):
        list_done_sku_price.append(list_all_sku_price[i].text.strip().replace("\r\n\r\n\t", ""))
    for k, v in zip(list_done_sku_name, list_done_sku_price):
        dict_sku_done[k] = v
    return dict_sku_done


def pagination(agent: int) -> str:
    for i in range(1, agent):
        return f"https://www.grandline.ru/katalog/krovlya/profnastil/?limit=60&page={i}"
    return None


df = pd.DataFrame.from_dict(get_avg_price_from_mc("https://www.grandline.ru/katalog/krovlya/profnastil/?limit=60&page=1"), orient='index', )
for i in range(2, 4):
    for k, v in get_avg_price_from_mc(pagination(i)).items():
        df.loc[get_avg_price_from_mc(pagination(i))][k] = get_avg_price_from_mc(pagination(i))[v]


df.to_excel('grandline.xlsx', index=True)
print(df)