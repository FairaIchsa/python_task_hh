# Получить с русской википедии список всех животных (https://inlnk.ru/jElywR)
# и вывести количество животных на каждую букву алфавита
import requests
from bs4 import BeautifulSoup

# может выполняться около минуты

prefix = 'https://ru.wikipedia.org'
url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'    # первая страница

dictionary = {}

while url is not None:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='html.parser')

    content = soup.find('div', id='mw-pages')
    groups = content.findAll('div', {'class': 'mw-category-group'})
    for group in groups:
        letter = group.find('h3').text
        count = len(group.findAll('li'))
        if letter not in dictionary:
            dictionary[letter] = count
        else:
            dictionary[letter] += count

    url = content.find('a', text='Следующая страница')
    if url is not None:
        url = prefix + url['href']

for key, val in dictionary.items():
    print(f"{key}: {val}")
