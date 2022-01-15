# clien 팁과 강좌 1page 크롤링
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 워크북 생성
wb = Workbook()
# 기본시트 활성화
ws1 = wb.active
# 타이틀 변경
ws1.title = "팁과강좌"
# 특정 셀의 너비 조절
ws1.column_dimensions["A"].width = 75


res = requests.get("https://www.clien.net/service/board/lecture")
soup = BeautifulSoup(res.text, "html.parser")

# print(soup.prettify())
#  #div_content > div.list_content > div:nth-child(4) > div.list_title > a.list_subject > span.subject_fixed
titles = soup.select("div.list_title > a.list_subject > span.subject_fixed")

for title in titles:
    # print(title.text.strip())
    # 엑셀 저장
    ws1.append([title.text.strip()])


wb.save("clien.xlsx")
wb.close()
