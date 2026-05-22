import os
import datetime
import requests
from bs4 import BeautifulSoup

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'

# 获取 HTML
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

# 获取当前日期目录
now = datetime.datetime.now()
path = now.strftime("%Y%m%d")

def creat_dir():
    if os.path.exists(path):
        print("ディレクトリはすでに存在します。")
    else:
        os.mkdir(path)

creat_dir()

# 创建 txt 文件路径
file_path = os.path.join(path, "sample13_3_2.html")

# 打开文件（写入模式）
with open(file_path, "w", encoding="utf-8") as f:

    # 遍历首页所有链接
    for a_tag in soup.find_all('a'):
        text = a_tag.string
        href = a_tag.get('href')

        line = f"{text}: {href}"
        print(line)

        # 写入文件
        f.write(line + "\n")

        # 处理子页面
        if href:
            try:
                r = requests.get(href)
                r.encoding = 'utf-8'

                s = BeautifulSoup(r.text, 'html.parser')

                for t in s.find_all("a"):
                    text2 = t.string
                    href2 = t.get("href")

                    sub_line = f"  {text2} -> {href2}"
                    print(sub_line)

                    # 写入子页面链接
                    f.write(sub_line + "\n")

            except Exception as e:
                err_line = f"  访问失败: {href}"
                print(err_line)
                f.write(err_line + "\n")

print("已保存到:", file_path)