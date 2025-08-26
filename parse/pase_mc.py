import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_avg_price_from_mc():
    """
    @page - страница для парсинга
    @list_all_sku - список всех sku
    @list_done_sku - готовый список товаров
    """
    list_done_sku = {}
    page = requests.get("https://metall-dk.ru/catalog/listovoy-prokat/")
    soup = BeautifulSoup(page.content, 'html.parser')
    list_all_sku = soup.find_all("div", attrs={"class": "table-view"})
    for list_all_sku in list_all_sku:
        list_done_sku[list_all_sku.find_all_next("a", class_="dark_link")] = \
            list_all_sku.find_all_next("span", attrs={"class": "values_wrapper"})
    return list_done_sku

# df = pd.read_excel("products.xlsx", sheet_name="Products")
# df['price'] = df['name(ru-ru)'].apply(get_avg_price_from_mc)
# df.to_excel("products_with_prices.xlsx", index=False)

print(get_avg_price_from_mc())