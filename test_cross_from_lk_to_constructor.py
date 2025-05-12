from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Cross
from test_data import Pages


class TestCross:
    # проверка перехода из ЛК в конструктор по клику на логотип Stellar Burgers
    def test_cross_from_lk_to_constructor_through_logo_true(self, new_driver, login):
        # сперва авторизируемся, используем фикстуру login
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Cross.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Cross.account_profile)))
        # нажимает на логотип Stellar Burgers
        new_driver.find_element(*Cross.logo_link).click()
        # ожидание появления раздела "Соберите бургер"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Cross.constructor_page)))
        assert new_driver.current_url == Pages.start_page

    # проверка перехода из ЛК в конструктор по клику на "Конструктор"
    def test_cross_from_lk_to_constructor_through_constructor_button_true(self, new_driver, login):
        # сперва авторизируемся, используем фикстуру login
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Cross.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Cross.account_profile)))
        # нажимает на "Конструктор"
        new_driver.find_element(*Cross.constructor_button).click()
        # ожидание появления раздела "Соберите бургер"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Cross.constructor_page)))
        assert new_driver.current_url == Pages.start_page

# pytest tests/test_cross_from_lk_to_constructor.py
