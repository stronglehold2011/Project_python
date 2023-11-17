import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base
from utilities.logger import Logger

"""Checkout summary page"""


class Checkout_summary(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    # Locators

    button_payment_method = "//*[@id='__next']/section/div/section/div[1]/section[2]/ul/li[3]/div[1]/label/span[2]"
    button_checkout = "//*[@id='__next']/section/div/section/div[2]/div[2]/div/div/button/div"

    # Getters

    def get_button_payment_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_payment_method)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    # Action

    def click_button_payment_method(self):
        self.get_button_payment_method().click()

    def click_button_checkout(self):
        self.get_button_checkout().click()

    # Methods
    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url("https://befree.ru/checkout/summary")
            self.get_screenshot()
            time.sleep(3)
            self.click_button_payment_method()
            self.click_button_checkout()
            time.sleep(3)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")
