from selenium import webdriver
import time

# 크롬 드라이버 로드
driver = webdriver.Chrome("d:\\chromedriver\\chromedriver.exe")

# 원하는 url 로 접속
driver.get("http://python.org")


# 화면크기 제어
driver.maximize_window()


# 소스 가져오기
print(driver.page_source)


time.sleep(3)
# 드라이버 종료
driver.close()
