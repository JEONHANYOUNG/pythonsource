import urllib.request as req

encar_url = "http://www.encar.com/index.do"

# urlopen() 을 통해서 얻을 수 있는 정보

try:
    response = req.urlopen(encar_url)

    print("type {}".format(type(response)))  
    print("geturl {}".format(response.geturl()))
    print("status {}".format(response.status))
    print("header {}".format(response.getheaders()))
    print("getcode {}".format(response.getcode()))

    contents = response.read().decode("euc-kr")

except Exception as e:
    print(e)
else:
    print(contents[:4000])
