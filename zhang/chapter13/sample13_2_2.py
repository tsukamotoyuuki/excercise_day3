import requests

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_1_1.html'

response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)

print(f'status code:{response.status_code}')
print(f'header:{response.headers}')
print(f'URL:{response.url}')
print(response.content.decode("utf-8"))
