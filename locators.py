from selenium.webdriver.common.by import By


class Registration:
    # поле "Имя"
    name_input = (By.XPATH, ".//fieldset[1]//label[text() = 'Имя']")
    # поле для ввода имени пользователя
    name_field = (By.XPATH, ".//fieldset[1]//input[@value = '']")
    # поле "Email"
    email_input = (By.XPATH, ".//fieldset[2]//label[text() = 'Email']")
    # поле для ввода логина (Email)
    email_field = (By.XPATH, ".//fieldset[2]//input[@value = '']")
    # поле "Пароль"
    password_input = (By.XPATH, ".//fieldset[3]//label[text() = 'Пароль']")
    # поле для ввода пароля
    password_field = (By.XPATH, ".//fieldset[3]//input[@value = '']")
    # кнопка "Зарегистрироваться"
    register_button = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    # надпись "Вход" на странице авторизации
    login_label = (By.XPATH, ".//h2[text() = 'Вход']")
    # надпись "Некорректный пароль"
    password_error = (By.XPATH, ".//p[text() = 'Некорректный пароль']")

class Login:
    # надпись "Вход" на странице авторизации
    login_label = (By.XPATH, ".//h2[text() = 'Вход']")
    # кнопка "Войти в аккаунт" на главной странице
    login_account_button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # кнопка "Личный Кабинет" на верхней панели
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    # кнопка-ссылка "Войти" на странице регистрации
    login_link_button = (By.XPATH, ".//p[text() = 'Уже зарегистрированы?']/a[(@href = '/login') and (text() = 'Войти')]")
    # кнопка-ссылка "Войти" на странице восстановления пароля
    login_link_button_rcv = (By.XPATH, ".//p[text() = 'Вспомнили пароль?']/a[(@href = '/login') and (text() = 'Войти')]")
    # поле "Email"
    email_input = (By.XPATH, ".//fieldset[1]//label[text() = 'Email']")
    # поле для ввода логина (Email)
    email_field = (By.XPATH, ".//fieldset[1]//input[@value = '']")
    # поле "Пароль"
    password_input = (By.XPATH, ".//fieldset[2]//label[text() = 'Пароль']")
    # поле для ввода пароля
    password_field = (By.XPATH, ".//fieldset[2]//input[@value = '']")
    # кнопка "Войти"
    login_button = (By.XPATH, ".//button[text() = 'Войти']")
    # надпись "Профиль" на странице личного кабинета
    account_profile = (By.XPATH, ".//a[(@href = '/account/profile') and (text() = 'Профиль')]")

class Cross:
    # кнопка "Личный Кабинет" на верхней панели
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    # надпись "Профиль" на странице личного кабинета
    account_profile = (By.XPATH, ".//a[(@href = '/account/profile') and (text() = 'Профиль')]")
    # кнопка "Конструктор" на верхней панели
    constructor_button = (By.XPATH, ".//li[1]")
    # логотип-ссылка Stellar Burger
    logo_link = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")
    # надпись "Соберите бургер" на странице конструктора
    constructor_page = (By.XPATH, ".//h1[text() = 'Соберите бургер']")

class ConstructorPage:
    # раздел "Булки"
    buns_section = (By.XPATH, ".//main/section[1]/div[@style = 'display: flex;']/div[1]")
    # раздел "Булки" выбран
    buns_section_click = (By.XPATH, ".//main/section[1]/div[@style = 'display: flex;']/div[1][contains(@class, 'tab_tab_type_current')]")
    # раздел "Соусы"
    sauce_section = (By.XPATH, ".//main/section[1]/div[@style = 'display: flex;']/div[2]")
    # раздел "Соусы" выбран
    sauce_section_click = (By.XPATH, ".//main/section[1]/div[@style = 'display: flex;']/div[2][contains(@class, 'tab_tab_type_current')]")
    # раздел "Начинки"
    topping_section = (By.XPATH, ".//main/section[1]/div[@style = 'display: flex;']/div[3]")
    # раздел "Начинки" выбран
    topping_section_click = (By.XPATH, ".//main/section[1]/div[@style = 'display: flex;']/div[3][contains(@class, 'tab_tab_type_current')]")

class Exit:
    # кнопка "Личный Кабинет" на верхней панели
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    # надпись "Профиль" на странице личного кабинета
    account_profile = (By.XPATH, ".//a[(@href = '/account/profile') and (text() = 'Профиль')]")
    # кнопка "Выход" в ЛК
    exit_button = (By.XPATH, ".//button[text() = 'Выход']")
    # надпись "Вход" на странице авторизации
    login_label = (By.XPATH, ".//h2[text() = 'Вход']")
