import time
import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    url = 'https://www.brd.ru/home-man'
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators
    select_brand = "//img[@alt='Element']"
    
    # Getters
    
    def get_select_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_brand)))
    
    # Actions
    def click_select_brand(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_select_brand())
        self.get_select_brand().click()
    
    # Methods
    def select_brand_element(self):
        with allure.step('Select brand element'):
            Logger.add_start_step(method='select_brand_element')
            self.driver.get(self.url)
            self.driver.maximize_window()
            time.sleep(2)
            self.click_select_brand()
            self.get_current_url()
            self.assert_url('https://www.brd.ru/brand/element')
            self.get_screen_shot('brand_element')
            Logger.add_end_step(url=self.driver.current_url, method='select_brand_element')
