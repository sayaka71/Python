# This Python file uses the following encoding: utf-8
# beautifulsoup4
# 独学プログラマーのスクレイピング

import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.google.com")
print(site)
data = BeautifulSoup(site.text, "html.parser")
print(data.title) #タイトルを出力する
print(data.title.text) #タイトルタグの中身のみを出力する
print(data.find_all("a")) #すべての「a」タグを出力する
print(data.find(id="id_name")) #id属性「id_name」に一致するタグを出力する