from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


# 크롬 드라이버 로드
driver = webdriver.Chrome("d:\\chromedriver\\chromedriver.exe")

# 원하는 url 로 접속
driver.get("https://www.daum.net")

element = driver.find_element(By.NAME, "q")
element.send_keys("아이유")
element.send_keys(Keys.ENTER)

# 뉴스기사 타이틀 출력
titles = driver.find_elements(By.CSS_SELECTOR, "#container  li  a.tit_main")
for title in titles:
    print(title.text)

time.sleep(3)
driver.close()
