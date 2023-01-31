import requests as r
from bs4 import BeautifulSoup


# Обработка стартовой страницы
url = "https://gdz-shok.ru"


response = r.get(url).text
soup = BeautifulSoup(response, "lxml")
datas = soup.find_all("div", class_="td")


# Сохранение промежуточных запросов в файлы json для проверки
with open("soup.json", "w") as file:
    file.write(str(soup))

with open("datas.json", "w") as file:
    file.write(str(datas))


data_list = []

for data in datas:
    try:
        url_2 = data.find("a").get("href")
        if url_2 != "#":
            if len(url_2) > 14:  # 14 - длина строки url_2, в которой нет ссылки на предмет, только на класс
                data_list.append(f"{url}{url_2}")
                # print(f"{url}{url_2}")
            else:
                pass
        else:
            pass
    except:
        pass


# Убираем дублирующиеся элементы
data_list_2 = []
for data in data_list:
    if data not in data_list_2:
        data_list_2.append(data)

data_list = data_list_2
"""
for data in data_list:
    print(data)
"""

# Перебираем ссылки из data_list
n = 0
while n < len(data_list)-1:
    response = r.get(data_list[n]).text
    soup = BeautifulSoup(response, "lxml")
    with open(f"{str((data_list[n])[24::]).replace('/','_')}.json", "w") as file:
        file.write(str(soup))
    n += 1

# Нужно настроить запрос по ссылкам в сохраняемых json файлах
