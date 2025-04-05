from bs4 import BeautifulSoup
import requests
url = 'https://vc.ru/u/1441213-dizayn-interera-houzzy/777384-top-60-saytov-o-dizayne-interera-2023-2024-luchshie-sayty-studii-dizayna-interera-zhurnaly-dlya-interera-programmy#01'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# title = soup.findAll('div', class_='info')
# div_price = soup.findAll("div", class_="l-island-a")
#
#
# result_list = []
# for a in div_price:
#     result_list.append(a.find('a', class_ = "").get_href()) # link
#     result_list.append("\n")

# all_page = 24
# for i in range(all_page):
#     url_page_next = "https://axop.su/mebel_dlya_vannoy/caprigo/page_" + str(i+1) + "/"
#     for a, b, c in zip(title, div_prise, url_product):
#         result_list.append(a.find('a', class_="product-name").get_text())
#         result_list.append(b.find('span', class_="price product-price").get_text())
#         result_list.append(c.find('a').get('href'))
#         result_list.append("\n")

# with open('disign.txt', 'w', encoding="utf-8") as data_file:
#     for x in result_list:
#         data_file.write(x)
