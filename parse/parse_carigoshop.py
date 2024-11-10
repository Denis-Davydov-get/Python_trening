from bs4 import BeautifulSoup
import requests
import csv
url = 'https://www.caprigoshop.ru/278-unitazy'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.findAll('div', class_='right-block')
# div_price = soup.findAll('div', class_='content_price')
# url_product = soup.findAll('div', class_='right-block')

result_list = []
# for a, b, c in zip(title, div_price, url_product):
for i in title:
    result_list.append(i.find('a', class_ = "product-name").get_text())
    # result_list.append(b.find('span', class_ = "price product-price").get_text())
    # result_list.append(c.find('a', class_ = "product-name").get('href'))
    # result_list.append("\n")

# all_page = 4
# for i in range(all_page):
#     url_page_next = url + "#/page-" + str(i+1)
#     # for a, b, c in zip(title, div_prise, url_product):
#     for a in title:
#         result_list.append(a.find('a', class_="product-name").get_text())
#         # result_list.append(b.find('span', class_="price product-price").get_text())
#         # result_list.append(c.find('a', class_="product-name").get('href'))
#         result_list.append("\n")

with open('unitazy.txt', 'w', encoding="utf-8") as data_file:
    result_list = set(result_list)
    for x in result_list:
        data_file.write(x)
        data_file.write("\n")
