import requests
from bs4 import BeautifulSoup
def parse (url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    find_tag_strong = soup.findAll('div', class_ = "col-sm-12 factory-title")
    print(find_tag_strong)
url = input("Введите страницу которую надо спарсить - ")

parse(url)