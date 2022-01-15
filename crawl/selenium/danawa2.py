from selenium import webdriver
from selenium import common
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()

# headless를 입력해주면 브라우저를 띄우지 않고 실행 가능
options.headless = True

# driver = webdriver.Chrome("c:\\chromedriver\\chromedriver", options=options)

driver = webdriver.Chrome("c:\\chromedriver\\chromedriver")

driver.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

driver.implicitly_wait(3)

# 제조사별 더보기 클릭
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            "#dlMaker_simple > dd > div.spec_opt_view > button.btn_spec_view.btn_view_more ",
        )
    )
).click()

# print(driver.page_source)

# 특정 제조사 클릭 = APPLE 클릭
WebDriverWait(driver, 2).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='selectMaker_simple_priceCompare_A']/li[17]/label")
    )
).click()

time.sleep(3)

# BeautifulSoup 사용
soup = BeautifulSoup(driver.page_source, "htlm.parser")

prod_list = soup.select(
    ".main_prodlist.main_prodlist_list > ul > li:not(.prod_ad_item)"
)
# print(prod_list)

for product in prod_list:
    # 제품명
    prod_name = product.select_one(".prod_name > a").text.strip()
    # 가격
    prod_price = product.select_one(".price_sect > a").text.strip()
    # 이미지 주소
    img = product.select_one(".thumb_image img").text.strip()
    if img.get("data-original"):
        prod_img_src = img.get("data-original")
    else:
        prod_img_src = img.get("src")
    print(prod_name, prod_price, "http:" + prod_img_src)

time.sleep(3)

driver.close()
