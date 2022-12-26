import requests as r
from bs4 import BeautifulSoup

url = "https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.3/"

response = r.get(url)

soup = BeautifulSoup(response.text, "lxml")
data = soup.find("div", class_="ex")
pic = data.find("img", class_="ex").get("src")

print(data, "\n")
print(pic)

with open("soup.json", "w") as file:
    file.write(soup.text)
