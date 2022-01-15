# 서울시 평생 학습 포털 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# 크롬 드라이버 로드
driver = webdriver.Chrome("d:\\chromedriver\\chromedriver.exe")

driver.get("https://sll.seoul.go.kr/main/MainView.do")
driver.maximize_window()
time.sleep(1)

# 돋보기 클릭
driver.find_element(By.CLASS_NAME, "ico.btn-top-search").click()
time.sleep(2)

# 검색어 입력
# driver.find_element(By.ID,"sgiSearch").send_keys("영어").send_keys(Keys.ENTER)

element = driver.find_element(By.ID, "sgiSearch")
element.send_keys("영어")
element.send_keys(Keys.ENTER)

# 결과가 보여지기를 기다림
time.sleep(2)

# 더 많은 결과보기 클릭
driver.find_element(By.CLASS_NAME, "btn-more-result").click()

# 결과페이지에서 온라인 강의 타이틀 출력
titles = driver.find_elements(By.CSS_SELECTOR, ".search-result-list > ul > li a")
# 수강신청기간 추출
rterms = driver.find_elements(By.CLASS_NAME, "rterm")


for idx, title in enumerate(titles):
    print("강좌명 : {}, 수강신청기간 : {}".format(title.text, rterms[idx].text))


time.sleep(3)
# 드라이버 종료
driver.close()
