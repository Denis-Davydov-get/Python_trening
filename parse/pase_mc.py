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
    list_all_sku = soup.find_all("div", attrs={"class": "cart_in_part item_img "})
    # for sku in list_all_sku:
    #     list_done_sku[sku.find("a").text] = sku.find("em", attrs={"class": "unit_price"})
    for sku in list_all_sku:
        return sku.find_all("a").text


# df = pd.read_excel("products.xlsx", sheet_name="Products")
# df['price'] = df['name(ru-ru)'].apply(get_avg_price_from_mc)
# df.to_excel("products_with_prices.xlsx", index=False)

print(get_avg_price_from_mc())
