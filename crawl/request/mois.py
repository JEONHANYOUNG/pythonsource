# 행정안전부 rss 가져오기
import requests

# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001
url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# print(params)  # [{'ctxCd': 1001}, {'ctxCd': 1012}, {'ctxCd': 1013}, {'ctxCd': 1014}]

with requests.Session() as s:
    for param in params:
        r = s.get(url, params=param)
        print("-" * 100)
        print(r.text)
