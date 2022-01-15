from selenium import webdriver
import time

# 크롬 드라이버 로드
chrome_driver = "c:\\chromedriver\\chromedriver.exe"

# 옵션을 설정 -- 브라우저 띄우지 않기
headless_options = webdriver.ChromeOptions()
headless_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_driver, options=headless_options)

# 원하는 url 로 접속
driver.get("http:/python.org")

# 소스 가져오기
print(driver.page_source)


time.sleep(3)
# 드라이버 종료
driver.close()
