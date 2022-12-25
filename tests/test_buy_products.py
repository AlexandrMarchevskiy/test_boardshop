import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.brand_page import Brand_page
from pages.cart_page import Cart_page
from pages.main_page import Main_page


@pytest.mark.parametrize('execution_number', range(1, 6))
def test_buy_product(set_group, execution_number):
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')  # отключение предупреждения ошибки рукопожатия
    
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
    
    cp = Cart_page(driver)
    cp.info_cart()