import requests as r
from bs4 import BeautifulSoup


# Обработка стартовой страницы
url = "https://gdz-shok.ru/gdz/klass_1/russki_yazik/"

response = r.get(url).text
soup = BeautifulSoup(response, "lxml")
datas = soup.find_all("div", class_="book")



# Сохранение промежуточных запросов в файлы json для проверки. Сами файлы потом нигде не используются
with open("test_2.json", "w") as file:
    file.write(str(datas))
