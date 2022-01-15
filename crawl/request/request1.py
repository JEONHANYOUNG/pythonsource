# requests 라이브러리 사용
# 설치 : pip install requests
# requests 기능 - get,post,put,patch,delete 지원
#                 세션 지원/쿠키 지원/json 지원/디코딩 적절하게 지원

import requests

# 세션 연결
s = requests.Session()
# get 방식
r = s.get("https://www.naver.com")

print("OK ? : {}".format(r.ok))
print(r.text)  # r.content(binary 형태의 응답)

# 세션 종료
s.close()
