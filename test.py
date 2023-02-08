import requests as r
from bs4 import BeautifulSoup

url = "https://gdz-shok.ru"
pages = [
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.3/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.4/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.5/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.6/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.7/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.8/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.9/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.10/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.11/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.12/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.13/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.14/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.15/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.16/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.17/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.18/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.19/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.20/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.21/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.22/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.23/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.24/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.25/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.26/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.27/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.28/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.29/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.30/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.31/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.32/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.33/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.34/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.35/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.36/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.37/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.38/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.39/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.40/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.41/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.42/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.43/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.44/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.45/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.46/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.47/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/1.48/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.3/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.4/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.5/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.6/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.7/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.8/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.9/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.10/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.11/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.12/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.13/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.14/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.15/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.16/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.17/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.18/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.19/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.20/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.21/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.22/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.23/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.24/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.25/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.26/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.27/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.28/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.29/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.30/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.31/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.32/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.33/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.34/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.35/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.36/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.37/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.38/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.39/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.40/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.41/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.42/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.43/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.44/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.45/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.46/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.47/",
"https://gdz-shok.ru/gdz/klass_1/matematika/moro_volkova/2.48/"]
data_jpg = []

for page in pages:
    response = r.get(page).text
    soup = BeautifulSoup(response, "lxml")
    jpg_datas = soup.find("div", class_="ex")
    url_jpg = jpg_datas.find("img").get("src")
    data_jpg.append(f"{str(url_jpg)}")
    print(f"control point 5.1 {page}")

    # Путь для macOS
    # line = f"/Users/macbook/PycharmProjects/Parser_1/Images/{name}"
    # Путь для Windows
    # line = f"C:/Users/Tayte/PycharmProjects/Parser_1/Images/{name}"
for jpg in data_jpg:
    name = f'{str(jpg.replace("/", "_"))}'
    line = f"/Users/macbook/PycharmProjects/Parser_1/Images/{name}"
    with open(fr"{line}", "wb") as file:
        response = r.get(f"{url}{jpg}")
        file.write(response.content)
        print(f"done{jpg}")
print("control point 7")

