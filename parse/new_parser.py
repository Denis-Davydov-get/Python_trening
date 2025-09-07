from datetime import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import time
from random import uniform

# Добавляем заголовки для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def fetch_page(url: str) -> BeautifulSoup:
    """Получение содержимого страницы"""
    try:
        response = requests.get(url, headers)
        response.raise_for_status()
        time.sleep(uniform(1, 2))
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке страницы {url}: {e}")
        return None


def parse_prices(soup: BeautifulSoup) -> Dict[str, str]:
    """Парсинг названий и цен товаров"""
    names = soup.find_all("div", attrs={"class": 'product-card__info'})
    prices = soup.find_all("div", attrs={"class": 'product-card__prices'})

    if len(names) != len(prices):
        print("Ошибка: количество названий не совпадает с количеством цен")
        return {}

    return {
        name.text.strip(): price.text.strip().replace("\r\n\r\n\t", "")
        for name, price in zip(names, prices)
    }


def get_all_pages_data(base_url: str, total_pages: int) -> Dict[str, str]:
    """Сбор данных со всех страниц"""
    all_data = {}

    for page_num in range(1, total_pages + 1):
        url = f"{base_url}&page={page_num}"
        print(f"Обработка страницы {page_num}...")

        soup = fetch_page(url)
        if not soup:
            continue

        page_data = parse_prices(soup)
        all_data.update(page_data)

    return all_data


def main():
    base_url = "https://metallstroyplus.ru/profnastil/"
    total_pages = 206  # Укажите реальное количество страниц

    all_data = get_all_pages_data(base_url, total_pages)

    # Создание DataFrame
    df = pd.DataFrame.from_dict(all_data, orient='index', columns=['Цена'])

    # Сохранение в Excel
    df.to_excel('metallstroyplus.xlsx', index_label='Название товара')
    print("Данные успешно сохранены в grandline.xlsx")
    print(df.head())


if __name__ == "__main__":
    main()
