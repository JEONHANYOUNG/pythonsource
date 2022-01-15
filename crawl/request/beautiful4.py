# pip install beautifulsoup4
# beautifulsoup : 파싱
# 크롤링 : requests + beautifulsoup 선호

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.v.daum.net/v/20220104102035295")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# 기자명
# writer = soup.find("span", class_="txt_info")
writer = soup.select_one("span.txt_info")
print(writer.string)

# 기사 작성 시간
# date_time = soup.find("span", class_="num_date")
date_time = soup.select_one("span.num_date")
print(date_time.string)

# 기사의 첫 번째 문단
# para1 = soup.find("p", attrs={"dmcf-pid": "E1x75MaNSt"})

# harmonyContainer > section > p:nth-child(1)
para1 = soup.select_one("#harmonyContainer > section > p:nth-child(1)")
print(para1.string)
