# 다음 뉴스 가져오기
# https://news.v.daum.net/v/20211231092356859

import urllib.request as req

url = "https://news.v.daum.net/v/20211231092356859"

try:
    response = req.urlopen(url).read().decode("utf-8")
except Exception as e:
    print(e)
else:
    print(response)
