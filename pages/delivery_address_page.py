import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

"""Delivery address page"""


class Delivery_address_page(Base):


    # Locators

    name_street = "//*[@id='__next']/section/section/section/section/aside/section/div/div/input"
    button_address = "//*[@id='__next']/section/section/section/section/aside/div/ul/li/div[1]/div[2]"
    button_bring_here = "//*[@id='__next']/section/section/section/section/aside/section/section/div[5]/div/button"

    # Getters

    def get_name_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_street)))

    def get_button_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_address)))

    def get_button_bring_here(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_bring_here)))

    # Action

    def input_name_street(self, name_street):
        self.get_name_street().send_keys(name_street)
        print("Input address")

    def click_button_address(self):
        self.get_button_address().click()
        print("click button enter address")

    def click_button_bring_here(self):
        self.get_button_bring_here().click()
        print("click button bring here")

    # Methods
    def delivery_address(self):
        with allure.step("Delivery address"):
            Logger.add_start_step(method="delivery_address")
            self.get_current_url()
            self.assert_url("https://befree.ru/checkout/delivery")
            self.input_name_street("Lamoda | СПб | м. Удельная |Удельный пр-т 27")
            self.click_button_address()
            self.click_button_bring_here()
            Logger.add_end_step(url=self.driver.current_url, method="delivery_address")
