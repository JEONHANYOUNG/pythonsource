import requests
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/서울_지하철"

try:

    with requests.Session() as s:
        res = s.get(url)

        soup = BeautifulSoup(res.text, "html.parser")
except Exception as e:
    print(e)
else:
    img1 = soup.select_one(
        "#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img"
    )
    # print(img1)
    print("src : ", img1["src"])

    # #mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img
    img2 = soup.select_one("#mw-content-text  div.thumb.tright  a > img")
    print("src : ", img2["src"])

    links = soup.select("a")
    # a 태그는 몇 개?
    print("a 태그 개수 : ", len(links))

    # 이미지 저장
    downlad = s.get("https:" + img1["src"])

    with open("./subway.jpg", "wb") as f:
        f.write(downlad.content)
