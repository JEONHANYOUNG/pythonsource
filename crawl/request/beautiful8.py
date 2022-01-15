import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user_agent = UserAgent()
headers = {"user-agent": user_agent.chrome}

res = requests.get("https://finance.naver.com/", headers=headers)
# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")

# 데이터 추출
# 인기 검색 종목 출력(종목명, 가격)

# #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > th > a
pop_list = soup.select("div.aside_popular > table > tbody > tr")
# print(pop_list)
for item in pop_list:
    # 종목명
    stock_name = item.find("a").string
    # 현재금액
    stock_price = item.find("td").string
    print(stock_name, stock_price)
