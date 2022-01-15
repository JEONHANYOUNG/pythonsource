import urllib.request as req
from fake_useragent import UserAgent

naver_news = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=022&aid=0003652695"
userAgent = UserAgent()
headers = {"user-agent": userAgent.random}

try:
    request_url = req.Request(naver_news, headers=headers)
    response = req.urlopen(request_url).read().decode("euc-kr")
except Exception as e:
    print(e)
else:
    print(request_url.header_items())
    print(response[:4000])
