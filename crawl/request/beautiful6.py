# find(), find_all() : 태그 + 속성으로 element 찾기 찾기
# select_one(), select() : css 선택자로 element 찾기
#                        : 태그, 아이디, 클래스명, 자식, 자손, 형제....


from bs4 import BeautifulSoup

with open("./crawl/request/exam.html", "r") as f1:
    html = f1.read()

soup = BeautifulSoup(html, "html.parser")

# p1 = soup.select_one("p")
# print(p1)

# b = soup.select_one("p.title > b")
# print(b)
# print(b.string)
# print(b.text)

# link1 = soup.select_one("#link1")  # soup.find("a",id="link1")
# print(link1)
# print(link1.text)

# link3 = soup.select_one("a[data-io='link']")
# print(link3)
# print(link3.text)

# select() : 여러개 한꺼번에 가져오기
# a_list = soup.select("a")
# a_list = soup.select("p.story > a")
# # print(a_list)
# for link in a_list:
#     print(link.string)

link1 = soup.select("p.story > a:nth-child(2)")
print(link1)
