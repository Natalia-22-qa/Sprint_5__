from locators import ConstructorPage
from test_data import Pages


class TestConstructor:
    # проверяем, что в стартовом состоянии выбран раздел "Булки"
    def test_buns_on_start_page_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # находим раздел "Булки" (выбран по-умолчанию)
        buns = new_driver.find_element(*ConstructorPage.buns_section)
        # запишем в переменную статус выбранного раздела
        buns_select = new_driver.find_element(*ConstructorPage.buns_section_click)
        # находим раздел "Соусы"
        sauce = new_driver.find_element(*ConstructorPage.sauce_section)
        # находим раздел "Начинки"
        topping = new_driver.find_element(*ConstructorPage.topping_section)
        # проверяем, что выбран именно раздел "Булки"
        assert (buns.get_attribute('class') == buns_select.get_attribute('class')
                 and buns.get_attribute('class') != sauce.get_attribute('class')
                 and buns.get_attribute('class') != topping.get_attribute('class'))

    # проверка переключения с раздела "Булки" на "Соусы"
    def test_cross_from_buns_to_sauce_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # находим раздел "Булки" (выбран по-умолчанию)
        buns = new_driver.find_element(*ConstructorPage.buns_section)
        # находим и кликаем по разделу "Соусы"
        new_driver.find_element(*ConstructorPage.sauce_section).click()
        # отмечаем выбранный раздел
        sauce = new_driver.find_element(*ConstructorPage.sauce_section)
        # запишем в переменную статус выбранного раздела
        sauce_select = new_driver.find_element(*ConstructorPage.sauce_section_click)
        # проверяем, что @class разделов "Соусы" и "Булки" изменились
        assert (sauce.get_attribute('class') == sauce_select.get_attribute('class')
                and sauce.get_attribute('class') != buns.get_attribute('class'))

    # проверка переключения с раздела "Булки" на "Начинки"
    def test_cross_from_buns_to_topping_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # находим раздел "Булки" (выбран по-умолчанию)
        buns = new_driver.find_element(*ConstructorPage.buns_section)
        # находим и кликаем по разделу "Начинки"
        new_driver.find_element(*ConstructorPage.topping_section).click()
        # отмечаем выбранный раздел
        topping = new_driver.find_element(*ConstructorPage.topping_section)
        # запишем в переменную статус выбранного раздела
        topping_select = new_driver.find_element(*ConstructorPage.topping_section_click)
        # проверяем, что @class разделов "Начинки" и "Булки" изменились
        assert (topping.get_attribute('class') == topping_select.get_attribute('class')
                and topping.get_attribute('class') != buns.get_attribute('class'))

    # проверка переключения с "Булки" на "Соусы" и обратно
    def test_cross_between_buns_and_sauce_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # находим раздел "Булки" (выбран по-умолчанию)
        buns = new_driver.find_element(*ConstructorPage.buns_section)
        # находим и кликаем по разделу "Соусы"
        new_driver.find_element(*ConstructorPage.sauce_section).click()
        # снова кликаем по разделу "Булки"
        new_driver.find_element(*ConstructorPage.buns_section).click()
        # запишем в переменную статус выбранного раздела
        buns_select = new_driver.find_element(*ConstructorPage.buns_section_click)
        # проверка статуса
        assert buns.get_attribute('class') == buns_select.get_attribute('class')

    # проверка переключения между разделами конструктора "Булки" и "Начинки"
    def test_cross_between_buns_and_topping_true(self, new_driver):
        # открываем сайт
        new_driver.get(Pages.start_page)
        # находим раздел "Булки" (выбран по-умолчанию)
        buns = new_driver.find_element(*ConstructorPage.buns_section)
        # находим и кликаем по разделу "Начинки"
        new_driver.find_element(*ConstructorPage.topping_section).click()
        # снова кликаем по разделу "Булки"
        new_driver.find_element(*ConstructorPage.buns_section).click()
        # запишем в переменную статус выбранного раздела
        buns_select = new_driver.find_element(*ConstructorPage.buns_section_click)
        # проверка статуса
        assert buns.get_attribute('class') == buns_select.get_attribute('class')

# pytest tests/test_constructor_cross.py
