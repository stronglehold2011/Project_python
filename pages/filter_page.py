import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains, Keys

from utilities.logger import Logger

"""Filtering products"""


class Filter_page(Base):


    # Locators
    main_sweaters_word = "//*[@id='__next']/main/section/section[1]/div[1]/div/h1"
    cookie = "/html/body/section/div[2]/div/button"
    select_filter = "//*[@id='__next']/main/section/section[1]/div[3]/button[2]/div[2]"
    price_up_to = "/html/body/div[3]/div[1]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/div/input"
    color = "/html/body/div[3]/div[1]/section/div/div[2]/div/ul/li[2]/div[1]/li"
    select_color_beige = "/html/body/div[3]/div[1]/section/div/div[2]/div/ul/li[2]/div[2]/div/div[1]/label"
    size = "/html/body/div[3]/div[1]/section/div/div[2]/div/ul/li[3]/div[1]/li/div[1]/div"
    select_size = "/html/body/div[3]/div[1]/section/div/div[2]/div/ul/li[3]/div[2]/div/div/button[2]/div/div"
    button_show = "/html/body/div[3]/div[1]/section/div/div[2]/div/div/div/div[2]/button/div"

    # Getters

    def get_main_sweaters_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_sweaters_word)))

    def get_cookie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookie)))

    def get_select_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_filter)))

    def get_select_price_up_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_up_to)))

    def get_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_select_color_beige(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_color_beige)))

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size)))

    def get_button_show(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_show)))

    # Action

    def click_cookie(self):
        self.get_cookie().click()
        print("click OK cookie")

    def click_select_filter(self):
        self.get_select_filter().click()
        print("click select  filter")

    def clear_click_get_price_up_to(self):
        self.get_select_price_up_to().send_keys(Keys.BACKSPACE * 4)
        print("price BACKSPACE")

    def input_price_up_to(self, price):
        self.get_select_price_up_to().send_keys(price)
        print("Input price up to")

    def click_color(self):
        self.get_color().click()
        print("click select filter color")

    def click_select_color_beige(self):
        self.get_select_color_beige().click()
        print("click select color beige")

    def click_size(self):
        self.get_size().click()
        print("click select filter size")

    def click_select_size(self):
        self.get_select_size().click()
        print("click select size")

    def click_button_show(self):
        self.get_button_show().click()
        print("click button show")

    # Methods
    def product_filtering(self):
        with allure.step("Product filtering"):
            Logger.add_start_step(method="product_filtering")
            self.get_current_url()
            self.assert_url("https://befree.ru/muzhskaya/svitery-muzskie")
            self.assert_word(self.get_main_sweaters_word(), "свитеры")
            self.click_cookie()
            self.click_select_filter()
            self.clear_click_get_price_up_to()
            self.input_price_up_to("3000")
            self.click_color()
            self.click_select_color_beige()
            self.click_color()
            self.click_size()
            self.click_select_size()
            self.click_size()
            self.driver.execute_script(f'window.scrollBy({0},{400})')
            self.click_button_show()
            Logger.add_end_step(url=self.driver.current_url, method="product_filtering")
