import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {"user-agent": UserAgent().chrome}

url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=003&aid=0010925360"
res = requests.get(url, headers=headers)
# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")
print(type(soup))  # <class 'bs4.BeautifulSoup'>

# find()
title = soup.find("h3", id="articleTitle")
print(title.get_text())
