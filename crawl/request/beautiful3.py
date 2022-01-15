from bs4 import BeautifulSoup

with open("./crawl/request/exam.html", "r") as f1:
    html = f1.read()

soup = BeautifulSoup(html, "html.parser")

# 이쁘게 출력
# print(soup.prettify())

# 파싱
# 태그로 찾기
# print("-- 태그로 찾기 --")
# print("title >> {}".format(soup.title))
# print("title 내용 >> {}".format(soup.title.string))
# print("title 태그의 부모 태그 >> {}".format(soup.title.parent))

# p1 = soup.p
# print("p >> {}".format(p1))
# print("p 내용 >> {}".format(p1.string))
# print("p 내용 >> {}".format(p1.get_text()))
# print("p 클래스 값 >> {}".format(p1["class"]))


# find() - 태그 + attr
# title = soup.find("title")
# print("title >> {}".format(title))
# print("title 내용 >> {}".format(title.string))
# print("title 태그의 부모 태그 >> {}".format(title.find_parent("head")))


# p1 = soup.find("p")
# print("p >> {}".format(p1))
# print("p 내용 >> {}".format(p1.string))
# print("p 내용 >> {}".format(p1.get_text()))
# print("p 클래스 값 >> {}".format(p1["class"]))


# p2 = soup.find("p", class_="story")
# print("p >> {}".format(p2))
# print("p 내용 >> {}".format(p2.get_text()))


# a1 = soup.find("a")
# print(a1.prettify())

# a2 = soup.find("a", id="link2")
# print(a2.prettify())
# print(a2.string)
# print(a2["href"])

# a3 = soup.find("a", {"class": "sister", "data-io": "link"})
# print(a3.prettify())
# print(a3.string)
# print(a3["href"])


# find_all() : 결과를 리스트로 형태로 처리/여러개의 동일한 태그 찾아오기
# a = soup.find_all("a")
# a = soup.find_all("a", limit=2)
# a = soup.find_all("a", class_="sister")
a = soup.find_all("a", string=["Lacie"])
print(a)
