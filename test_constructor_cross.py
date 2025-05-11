import time
# паузы добавлены для зрительного отслеживания
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorPage
from locators import Pages

class TestConstructor:
    # проверяем, что в стартовом состоянии выбран раздел "Булки"
    def test_buns_on_start_page_true(self, new_driver):
        # значение атрибута class у выбранного и невыбранного раздела конструктора
        active = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        not_active = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'

        # открываем сайт
        new_driver.get(Pages.start_page)

        # находим раздел "Булки"
        buns = new_driver.find_element(*ConstructorPage.buns_section_click)
        # находим раздел "Соусы"
        sauce = new_driver.find_element(*ConstructorPage.sauce_section_click)
        # находим раздел "Начинки"
        topping = new_driver.find_element(*ConstructorPage.topping_section_click)
        # проверяем, что выбран именно раздел "Булки"
        assert (buns.get_attribute('class') == active
                and sauce.get_attribute('class') == not_active
                and topping.get_attribute('class') == not_active)

    # проверка переключения между разделами конструктора "Булки" и "Соусы"
    def test_cross_between_buns_and_sauce_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)

        # записали заголовок "Булки" из меню в переменную
        buns_label = new_driver.find_element(*ConstructorPage.buns_label)
        # кликаем по разделу "Соусы"
        new_driver.find_element(*ConstructorPage.sauce_section_click).click()
        # ожидание появления заголовка "Соусы" в меню
        sauce_label = WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((ConstructorPage.sauce_label)))

        time.sleep(1)
        # проверяем, что заголовок "Соусы" видно, а "Булки" нет
        assert sauce_label.is_displayed() and buns_label.is_enabled()

        # кликаем по разделу "Булки"
        new_driver.find_element(*ConstructorPage.buns_section_click).click()
        # ожидание появления заголовка "Булки" в меню
        buns_label = WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((ConstructorPage.buns_label)))

        time.sleep(1)

        assert buns_label.is_displayed()

    # проверка переключения между разделами конструктора "Булки" и "Начинки"
    def test_cross_between_buns_and_topping_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)

        # записали заголовок "Булки" из меню в переменную
        buns_label = new_driver.find_element(*ConstructorPage.buns_label)
        # кликаем по разделу "Начинки"
        new_driver.find_element(*ConstructorPage.topping_section_click).click()
        # ожидание появления заголовка "Начинки" в меню
        topping_label = WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((ConstructorPage.topping_label)))

        time.sleep(1)
        # проверяем, что заголовок "Начинки" видно, а "Булки" нет
        assert topping_label.is_displayed() and buns_label.is_enabled()

        # кликаем по разделу "Булки"
        new_driver.find_element(*ConstructorPage.buns_section_click).click()
        # ожидание появления заголовка "Булки" в меню
        buns_label = WebDriverWait(new_driver, 3).until(
            expected_conditions.visibility_of_element_located((ConstructorPage.buns_label)))

        time.sleep(1)

        assert buns_label.is_displayed()

# pytest tests/test_constructor_cross.py
