import os
import datetime
import locale
from bs4 import BeautifulSoup
import requests
import re
import shutil
import time


def today_directory():
    locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
    today = datetime.datetime.now()
    today_str = today.strftime('%Y%m%d')

    if not os.path.exists(f"{today_str}"):
        os.mkdir(f"{today_str}")
    else:
        print("ディレクトリはすでに存在します")

    return today_str


def make_html(urls, direcrory):
    time.sleep(1)

    response = requests.get(urls)
    response.encoding = 'utf-8'

    file_name = re.search("sample\w+", urls)

    file_path = f"{direcrory}/{file_name[0]}.html"

    if not os.path.exists(file_path):
        with open(f"{file_name[0]}.html", "w", encoding="utf-8") as f:
            print(response.text, file=f)
            print(f"make {file_name[0]}.html")

        shutil.move(f"{file_name[0]}.html", f"{direcrory}")
    else:
        print("ファイルはすでに存在します")

    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a'):
        if a_tag.get('href'):
            make_html(a_tag.get('href'), direcrory)


url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'

direcrory_name = today_directory()
make_html(url, direcrory_name)
