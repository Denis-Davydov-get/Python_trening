import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_avg_price_from_mc(url: str) -> dict:
    try:
        # Отправляем запрос с заголовками для имитации браузера
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на успешность запроса

        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим все элементы с ценами и названиями
        list_all_sku_name = soup.find_all("div", attrs={"class": 'refstr _nm'})
        list_all_sku_price = soup.find_all("div", attrs={"class": 'pr'})

        # Проверяем, что списки одинаковой длины
        if len(list_all_sku_name) != len(list_all_sku_price):
            raise ValueError("Количество названий и цен не совпадает")

        # Создаем словарь с очищенными данными
        dict_sku_done = {}
        for name, price in zip(list_all_sku_name, list_all_sku_price):
            clean_name = name.get_text(strip=True)
            clean_price = price.get_text(strip=True)

            # Добавляем проверку на пустые значения
            if clean_name and clean_price:
                dict_sku_done[clean_name] = clean_price

        return dict_sku_done

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return {}
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return {}


# Получение данных
url = "https://mc.ru/metalloprokat/stal_listovaya_g_k/Page200/2"
data_dict = get_avg_price_from_mc(url)

# Создание DataFrame
try:
    # Преобразуем словарь в DataFrame
    df = pd.DataFrame(list(data_dict.items()), columns=['Наименование', 'Цена'])

    # Обрабатываем NaN значения
    df['Цена'] = df['Цена'].replace('', 0).astype(float)

    # Сохраняем в CSV
    df.to_csv('output.csv', index=False, encoding='utf-8-sig')
    print("Данные успешно сохранены в output.csv")

except Exception as e:
    print(f"Ошибка при обработке данных: {e}")
