from bs4 import BeautifulSoup
import requests
import csv
url = 'https://www.caprigoshop.ru/133-rasprodazha'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.findAll('div', class_='product-container')


result_list = []
for a in title:
    result_list.append(a.find('a', class_ = "product-name").get_text())
    result_list.append(";")
    result_list.append(a.find('span', class_ = "price product-price").get_text())
    result_list.append(";")
    result_list.append(a.find('span', class_ = "old-price product-price").get_text())
    result_list.append(";")
    result_list.append(a.find('a', class_ = "product-name").get('href'))
    result_list.append(";")
    # result_list.append(a.find('img', class_ = "replace-2x img-responsive lazyloaded").get('src'))
    result_list.append("\n")

# all_page = 2
# for i in range(all_page):
#     url_page_next = "https://www.caprigoshop.ru/82-katalog-mebeli-dlya-vannoj-komnaty#/page-" + str(i+1)
#     for a, b, c in zip(title, div_prise, url_product):
#         result_list.append(a.find('a', class_="product-name").get_text())
#         result_list.append(b.find('span', class_="price product-price").get_text())
#         result_list.append(c.find('a', class_="product-name").get('href'))
#         result_list.append("\n" (sep=";"))

with open('sale2.txt', 'w', encoding="utf-8") as data_file:
    for x in result_list:
        data_file.write(x)
