# train.xlsx 정규표현식 적용

from openpyxl import load_workbook
import re

# 엑셀파일 로드
wb = load_workbook("./crawl/regex/train.xlsx")

# sheet 활성화
ws1 = wb.active

# 정규식
pattern = re.compile(" Mr\.")

# Name 성별
for each_row in ws1.rows:
    if len(pattern.findall(each_row[3].value)) > 0:
        print(each_row[3].value)

wb.close()
