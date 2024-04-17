import string
import random


def generate_random_email():
    """Генерит 7-значную строку"""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

    """Список доменов"""
    domains = ['mail.ru', 'maill.ru',
               'vk.ru', 'vkk.ru',
               'rambler.ru', 'ramble.ru',
               'yandex.ru', 'ya.ru']

    """Выбрать рандомный домен"""
    domain = random.choice(domains)

    """Склеить имя и домен"""
    email = f"{username}@{domain}"

    return email


def generate_random_phone_number():
    prefix = '+7 (9'
    middle = '{:03d}'.format(
        random.randint(100, 999))
    suffix = '){:03d}-{:02d}-{:02d}'.format(random.randint(0, 9),
                                            random.randint(0, 9),
                                            random.randint(0, 9))
    return prefix + middle + suffix
