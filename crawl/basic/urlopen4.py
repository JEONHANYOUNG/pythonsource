import urllib.request as req

daumnews_url = "https://news.v.daum.net/v/20211231093441154"

# urlopen 을 통해서 얻을 수 있는 정보

try:
    response = req.urlopen(daumnews_url).read().decode("utf-8")
except Exception as e:
    print(e)
else:
    print(response)
