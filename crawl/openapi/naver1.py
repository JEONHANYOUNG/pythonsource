import requests
import re

headers = {
    "X-Naver-Client-Id": "jEN4YNR9yf1PMfHNopcy",
    "X-Naver-Client-Secret": "KfcO7NQ7wH",
}
res = requests.get(
    "https://openapi.naver.com/v1/search/shop.json?query=아이폰", headers=headers
)

# print(res.json())

data = res.json()

for item in data["items"]:

    title = re.sub("<.*?>", "", item["title"])
    print(title, item["link"])
