import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

"""Main page and product category selection"""
class Main_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    # Locators

    mens_button = "//*[@id='__next']/div[3]/div/div[1]/div/a[2]/div/button"
    select_category_cloth = "/html/body/div[3]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[3]/a/div/div/div[1]/div"
    select_sweaters_and_jumpers = "/html/body/div[4]/div[1]/section/div/div[2]/div/div[6]/a/div/div/div[1]/div"
    select_sweaters = "/html/body/div[5]/div[1]/section/div/div[2]/div/div[2]/a/div/div/div[1]/div"

    # Getters

    def get_select_mens_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mens_button)))

    def get_select_category_cloth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category_cloth)))

    def get_select_sweaters_and_jumpers(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_sweaters_and_jumpers)))

    def get_select_sweaters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_sweaters)))

    # Action

    def click_select_mens_button(self):
        self.get_select_mens_button().click()
        print("Click select mens button")

    def click_select_category_cloth(self):
        ActionChains(self.driver).move_to_element(self.get_select_category_cloth()).perform()
        self.get_select_category_cloth().click()
        print("Click select category cloth")

    def click_select_sweaters_and_jumpers(self):
        self.get_select_sweaters_and_jumpers().click()
        print("Click select sweaters and jumpers")

    def click_select_sweaters(self):
        self.get_select_sweaters().click()
        print("Click select sweaters")

    # Methods
    def select_categories_1(self):
        with allure.step("Select categories 1"):
            Logger.add_start_step(method="select_categories_1")
            self.get_current_url()
            self.assert_url("https://befree.ru/muzhskaya")
            self.click_select_mens_button()
            self.click_select_category_cloth()
            self.click_select_sweaters_and_jumpers()
            self.click_select_sweaters()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_categories_1")
