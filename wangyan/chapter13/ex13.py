import requests
from bs4 import BeautifulSoup
import os
import datetime
import time

today = datetime.date.today()
folder = today.strftime("%Y%m%d")
os.makedirs(f"{folder}",exist_ok=True)

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
for a_tag in soup.find_all('a'):
    text = a_tag.string
    href = a_tag.get('href')
    print(f'{text}: {href}')

    r = requests.get(href)
    r.encoding = 'utf-8'
    sub_html = r.text



    name = url.split("/")[-1]

    save_path = os.path.join(folder, name)


    with open(save_path, "w", encoding="utf-8") as f:
        f.write(response.text)
        time.sleep(1)

