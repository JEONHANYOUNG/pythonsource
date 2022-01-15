# find_element
# 다음 사이트에 특정 검색어를 입력 후 결과 페이지 가져오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome("c:\\chromedriver\\chromedriver", options=options)

driver.get("https://www.daum.net")

# 원하는 요소 찾기 : find_~~~~~~()

# name 속성을 이용해서 찾기
# element = driver.find_element(By.NAME, "q")
element = driver.find_element_by_name("q")
print(element)

# send_keys() : 키보드 액션
# 검색어 넣기
element.send_keys("안드로이드")

# 엔터 넣기(Keys.RETURN, Keys.ENTER)
element.send_keys(Keys.RETURN)

# 페이지 가져오기
print(driver.page_source)

# 스크린 샷
driver.save_screenshot("c:\\android.png")

time.sleep(3)
driver.close()
