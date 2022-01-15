import requests

# json 데이터 처리

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1641260036877"

with requests.Session() as s:
    r = s.get(url)
    # print(r.text)
    # print(r.json())
    for i, item in enumerate(r.json(), 1):
        print(i, item["product_name"])
