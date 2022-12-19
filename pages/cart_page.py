import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    jeans_element_E02 = ('//a[@href="/product/z1pnb1-elf1-504-muzhskie-zauzhennye-dzhinsy-element-e02"]', 'Мужские Зауженные Джинсы Element E02')
    shoes_topaz_C3 = ('//a[@href="/product/z6tm31-01a-339-muzhskie-kozhanye-botinki-topaz-c3"]', 'Мужские Кожаные Ботинки Topaz C3')
    hoodie_element = ('//a[@href="/product/w1hob1-elp1-967-muzhskoe-hudi-element-forces"]', 'Мужское Худи Element Forces')

    total_price = '//span[@class="js-allproductstotal-text"]'

    # Getters


    def get_total_price(self):
        return self.driver.find_element(By.XPATH, self.total_price)



    # Methods

    def cart_check(self, getters):
        in_cart = []
        not_in_cart = []
        for product in getters:
            try:
                WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, product[0])))
                in_cart.append(product[1])
            except:
                not_in_cart.append(product[1])
        print(f'В корзине {len(in_cart)} продуктов: {in_cart} , на сумму: {self.get_total_price().text}.  \n Не в корзине {not_in_cart}')

    def info_cart(self):
        products = [self.jeans_element_E02, self.shoes_topaz_C3, self.hoodie_element]
        self.cart_check(products)
