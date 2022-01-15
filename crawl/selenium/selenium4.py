from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome("d:\\chromedriver\\chromedriver")

driver.get("https://www.naver.com/")

element = driver.find_element(By.NAME, "query")

element.send_keys("안드로이드")
element.send_keys(Keys.ENTER)


time.sleep(3)
driver.close()
