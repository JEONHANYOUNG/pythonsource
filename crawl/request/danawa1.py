# 로그인을 한 후 접근이 가능한 페이지 크롤링
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 로그인할 때 필요한 formData
login_info = {
    "redirectUrl": "http://www.danawa.com/",
    "loginMemberType": "general",
    "id": "pjky5",
    "isSaveId": "true",
    "password": "12344321@a",
}

# headers
headers = {
    "user-agent": UserAgent().chrome,
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F",
}

with requests.Session() as s:
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)
    # print(res.text)

    res = s.get("https://buyer.danawa.com/order/Order/orderList", headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    # 아이디 출력
    user_id = soup.select_one("p.user")
    print(user_id.text)

    if user_id is None:
        raise Exception("Login 실패")

    # 주문/배송조회
    info_list = soup.select("div.sub_info > ul.info_list > li")

    print("**** 나의 쇼핑 내역 ****")
    for item in info_list:
        proc, val = item.find("span").string.strip(), item.find("strong").string.strip()
        print(proc, val)
