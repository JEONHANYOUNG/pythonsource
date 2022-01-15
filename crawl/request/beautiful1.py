# pip install beautifulsoup4
# beautifulsoup : 파싱
# 크롤링 : requests + beautifulsoup 선호

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.v.daum.net/v/20220104102035295")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# print(soup.head)  # <head> ~ <head>
# print(soup.title)  # <title> ~ <title>
# print(soup.title.string)  # <title> ~ <title> 태그 안의 내용
# print(soup.title.get_text())  # <title> ~ <title> 태그 안의 내용
print(soup.p)
