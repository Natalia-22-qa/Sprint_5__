import time
# паузы добавлены для зрительного отслеживания
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Exit
from locators import Pages


class TestExit:
    def test_exit_from_lk_true(self, new_driver, login):

    # сперва авторизируемся, используем фикстуру login

        # нажимает кнопку "Личный Кабинет"
        new_driver.find_element(*Exit.personal_account_button).click()
        # ожидание появления раздела "Профиль"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Exit.account_profile)))

        time.sleep(1)

        # нажимает кнопку "Выход"
        new_driver.find_element(*Exit.exit_button).click()
        # ожидание появления страницы авторизации
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((Exit.login_label)))

        time.sleep(1)

        assert new_driver.current_url == Pages.login_page

# pytest tests/test_exit.py
