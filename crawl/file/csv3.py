# python에서 csv 파일 처리
# csv(comma separated values) : 몇 가지 필드를 쉼표로 구분한 텍스트 데이터

import csv

with open("./sample2.csv", "r") as f:
    # dict 구조로 읽어올 경우
    reader = csv.DictReader(f, delimiter="|")

    # print(reader)
    # print(type(reader))
    # print(dir(reader))

    # 헤더명 제거
    next(reader)

    for item in reader:
        print(item)
