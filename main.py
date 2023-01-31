import requests as r
from bs4 import BeautifulSoup


# Обработка стартовой страницы
url = "https://gdz-shok.ru"

response = r.get(url).text
soup = BeautifulSoup(response, "lxml")
datas = soup.find_all("div", class_="td")


# Сохранение промежуточных запросов в файлы json для проверки. Сами файлы потом нигде не используются
with open("soup.json", "w") as file:
    file.write(str(soup))

with open("datas.json", "w") as file:
    file.write(str(datas))


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


# Убираем дублирующиеся элементы, из-за их дублирования в html
data_list_2 = []

for data in data_list:
    if data not in data_list_2:
        data_list_2.append(data)

data_list = data_list_2
"""
for data in data_list:
    print(data)
"""

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
books = books_2

print(books)
