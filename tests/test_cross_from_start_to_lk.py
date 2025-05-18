from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Cross
from test_data import Pages


class TestCross:
    # проверка перехода со стартовой страницы в ЛК
    def test_cross_from_start_page_to_lk_true(self, new_driver, login):
        # сперва авторизируемся, используем фикстуру login
        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Cross.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Cross.account_profile)))
        assert new_driver.current_url == Pages.profile_page

# pytest tests/test_cross_from_start_to_lk.py
