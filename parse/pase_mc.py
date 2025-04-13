import requests
from bs4 import BeautifulSoup

url = 'https://mc.ru/price/msk'
response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
my_divs = soup.find_all("div")
response = requests.get(url)
file_Path = 'research_Paper_1.pdf'

if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
else:
    print('Failed to download file')