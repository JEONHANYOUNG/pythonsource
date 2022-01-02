import urllib.request as req
from fake_useragent import UserAgent

naver_news = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=056&aid=0011185842"
userAgent = UserAgent()
headers = {"user-agent": userAgent.random}

try:
    request_url = req.Request(naver_news)
    response = req.urlopen(request_url).read().decode("euc-kr")
except Exception as e:
    print(e)  # ('Host', 'news.naver.com')
else:
    print(request_url.header_items())  # ('User-agent', 'Python-urllib/3.10')
    print(response[:4000])
