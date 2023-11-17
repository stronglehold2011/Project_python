import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

"""Delivery method page"""


class Delivery_method_page(Base):


    # Locators

    main_delivery_word = "/html/body/div[3]/div/div/div/div/div"
    method_delivery_1 = "/html/body/div[3]/div/div/div/div/section/button[1]/div/div[2]"

    # Getters

    def get_main_delivery_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_delivery_word)))

    def get_method_delivery_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.method_delivery_1)))

    # Action

    def click_method_delivery_1(self):
        self.get_method_delivery_1().click()
        print("click button method delivery pick-up point")

    # Methods
    def delivery(self):
        with allure.step("Delivery"):
            Logger.add_start_step(method="delivery")
            self.get_current_url()
            self.assert_url("https://befree.ru/cart")
            self.assert_word(self.get_main_delivery_word(), "выберите способ доставки")
            self.click_method_delivery_1()
            Logger.add_end_step(url=self.driver.current_url, method="delivery")
