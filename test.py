import requests as r
from bs4 import BeautifulSoup


url = "https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/"

response = r.get(url).text
soup = BeautifulSoup(response, "lxml")
datas_page = soup.find("ul", class_="numbers")
"""
print(datas_page)
"""

pages = []

i = 0
while i <= len(datas_page):
    number_page = page.find("a").get("href")
    pages.append(number_page)
    i += 1

print(pages)
"""
with open("test_2.json", "w") as file:
    file.write(str(pages))
"""
# Переписать всё нахрен