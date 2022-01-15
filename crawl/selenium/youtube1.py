# youtube에서 검색어 넣고 타이틀 가져오기
# selenium 만 사용
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# 크롬 드라이버 로드
driver = webdriver.Chrome("d:\\chromedriver\\chromedriver.exe")

# 원하는 url 로 접속
driver.get("https://www.youtube.com/")

time.sleep(2)

element = driver.find_element(By.NAME, "search_query")
element.send_keys("아이유")
element.send_keys(Keys.ENTER)

time.sleep(2)

# 검색결과 페이지에서 타이틀 가져오기
titles = driver.find_elements(By.TAG_NAME, "h3")
for title in titles:
    print(title.text)


time.sleep(3)
driver.close()
