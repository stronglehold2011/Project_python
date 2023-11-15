from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Authorization page"""
class Login_page(Base):  # теперь класс Login_page стал классом потомком класса Base

    url = 'https://befree.ru/muzhskaya'

    def __init__(self, driver):  # Передаем driver, чтобы отсюда мы могли запускать шаги авторизации
        super().__init__(driver)  # super указывает, что это потомок
        self.driver = driver

    # Locators

    entrance = ("#__next > div.Header__Root-zhep8t-0.iWEsyZ > header > div.Header__Info-zhep8t-5.efDoIf > "
                "div.Profile__Block-sc-1ak7qq8-0.cbwqnQ > div > svg")
    user_name = "//input[@inputmode='email']"
    password = "//input[@type='password']"
    sign_in_button = "/html/body/div[3]/div[1]/section/div/div[2]/div/section/section/section/form/div[4]/div/button"

    # Getters

    def get_entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.entrance)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button)))

    # Action
    def click_entrance(self):
        self.get_entrance().click()
        print("click entrance")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def click_sign_in_button(self):
        self.get_sign_in_button().click()
        print("Authorization passed ")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_entrance()
        self.input_user_name("testovarov@mail.ru")
        self.input_password("Iyri)OuIlI12")
        self.click_sign_in_button()

