# openpyxl 라이브러리 사용법

# 엑셀 실행 => 워크북 생성 => 저장
from openpyxl import Workbook

wb = Workbook()  # 새 워크북 생성
ws = wb.active  # 현재 가지고 있는 시트를 활성화

ws.title = "월말결산"

wb.save("./sample.xlsx")
wb.close()
