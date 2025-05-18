import pytest
from selenium import webdriver
from locators import Login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_data import Pages
from test_data import Data

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
    new_driver.find_element(*Login.email_field).send_keys(Data.test_email)
    # нажимаем на поле "Пароль"
    new_driver.find_element(*Login.password_input).click()
    # ожидание появления поля ввода пароля
    WebDriverWait(new_driver, 3).until(
        expected_conditions.visibility_of_element_located((Login.password_field)))
    # вводим пароль
    new_driver.find_element(*Login.password_field).send_keys(Data.test_password)
    # нажимает кнопку "Войти"
    new_driver.find_element(*Login.login_button).click()
    new_driver.maximize_window()
    yield
