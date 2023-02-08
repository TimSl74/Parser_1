import requests as r
from bs4 import BeautifulSoup
import re

print("control point 1")

# Обработка стартовой страницы
url = "https://gdz-shok.ru"

response = r.get(url).text
soup = BeautifulSoup(response, "lxml")
datas = soup.find_all("div", class_="td")

# Сохранение промежуточных запросов в файлы json для проверки. Сами файлы потом нигде не используются
"""
with open("soup.json", "w") as file:
    file.write(str(soup))

with open("datas.json", "w") as file:
    file.write(str(datas))
"""

# Поиск локальных ссылок на страницы по предметам
data_list = []

for data in datas:
    try:
        url_2 = data.find("a").get("href")
        if url_2 != "#":
            if len(url_2) > 14:
                # 14 - длина строки url_2, в которой нет ссылки на предмет, только на класс
                data_list.append(f"{url}{url_2}")
            else:
                pass
        else:
            pass
    except:
        pass
print("control point 2")

# Убираем дублирующиеся элементы, из-за их дублирования в html
data_list_2 = []

for data in data_list:
    if data not in data_list_2:
        data_list_2.append(data)

data_list = data_list_2

print("control point 3")
# Перебираем ссылки из data_list и получаем новые ссылки по предметам
n = 0
books = []
while n < len(data_list)-1:
    response = r.get(data_list[n]).text
    # print(data_list[n])
    soup = BeautifulSoup(response, "lxml")
    datas_book = soup.find("div", class_="book")
    for book in datas_book:
        url_book = datas_book.find("a").get("href")
        books.append(url_book)
    n += 1

# Убираем дубликаты
books_2 = []
for book in books:
    if book not in books_2:
        books_2.append(book)
books = books_2

# Добавляем адрес домашней страницы к локальным ссылкам
books_2 = []
for book in books:
    books_2.append(f"{url}{book}")
url_books = books_2
print("control point 4")
"""
print(url_books)
"""
# Перебираем книги, чтобы получить адрес каждой страницы в книге
pages = []
logs = []
for book in url_books:
    response = r.get(book).text
    soup = BeautifulSoup(response, "lxml")
    datas_page = soup.find_all("ul", class_="numbers")

    url_pages = []
    with open("test_2.json", "w") as file:
        file.write(str(datas_page))
    with open("test_2.json", "r") as file:
        for word in file:
            # Поиск локальной ссылки, заключённой между кавычек.
            # Перебрать как ранее через find или find_all не получается
            url_pages.append(' '.join(re.findall(r'\"([^""]+)\"', word)))

    n = 0
    try:
        while n < len(url_pages):
            if 1 < len(str(url_pages[n])) and url_pages[n] != "numbers" and url_pages[n] != "long_numbers":
                pages.append(f"{str(book)}{url_pages[n]}")
            n += 1
    except:
        logs.append(str(url_pages[n]))
"""
with open("pages.json", "w") as file:
    file.write(str(pages))
"""
with open("logs.json", "w") as file:
    file.write(str(logs))

print("control point 5")
data_jpg = []
for page in pages:
    response = r.get(page).text
    soup = BeautifulSoup(response, "lxml")
    jpg_datas = soup.find("div", class_="ex")
    url_jpg = jpg_datas.find("img").get("src")
    data_jpg.append(f"{str(url_jpg)}")
    print(f'"{page}"')

print(data_jpg)
print("control point 6")
for jpg in data_jpg:
    name = f'{str(jpg.replace("/", "_"))}.jpg'
    line = f"/Users/macbook/PycharmProjects/Parser_1/{name}"
    with open(fr"{line}", "wb") as file:
        response = r.get(f"{url}{jpg}")
        file.write(response.content)
        print("done")
print("control point 7")
