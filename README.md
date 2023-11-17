# Befree_ui_test
### <div align="lef">Данный проект является учебным. В нем реализован автоматизированный UI тест на Python, с использованием библиотеки Selenium WebDriver.
### <div align="lef">Цель теста: Проверить корректность прохождения бизнес пути покупки товара (от открытия сайта, авторизации, выбора товара и до момента оплаты), на примере интернет магазина https://befree.ru/muzhskaya .
### <div align="left">Что требуется для запуска (если, что-то из нижеперечисленного уже установленно, то игнорируем):
- Скачать проект
- Скачать и установить Python 3 и интегрированную среду разработки PyCharm
- Установить Selenium-WebDriver для Python. Инструкцию смотрим тут: https://selenium-python.com/install-selenium-python
- Скачать актуальную для своего браузера Сhrome версию "Сhromedriver". Смотрим тут: https://chromedriver.chromium.org/
- Импортировать библиотеку Pytest
 
### <div align="left">Краткое описание директорий: </div>  
  
- base - директория в которой хранится базовый класс base_class, содержащий основные методы, используемые в разных частях проекта.
- pages - директория в которой хранятся классы, отвечающие за определенные страницы сайта.
- screen - директория в которую будут сохраняться скриншоты.
- tеsts - директория в которой содержится тест.
- utilities - директория для хранения разлиных утилит.
### <div align="left">Важное примечание: </div>
- Комментарии к классам и методам, можно уведеть на страницах проекта.
- Для запуска теста, в консоли PyCharm пишем: python -m pytest -s -v или python -m pytest -s -v test_buy_product.py .
- В тесте происходит авторизация, поэтому для его корректной отработки, необходимо создать аккаунт на сайте https://befree.ru/muzhskaya . Зайти в директорию "page", выбрать файл "login_page" и в нем в self.input_user_name(" ******** ") заменить звездочки на логин, указанный при создании аккаунта, а в
self.input_password(" ********* ") заменить звездочки на пароль от аккаунта.
