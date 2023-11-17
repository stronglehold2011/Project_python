import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

"""Page of the selected product"""


class Selected_product(Base):

    # Locators
    size = "/html/body/div[2]/main/div[4]/section/section/aside/div[2]/section/div[2]/button[2]/div/div"
    button_add = ("#__next > main > div:nth-child(4) > section > section > aside > "
                  "div.MainButton__Root-sc-2k69po-0.DwTaZ > button > div > div.WithCounter__Row-sc-1pky0r-1.beYYxP > "
                  "div.Typography__Component-sc-1bp3vo6-0.iTILhy")

    button_go_to_cart = "//button[@class='AddToCartButton__Root-sc-1eeshpm-0 fswwBr addCartBtn']"

    # Getters
    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size)))

    def get_button_add(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_add)))

    def get_button_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_go_to_cart)))

    # Action
    def click_select_size(self):
        self.get_select_size().click()
        print("size selected")

    def click_button_add(self):
        self.get_button_add().click()
        print("button add pressed")

    def click_button_go_to_cart(self):
        self.get_button_go_to_cart().click()
        print("button go to cart")

    # Methods
    def add_product(self):
        with allure.step("Add product"):
            Logger.add_start_step(method="add_product")
            self.get_current_url()
            self.click_select_size()
            self.click_button_add()
            self.click_button_go_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method="add_product")
