from datetime import datetime

from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):  # сохраняем в метод: 1.self, 2.элемент, 3.значение, которое ожидаем получить
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # в скобках год.месяц.день.час.минута.секунда.

        """Создадим переменную и сохраним в нее название нашего нового файла:"""
        name_screenshot = 'screenshot' + now_date + '.png'

        """Обращаемся к переменной driver и пишем save_screenshot и путь дериктории в которую сохраняем"""
        self.driver.save_screenshot(
            'C:\\Users\\Рома\\PycharmProjects\\pythonProject1\\main_project_1\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result: object) -> object:
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method scroll page """

    def scroll(self, x, y):
        return self.driver.execute_script(f'window.scrollBy({x},{y})')

    """Method of pointing at the element"""

    def hover_actions_chains(self, element):
        locator = self.driver.find_element(element)
        return ActionChains(self.driver).move_to_element(locator).perform()

    """Method price comparison """
    def assert_price(self, price1, price2):
        assert price1 == price2
        print("The price of the product matches")
