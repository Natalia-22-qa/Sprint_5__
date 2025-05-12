import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data_generation import DataGeneration
from locators import Registration
from test_data import Pages


class TestRegistration:
    # проверка регистрации при вводе корректных данных
    def test_registration_successfully(self, new_driver):
        # открываем страницу регистрации
        new_driver.get(Pages.registration_page)
        # нажимаем на поле "Имя"
        new_driver.find_element(*Registration.name_input).click()
        # ожидание появления поля ввода имени
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.name_field)))
        # вводим имя пользователя
        new_driver.find_element(*Registration.name_field).send_keys(DataGeneration.name_generation())
        # нажимаем на поле "Email"
        new_driver.find_element(*Registration.email_input).click()
        # ожидание появления поля ввода логина
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.email_field)))
        # вводим логин
        new_driver.find_element(*Registration.email_field).send_keys(DataGeneration.login_generation())
        # нажимаем на поле "Пароль"
        new_driver.find_element(*Registration.password_input).click()
        # ожидание появления поля ввода пароля
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.password_field)))
        # вводим пароль
        new_driver.find_element(*Registration.password_field).send_keys(DataGeneration.password_generation())
        # нажимает кнопку "Зарегистрироваться"
        new_driver.find_element(*Registration.register_button).click()
        # ожидание появления страницы авторизации
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.login_label)))
        assert new_driver.current_url == Pages.login_page

    # проверка вывода ошибки при некорректном пароле
    @pytest.mark.parametrize('password_failed', ['1','12','123','1234','12345'])
    def test_show_error_when_password_failed(self, new_driver, password_failed):
        # открываем страницу регистрации
        new_driver.get(Pages.registration_page)
        # нажимаем на поле "Имя"
        new_driver.find_element(*Registration.name_input).click()
        # ожидание появления поля ввода имени
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.name_field)))
        # вводим имя
        new_driver.find_element(*Registration.name_field).send_keys(DataGeneration.name_generation())
        # нажимаем на поле "Email"
        new_driver.find_element(*Registration.email_input).click()
        # ожидание появления поля ввода логина
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.email_field)))
        # вводим логин
        new_driver.find_element(*Registration.email_field).send_keys(DataGeneration.login_generation())
        # нажимаем на поле "Пароль"
        new_driver.find_element(*Registration.password_input).click()
        # ожидание появления поля ввода пароля
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.password_field)))
        # вводим пароль
        new_driver.find_element(*Registration.password_field).send_keys(password_failed)
        # нажимает кнопку "Зарегистрироваться"
        new_driver.find_element(*Registration.register_button).click()
        # ожидание появления надписи "Некорректный пароль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Registration.password_error)))
        assert new_driver.find_element(*Registration.password_error)

# pytest tests/test_registration.py
