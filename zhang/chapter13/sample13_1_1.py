import urllib.request

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_1_1.html'

with urllib.request.urlopen(url) as conn:
    data = conn.read()
    text = data.decode('utf-8')
    # https://developer.mozilla.org/ja/docs/Web/HTTP/Status
    print(f'status code:{conn.status}')
    print(f'header:{conn.headers}')
    print(f'URL:{conn.geturl()}')
    print(text)

