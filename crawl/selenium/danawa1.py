# danawa 사이트 로그인
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# 크롬 드라이버 로드
driver = webdriver.Chrome("d:\\chromedriver\\chromedriver.exe")

# 다나와 사이트 접속
driver.get("http://www.danawa.com/")

driver.maximize_window()
time.sleep(1)

# 로그인 클릭
driver.find_element(By.CLASS_NAME, "btn_user.btn_user--login").click()

# 아이디, 비밀번호 입력 후 로그인 버튼 클릭
# 아이디 태그 찾기
user_id = driver.find_element(By.ID, "danawa-member-login-input-id")
# 아이디 입력하기 전 input clear
user_id.clear()
# 아이디 입력
user_id.send_keys("본인 아이디")

# 비밀번호 태그 찾기
password = driver.find_element(By.ID, "danawa-member-login-input-pwd")
password.clear()
# 비밀번호 입력
password.send_keys("본인비밀번호")
# 비밀번호 입력 후 엔터
password.send_keys(Keys.ENTER)


time.sleep(3)
# 드라이버 종료
driver.close()
