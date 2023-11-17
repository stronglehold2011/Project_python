import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages import filtered_sweaters_page

from base.base_class import Base
from utilities.logger import Logger

"""Cart page"""


class Cart_page(Base):  # теперь класс Cart_page классом потомком класса Base

    # def __init__(self, driver):  # Передаем driver, чтобы отсюда мы могли запускать шаги авторизации
    #     super().__init__(driver)  # super указывает, что это потомок
    #     self.driver = driver

    # Locators

    button_place_an_order = "//button[@class='Button__Component-sc-1qrls71-1 Button__Main-sc-1qrls71-2 dtDlMV kUMWms']"
    price_cart = "//*[@id='__next']/main/div/section/section/section[2]/div/section[2]/div[1]/div[2]/div[2]"

    # Getters

    def get_button_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_an_order)))

    def get_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_cart)))

    # Action

    def click_button_place_an_order(self):
        self.get_button_place_an_order().click()
        print("click button place an order")

    def price_cart_text(self):
        price_g = self.get_price_cart().text
        return price_g

    # Methods
    def placing_an_order(self):
        with allure.step("Placing an order"):
            Logger.add_start_step(method="placing_an_order")
            self.get_current_url()
            self.assert_url("https://befree.ru/cart")
            self.assert_price(filtered_sweaters_page.price_sweater_text, self.price_cart_text())
            time.sleep(3)
            self.click_button_place_an_order()
            Logger.add_end_step(url=self.driver.current_url, method="placing_an_order")
