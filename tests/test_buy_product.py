from datetime import time
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.checkout_summary_page import Checkout_summary
from pages.delivery_address_page import Delivery_address_page
from pages.delivery_method_page import Delivery_method_page
from pages.filter_page import Filter_page
from pages.filtered_sweaters_page import Filter_sweaters_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.selected_product_page import Selected_product
import allure


@allure.description("Test buy product 1")
def test_buy_product_1(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 1")

    login = Login_page(driver)

    login.authorization()

    mp = Main_page(driver)
    mp.select_categories_1()

    fp = Filter_page(driver)
    fp.product_filtering()

    fsp = Filter_sweaters_page(driver)
    fsp.select_sweaters()

    sp = Selected_product(driver)
    sp.add_product()

    cp = Cart_page(driver)
    cp.placing_an_order()

    dmp = Delivery_method_page(driver)
    dmp.delivery()
    time.sleep(3)
    dap = Delivery_address_page(driver)
    dap.delivery_address()

    cs = Checkout_summary(driver)
    cs.finish()

    print("Finish Test")
    driver.quit()
