from selenium import webdriver
import time

driver = webdriver.Chrome("d:\\chromedriver\\chromedriver")

driver.get("https://www.daum.net")

print("title", driver.title)
print("url", driver.current_url)
print("session", driver.session_id)


time.sleep(3)

driver.close()
