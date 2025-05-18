from locators import ConstructorPage
from test_data import Pages
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    # проверка переключения с раздела "Булки" на "Соусы"
    def test_cross_from_buns_to_sauce_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # кликаем по разделу "Соусы"
        WebDriverWait(new_driver,3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.sauce_section)).click()
        # находим выбранный раздел
        active_tab = WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.active_section))
        # проверяем, что выбранный раздел - "Соусы"
        assert "Соусы" in active_tab.text

    # проверка переключения с раздела "Булки" на "Начинки"
    def test_cross_from_buns_to_topping_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # кликаем по разделу "Начинки"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.topping_section)).click()
        # находим выбранный раздел
        active_tab = WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.active_section))
        # проверяем, что выбранный раздел - "Начинки"
        assert "Начинки" in active_tab.text

    # проверка переключения с "Булки" на "Соусы" и обратно
    def test_cross_between_buns_and_sauce_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # кликаем по разделу "Соусы"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.sauce_section)).click()
        # кликаем по разделу "Булки"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.buns_section)).click()
        # находим выбранный раздел
        active_tab = new_driver.find_element(*ConstructorPage.active_section)
        # проверяем, что выбранный раздел - "Булки"
        assert "Булки" in active_tab.text

    # проверка переключения между разделами конструктора "Булки" и "Начинки"
    def test_cross_between_buns_and_topping_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # кликаем по разделу "Начинки"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.topping_section)).click()
        # кликаем по разделу "Булки"
        WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPage.buns_section)).click()
        # находим выбранный раздел
        active_tab = new_driver.find_element(*ConstructorPage.active_section)
        # проверяем, что выбранный раздел - "Булки"
        assert "Булки" in active_tab.text

# pytest tests/test_constructor_cross.py
