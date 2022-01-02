# 크롤링 주의 사항
# 각 사이트는 크롤링이 되는 정보와 되지 않는 정보를 명시하고 있음 => robots.txt
# 규칙 준수

import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]

file_name = "robots.txt"

for url in urls:
    print(url + file_name)
    robots = requests.get(url + file_name)
    print(robots.text)
