import urllib.request as req

naver_news = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=022&aid=0003652695"

try:
    request_url = req.Request(naver_news)
    response = req.urlopen(request_url).read().decode("euc-kr")
except Exception as e:
    print(e)
else:
    print(request_url.header_items())  # ('User-agent', 'Python-urllib/3.10')
    print(response[:4000])
