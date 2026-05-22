from bs4 import BeautifulSoup
import requests
import re
import csv


def make_html(urls, writer):

    response = requests.get(urls)
    response.encoding = 'utf-8'

    file_name = re.search("sample\w+", urls)

    soup = BeautifulSoup(response.text, 'html.parser')

    for a_tag in soup.find_all('a'):
        if not a_tag.get('href'):
            writer.writerow([f'{response.url}', a_tag.get("title")])
            print(f"write {file_name[0]}.html")
        else:
            print(a_tag.get('href'))
            make_html(a_tag.get('href'), writer)

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'

with open(f"title.csv", "a", encoding="utf-8") as f:
    writer = csv.writer(f)
    make_html(url, writer)
