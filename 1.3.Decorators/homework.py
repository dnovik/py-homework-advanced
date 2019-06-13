
from datetime import datetime
from homework_files import file, add_to_recipes

FILE_TO_WRITE = r'logger.txt'


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


raise_to_pow(11)


# ЗАДАНИЕ 2

def logger(func):


    def get_func_info(*args):
        func_name = func.__name__
        func_time = datetime.now()
        func_args = args
        func_result = func(args[0])

        with open(args[1], 'w', encoding='utf-8') as logger_file:
            logger_file.write(f'Имя функции: {func_name}\n')
            logger_file.write(f'Дата и время запуска функции: {func_time}\n')
            logger_file.write(f'Аргументы функции: {func_args}\n')
            logger_file.write(f'Результат функции: {func_result}\n')

    return get_func_info


@logger
def raise_to_pow(num):
    result = num ** 2
    return result


raise_to_pow(11, FILE_TO_WRITE)

# ЗАДАНИЕ 3
@logger
add_to_recipes(file)
