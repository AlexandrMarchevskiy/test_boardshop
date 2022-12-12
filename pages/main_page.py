from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page(Base):

    url = 'https://www.brd.ru/home-man'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_brand = '/html/body/div[1]/main/div/div[4]/div/div/a[4]'

    # Getters

    def get_select_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_brand)))

    #Actions
    def click_select_brand(self):
        self.get_select_brand().click()

    # Methods
    def select_brand_element(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_select_brand()
        self.get_current_url()
        self.assert_url('https://www.brd.ru/brand/element')