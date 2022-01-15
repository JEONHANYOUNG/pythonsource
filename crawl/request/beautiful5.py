# gmarket.co.kr 전체 카테고리
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.gmarket.co.kr/")
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")

# 전체 카테고리 추출 : find_all()
# one_depth = soup.find_all("a", class_="link__1depth-item")
# # print(one_depth)
# for item in one_depth:
#     print(item.string)

# 2차 카테고리 추출
item__2depth = soup.find_all("li", class_="list-item__2depth")
# print(item__2depth)
for item in item__2depth:
    link1 = item.find("a")["href"]  # 2차 카테고리 주소 추출
    print(item.string, link1)
