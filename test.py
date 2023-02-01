import requests as r
from bs4 import BeautifulSoup
import re

url = "https://gdz-shok.ru/gdz/klass_2/matematika/moro_uchebnik/"

response = r.get(url).text
soup = BeautifulSoup(response, "lxml")
datas_page = soup.find_all("ul", class_="numbers")


"""
pages = []
for data in datas_page:
    datas_page_2 = data.find("a").get("href")
    pages.append(datas_page_2)

print(pages)
"""

url_pages = []
with open("test_2.json", "w") as file:
    file.write(str(datas_page))
with open("test_2.json", "r") as file:
    for word in file:
        url_pages.append(' '.join(re.findall(r'\"([^""]+)\"', word)))

print(url_pages)
n = 0
pages = []
while n < len(url_pages):
    if 1 < len(str(url_pages[n])) and url_pages[n] != "numbers":
        pages.append(url_pages[n])
    n += 1

with open("pages.json", "w") as file:
    file.write(str(pages))


import requests #импортируем модуль
f = open(r'D:\file_bdseo.zip',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("http://site.ru/file.zip") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()
