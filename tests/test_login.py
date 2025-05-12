from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Login
from test_data import Pages
from test_data import Data


class TestLogin:
    # проверка входа по кнопке "Войти в аккаунт" на главной странице
    def test_login_through_login_account_button_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # нажимаем на кнопку "Войти в аккаунт"
        new_driver.find_element(*Login.login_account_button).click()
        # ожидание появления страницы авторизации
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.login_label)))
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
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Login.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.account_profile)))
        assert new_driver.current_url == Pages.profile_page

    # проверка входа по кнопке "Личный Кабинет"
    def test_login_through_personal_account_button_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Login.personal_account_button).click()
        # ожидание появления страницы авторизации
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.login_label)))
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
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Login.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.account_profile)))
        assert new_driver.current_url == Pages.profile_page

    # проверка входа по кнопке-ссылке "Войти" в форме регистрации
    def test_login_through_login_link_button_true(self, new_driver):
        # открываем страницу регистрации
        new_driver.get(Pages.registration_page)
        # нажимает кнопку-ссылку "Войти" на странице регистрации
        new_driver.find_element(*Login.login_link_button).click()
        # ожидание появления страницы авторизации
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.login_label)))
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
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Login.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.account_profile)))
        assert new_driver.current_url == Pages.profile_page

    # проверка входа по кнопке-ссылке "Войти" в форме восстановления пароля
    def test_login_through_login_link_button_rcv_true(self, new_driver):
        # открываем страницу восстановления пароля
        new_driver.get(Pages.recover_password_page)
        # нажимает кнопку-ссылку "Войти" на странице восстановления пароля
        new_driver.find_element(*Login.login_link_button_rcv).click()
        # ожидание появления страницы авторизации
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.login_label)))
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
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Login.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Login.account_profile)))
        assert new_driver.current_url == Pages.profile_page

# pytest tests/test_login.py
