import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

"""Filtered Products Page"""
# Globals
price_sweater_text = ''


class Filter_sweaters_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #
    #     self.driver = driver

    # Locators
    main_sweaters_word = "//*[@id='__next']/main/section/section[1]/div[1]/div/h1"
    name_sweater = "//*[@id='__next']/main/section/section[2]/section/div/div/div/div/a/div/div/div[2]/div[2]"
    price_sweater = "//*[@id='__next']/main/section/section[2]/section/div/div/div/div/a/div/div/div[2]/div[1]/div/div[1]/div/div[1]"

    # Getters

    def get_main_sweaters_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_sweaters_word)))

    def get_select_sweater(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_sweater)))

    # Action

    def click_select_sweater(self):
        self.get_select_sweater().click()
        print("click cotton sweater with pigtail pattern")

    """Getting the price of the product"""

    def price_sweater_text_1(self):
        global price_sweater_text
        product_1 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_sweater)))
        price_sweater_text = product_1.text + " Р"

        return price_sweater_text

    # Methods
    def select_sweaters(self):
        with allure.step("Select sweaters"):
            Logger.add_start_step(method="select_sweaters")
            self.get_current_url()
            self.assert_url("https://befree.ru/muzhskaya/svitery-muzskie?filters=%7B%22prices%22%3A%7B%22min_value%22"
                            "%3A2999%2C%22max_value%22%3A3000%7D%2C%22colors%22%3A%7B%22value_ids%22%3A%5B10%5D%7D%2C"
                            "%22sizes%22%3A%7B%22value_ids%22%3A%5B3%5D%7D%7D")
            self.assert_word(self.get_main_sweaters_word(), "свитеры")
            self.driver.execute_script(f'window.scrollBy({0},{300})')
            self.click_select_sweater()
            self.price_sweater_text_1()
            Logger.add_end_step(url=self.driver.current_url, method="select_sweaters")
