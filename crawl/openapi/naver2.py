# 1000개의 쇼핑 검색 결과 가져오기
# query : 검색을 원하는 문자열(필수)
# display : 검색결과 출력 건수
# start : 검색 시작 위치


# https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start=201

import requests
from openpyxl import Workbook
import re

wb = Workbook()

ws1 = wb.active
ws1.title = "아이폰 1000"

# 첫번째 행 지정(제목)
ws1.append(["순위", "상품명", "주소"])

# 열 너비 지정
ws1.column_dimensions["B"].width = 100
ws1.column_dimensions["C"].width = 80


headers = {
    "X-Naver-Client-Id": "jEN4YNR9yf1PMfHNopcy",
    "X-Naver-Client-Secret": "KfcO7NQ7wH",
}


start, num = 1, 0
for idx in range(10):
    start_num = start + (idx * 100)

    url = (
        "https://openapi.naver.com/v1/search/shop.json?query=아이폰&display=100&start="
        + str(start_num)
    )

    # print(url)

    res = requests.get(url, headers=headers)

    # # print(res.json())

    data = res.json()

    for item in data["items"]:
        num += 1
        title = re.sub("<.*?>", "", item["title"])
        print(title, item["link"])
        ws1.append([num, title, item["link"]])


wb.save("아이폰.xlsx")
wb.close()
