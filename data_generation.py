import random as r
import string as s


class DataGeneration:

    # генерируем имя пользователя
    @staticmethod
    def name_generation():
        name_length = r.randint(4, 8)
        name = ''.join(r.choice(s.ascii_letters) for _ in range(name_length))
        return name


    # генерируем логин (Email)
    @staticmethod
    def login_generation():
        login_length = r.randint(3, 5)
        login = ''.join(r.choice(s.ascii_letters + s.digits) for _ in range(login_length))

        domains = ['mail.ru', 'yandex.ru', 'gmail.com']
        domain = r.choice(domains)

        return f'{login}@{domain}'

    # генерируем пароль
    @staticmethod
    def password_generation():
        password_length = r.randint(6, 10)
        password = ''.join(r.choice(s.ascii_letters + s.digits) for _ in range(password_length))
        return password
