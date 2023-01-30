import requests as r
from bs4 import BeautifulSoup

url = "https://gdz-shok.ru"

response = r.get(url).text
soup = BeautifulSoup(response, "lxml")

datas = soup.find_all("div", class_="td")

with open("soup.json", "w") as file:
    file.write(str(soup))

with open("datas.json", "w") as file:
    file.write(str(datas))

for data in datas:
    try:
        url_2 = data.find("a").get("href")
        if url_2 != "#":
            if len(url_2) > 14:  # 14 - длина строки url_2, в которой нет ссылки на предмет, только на класс
                print(f"{url}{url_2}")
            else:
                pass
        else:
            pass
    except:
        pass
# Вместо print нужно собирать все ссылки в список, который потом уже перебирать запросами
# В списке нужно убрать дублирующиейся ссылки, потому что ссылки на 1 класс дублируются
