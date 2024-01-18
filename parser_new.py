import csv

import requests
from bs4 import BeautifulSoup

url = 'https://1c.ru/rus/partners/franch-citylist.jsp?reg=&city=&partnerName=&is_map_open=0&mark=true&pageNumber_inp=1#map_ancor/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
parse_element = soup.findAll('table', class_='table table-striped nospace')
title_link = []
link = []

for page in parse_element:
    product_name = page.find('h3', _class='grid-item')
    # product_url = page.find('a', class_='').get('href')
    title_link.append(product_name)
    # link.append(product_url)

with open("parse.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow('title')
spisok = [title_link]

for result in spisok:
    with open("parse.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(result)
