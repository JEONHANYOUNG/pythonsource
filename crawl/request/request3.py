import requests
from fake_useragent import UserAgent

# header 정보 보내기

# userAgent = UserAgent()
# userAgent.random, userAgent.chrome

headers = {"user-agent": UserAgent().chrome}

s = requests.Session()

r = s.get("http://httpbin.org", headers=headers)
print(r.text)

s.close()
