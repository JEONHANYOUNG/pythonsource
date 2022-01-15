import urllib.request as req
from fake_useragent import UserAgent
import json
import csv

userAgent = UserAgent()
headers = {"user-agent": userAgent.random, "referer": "https://finance.daum.net/"}

try:
    url = "https://finance.daum.net/api/search/ranks?limit=10"
    res = req.urlopen(req.Request(url, headers=headers)).read().decode("utf-8")
except Exception as e:
    print(e)
else:
    # print(res)
    # json.loads() : json 데이터를 python 객체(dict)로 변환
    rank_json = json.loads(res)["data"]
    # print(rank_json)
    data = []
    for item in rank_json:
        print(
            "순위 : {}, 금액 : {}, 회사명 : {}".format(
                item["rank"], item["tradePrice"], item["name"]
            )
        )
        # 파일 저장
        data.append(item)

        with open("./finance.txt", "a", encoding="utf-8") as f, open(
            "./stock.csv", "w", newline=""
        ) as f1:
            # txt 저장
            f.write(
                "순위 : {}, 금액 : {}, 회사명 : {}\n".format(
                    item["rank"], item["tradePrice"], item["name"]
                )
            )

            # csv 저장
            # for i in data:
            #     print(i)

            output = csv.writer(f1)
            # 제목행 저장
            output.writerow(data[0].keys())
            for row in data:
                output.writerow(row.values())
