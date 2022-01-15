import requests
from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
# num
# isbn
ws1.column_dimensions["B"].width = 30
# title
ws1.column_dimensions["C"].width = 100
# price
ws1.column_dimensions["D"].width = 15
# discount
ws1.column_dimensions["E"].width = 15


# 제목 행 삽입
ws1.append(["num", "isbn", "title", "price", "discount"])
# 시트 명 지정
ws1.title = "베르나르 베르베르"

# 네이버 인증키
headers = {
    "X-Naver-Client-Id": "jEN4YNR9yf1PMfHNopcy",
    "X-Naver-Client-Secret": "KfcO7NQ7wH",
}

url = "https://openapi.naver.com/v1/search/book.json"
start, num = 1, 0
for idx in range(4):

    start_num = start + (idx * 100)

    # parameter
    param = {
        "query": "베르나르 베르베르",
        "display": "100",
        "start": start_num,
        "sort": "count",
    }

    res = requests.get(url, headers=headers, params=param)

    data = res.json()

    for item in data["items"]:
        num += 1
        print(num, item["isbn"], item["title"], item["price"], item["discount"])
        ws1.append([num, item["isbn"], item["title"], item["price"], item["discount"]])


wb.save("베르나르.xlsx")
wb.close()
