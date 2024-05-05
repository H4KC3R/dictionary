from bs4 import BeautifulSoup
import requests

word = "wireless"
url = f"https://www.multitran.com/m.exe?l1=1&l2=2&s={word}"
response = requests.get(url)
html_content = response.text

# Создание объекта Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Поиск элемента <body> с определенным стилем
body = soup.body
container = body.find('div', class_='container')
mclass_elements = container.find_all(class_='mclass160_10')[2]
first_table = mclass_elements.find('table')

print(first_table)
