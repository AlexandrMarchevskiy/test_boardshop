import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from pages.brand_page import Brand_page
from pages.main_page import Main_page

def test_buy_product(set_group):
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')   # отключение предупреждения ошибки рукопожатия


    s = Service('D:\\test_shop_project\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)

    mp = Main_page(driver)
    time.sleep(2)
    mp.select_brand_element()

    bp = Brand_page(driver)
    time.sleep(2)
    bp.select_cats()
    time.sleep(2)
    bp.select_products()
    time.sleep(2)
