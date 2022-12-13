from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Brand_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    male_box = '//*[@id="mCSB_1_container"]/label[1]'
    shoes = '//*[@id="mCSB_2_container"]/label[4]'
    jeans = '//*[@id="mCSB_2_container"]/label[17]'
    hoodies = '//*[@id="mCSB_2_container"]/label[53]'

    # Getters

    def get_male_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.male_box)))

    def get_shoes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shoes)))

    def get_jeans(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jeans)))

    def get_hoodies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hoodies)))

    #Actions
    def click_male_box(self):
        self.get_male_box().click()

    def click_shoes(self):
        self.get_shoes().click()
        print('shoes cat selected')

    def click_jeans(self):
        self.get_jeans().click()
        print('jeans cat selected')

    def click_hoodies(self):
        self.get_hoodies().click()
        print('hoodies cat selected')

    # Methods
    def select_cats(self):
        self.get_current_url()
        self.click_male_box()
        self.click_shoes()
        self.click_jeans()
        self.click_hoodies()