
from datetime import datetime
import requests


FILE_TO_WRITE = r'logger.txt'
API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'


# ЗАДАНИЕ 1


def logger(func):

    def get_func_info(*args):
        func_name = func.__name__
        func_time = datetime.now()
        func_args = args
        func_result = func(args[0])

        with open(FILE_TO_WRITE, 'w', encoding='utf-8') as logger_file:
            logger_file.write(f'Имя функции: {func_name}\n')
            logger_file.write(f'Дата и время запуска функции: {func_time}\n')
            logger_file.write(f'Аргументы функции: {func_args}\n')
            logger_file.write(f'Результат функции: {func_result}\n')

    return get_func_info


@logger
def raise_to_pow(num):
    result = num ** 2
    return result

# выполняем функцию для проверки декоратора
raise_to_pow(11)


# ЗАДАНИЕ 2

def decorate(file=FILE_TO_WRITE):

    def logger(func):

        def get_func_info(*args):
            func_name = func.__name__
            func_time = datetime.now()
            func_args = args, file
            func_result = func(args[0])

            with open(file, 'w', encoding='utf-8') as logger_file:
                logger_file.write(f'Имя функции: {func_name}\n')
                logger_file.write(f'Дата и время запуска функции: {func_time}\n')
                logger_file.write(f'Аргументы функции: {func_args}\n')
                logger_file.write(f'Результат функции: {func_result}\n')
        return get_func_info
    return logger


@decorate()
def raise_to_pow(num):
    result = num ** 2
    return result

# выполняем функцию для проверки декоратора
raise_to_pow(34)


# ЗАДАНИЕ 3
# Функция взята из домашнего задания по теме: 3.2.http.requests

@decorate()
def get_lang_id(language_name):
    # функция принимает название языка на русском и возвращает его параметр в виде id из Яндекс.Переводчик API

    langs_url = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'

    params = {
        'key': API_KEY,
        'ui': 'ru'
    }

    langs = requests.get(langs_url, params).json()

    lang_dict = langs['langs']

    for lang_id, lang_name in lang_dict.items():
        if language_name == lang_name:
            response = lang_id
            break
        else:
            response = 'Язык не найден'
    return response


# выполняем функцию для проверки декоратора
get_lang_id('Немецкий')