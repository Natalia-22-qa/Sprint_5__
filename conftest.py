import time
# паузы добавлены для зрительного отслеживания
import pytest
from selenium import webdriver
from locators import Login
from locators import Pages
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# создание driver
@pytest.fixture()
def new_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# авторизация
@pytest.fixture()
def login(new_driver):
    new_driver.get(Pages.login_page)
    # нажимаем на поле "Email"
    new_driver.find_element(*Login.email_input).click()
    # ожидание появления поля ввода логина
    WebDriverWait(new_driver, 3).until(
        expected_conditions.visibility_of_element_located((Login.email_field)))
    # вводим существующий логин
    new_driver.find_element(*Login.email_field).send_keys('natalia_aleksandrova_22qa_111@mail.ru')
    # нажимаем на поле "Пароль"
    new_driver.find_element(*Login.password_input).click()
    # ожидание появления поля ввода пароля
    WebDriverWait(new_driver, 3).until(
        expected_conditions.visibility_of_element_located((Login.password_field)))
    # вводим пароль
    new_driver.find_element(*Login.password_field).send_keys('123456')
    # нажимает кнопку "Войти"
    new_driver.find_element(*Login.login_button).click()
    new_driver.maximize_window()
    time.sleep(1)
    yield