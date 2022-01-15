# clien 팁과 강좌 1 ~ 5 page 크롤링/제목,날짜 저장
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

# https://www.clien.net/service/board/lecture
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=1(2page)
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=2
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=4(5page)


for page_num in range(5):
    if page_num == 0:  # 첫페이지
        res = requests.get("https://www.clien.net/service/board/lecture")
    else:
        res = requests.get(
            "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
            + str(page_num)
        )

    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.select("div.list_title > a.list_subject > span.subject_fixed")
    # #div_content > div:nth-child(4) > div.list_time > span > span
    # #div_content > div:nth-child(4) > div.list_time > span
    times = soup.select("div.list_time > span")

    # for time in times:
    #     print(time.text.strip()[:5])

    for idx, title in enumerate(titles):
        print(title.text.strip(), times[idx].text.strip()[:5])
        ws1.append([title.text.strip(), times[idx].text.strip()[:5]])

wb.save("clien2.xlsx")
wb.close()
