import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Brand_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators cats
    male_box = '//*[@id="mCSB_1_container"]/label[1]'
    shoes = '//*[@id="mCSB_2_container"]/label[4]'
    jeans = '//*[@id="mCSB_2_container"]/label[18]'
    hoodies = '//*[@id="mCSB_2_container"]/label[54]'

    # Locators products

    jeans_element_E02 = '/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div[1]/div/a'
    shoes_topaz_C3 = '//a[@href="/product/z6tm31-01a-339-muzhskie-kozhanye-botinki-topaz-c3"]'
    hoodi_element_92 = '/html/body/div[1]/main/div[3]/div/div[2]/div[9]/div[1]/div/a'


    # Locators in products
    jeans_size_32_32 = '//*[@id="add_product-form"]/div/label[5]'
    add_product_in_cart = '//*[@id="product-detail"]/div[1]/div[1]/aside/div[4]/button'

    shoes_size_42 = '//*[@id="add_product-form"]/div/label[6]'

    # Optional locators

    scrollbar_cats = '//*[@id="mCSB_2_dragger_vertical"]'

    close_msg = '/html/body/div[8]/div/div[3]/label'



    # Getters cats

    def get_male_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.male_box)))

    def get_shoes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shoes)))

    def get_jeans(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jeans)))

    def get_hoodies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hoodies)))

    # Getters products

    def get_jeans_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jeans_element_E02)))

    def get_shoes_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shoes_topaz_C3)))

    def get_hoodie_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hoodi_element_92)))

    # Getters options

    def get_scrollbar_cats(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.scrollbar_cats)))


    def get_close_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_msg)))


    def get_jeans_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jeans_size_32_32)))

    def get_product_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_in_cart)))

    def get_shoes_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shoes_size_42)))


    #Actions cats

    def click_male_box(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_scrollbar_cats())
        self.get_male_box().click()

    def click_shoes(self):
        self.get_shoes().click()
        print('shoes cat selected')

    def click_jeans(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_scrollbar_cats()).move_by_offset(0, 45).release().perform()
        self.get_jeans().click()
        print('jeans cat selected')

    def click_hoodies(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_scrollbar_cats()).move_by_offset(0, 80).release().perform()
        self.get_hoodies().click()
        print('hoodies cat selected')

    # Actions products

    def select_jeans(self):
        self.get_jeans_product().click()
        self.assert_url('https://www.brd.ru/product/z1pnb1-elf1-504-muzhskie-zauzhennye-dzhinsy-element-e02')
        self.get_jeans_size().click()
        self.get_product_add_cart().click()
        self.get_close_message().click()
        self.driver.back()
        print('jeans selected!')
        time.sleep(3)

    def select_shoes(self):
        self.driver.execute_script("window.scrollTo(0, 1700)")
        self.get_shoes_product().click()
        self.assert_url('https://www.brd.ru/product/z6tm31-01a-339-muzhskie-kozhanye-botinki-topaz-c3')
        self.get_shoes_size().click()
        self.get_product_add_cart().click()
        self.get_close_message().click()
        self.driver.back()
        print('shoes selected!')


    # Methods
    def select_cats(self):
        self.click_male_box()
        time.sleep(2)
        self.click_shoes()
        time.sleep(2)
        self.click_jeans()
        time.sleep(2)
        self.click_hoodies()

    def select_products(self):
        self.select_jeans()
        self.select_shoes()