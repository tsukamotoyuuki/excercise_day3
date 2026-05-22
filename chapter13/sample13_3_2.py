import requests
from bs4 import BeautifulSoup

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'

# HTMLを取得
response = requests.get(url)
response.encoding = 'utf-8'

# BeautifulSoupを用いて取得したHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')
# HTMLに書かれたaタグ（要素）のテキストとリンク情報を取得
for a_tag in soup.find_all('a'):
    text = a_tag.string
    href = a_tag.get('href')
    print(f'{text}: {href}')



# https://bit.ly/3V6lr5c

