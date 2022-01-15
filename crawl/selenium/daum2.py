from selenium import webdriver
from selenium import common
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


import time


options = webdriver.ChromeOptions()

# headless를 입력해주면 브라우저를 띄우지 않고 실행 가능
options.headless = True

# driver = webdriver.Chrome("c:\\chromedriver\\chromedriver", options=options)

driver = webdriver.Chrome("c:\\chromedriver\\chromedriver")

driver.get("https://news.v.daum.net/v/20220111085135792")

# print(driver.page_source)

# contents = driver.find_element(By.ID, "harmonyContainer")
# print(contents.text)

# 댓글 가져오기
loop, count = True, 0

while loop and count < 10:
    try:
        # 더보기 버튼 기다리기
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alex_more > button"))
        )
        # 더보기 버튼 클릭
        element.click()
        count += 1

        # 댓글 내용 가져오기 위한 시간 주기
        time.sleep(2)
    except TimeoutException:
        loop = False


# 현재 댓글 가져오기
comment_list = driver.find_elements(By.CSS_SELECTOR, ".list_comment li")

for idx, comment in enumerate(comment_list, 1):
    print("[{}] : {}".format(idx, comment.find_element(By.CSS_SELECTOR, "div p").text))

time.sleep(3)
driver.close()
