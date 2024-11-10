"""Модуль с функциями для работы с исключениями"""

from exceptions import NegativeValueError, InvalidParameterError, InvalidDataError


# Задание 1
def return_positive(x):
    """Возвращает положительное число, выбрасывает исключение, если отрицательное"""
    if x < 0:
        raise ValueError("число x не может быть отрицательным")

    return x


def divide_numbers(x, y):
    """Делит два числа, выбрасывает исключение, если делитель равен 0"""
    if y == 0:
        raise ZeroDivisionError("число y не может быть равно 0")

    return x / y


# Задание 2
def convert_to_int(value):
    """Конвертирует значение в целое число"""
    try:
        return int(value)
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        return None


# Задание 3
def get_element_from_list(lst, index):
    """Возвращает элемент списка по индексу"""
    try:
        return lst[index]
    except Exception as e:
        print(f"Ошибка доступа к элементу списка: {e}")
        return None
    finally:
        print("Завершение работы функции")


# Задание 4
def calculate_square_root(value):
    """Вычисляет квадратный корень"""
    try:
        if value < 0:
            raise ValueError("Отрицательное число")
        return value ** 0.5
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None
    except TypeError:
        print("Ошибка: значение должно быть числом")
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def safe_division(a, b):
    """Делит два числа"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        return None
    except TypeError:
        print("Ошибка: a и b должны быть числами")
        return None
    except ValueError:
        print("Ошибка: некорректные значения")
        return None
    finally:
        print("Завершение работы функции")


def validate_string_length(s, max_length):
    """Проверяет длину строки"""
    try:
        if not isinstance(s, str):
            raise TypeError("s должно быть строкой.")
        if len(s) > max_length:
            raise IndexError("Длина строки превышает допустимую")
        return s
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None
    except IndexError as e:
        print(f"Ошибка: {e}")
        return None
    except TypeError:
        print("Ошибка: максимальная длина должна быть числом")
        return None


# Задание 5
def process_data(data):
    """Обрабатывает данные"""
    try:
        if not isinstance(data, list):
            raise TypeError("data должно быть списком")
        for item in data:
            if item < 0:
                raise ValueError("Отрицательное число")
            print(f"Обработка элемента: {item}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение работы функции")


# Задание 7
def process_data_v2(data):
    """Обрабатывает данные v2"""
    try:
        if not isinstance(data, list):
            raise InvalidDataError("data должно быть списком")
        for item in data:
            if item < 0:
                raise NegativeValueError("Отрицательное число")
            print(f"Обработка элемента: {item}")
    except NegativeValueError as e:
        print(f"Ошибка: {e}")
    except InvalidDataError as e:
        print(f"Ошибка: {e}")


# Задание 8
def print_string(s):
    """Выводит строку, выбрасывает исключение при пустой строке"""
    if not s:
        raise InvalidParameterError("Строка не должна быть пустой.")
    print(s)


def print_number(x):
    """Выводит число, выбрасывает исключение при отрицательном значении"""
    if x < 0:
        raise NegativeValueError("Число не может быть отрицательным.")
    print(x)


def print_data(data):
    """Выводит данные"""
    if not isinstance(data, dict):
        raise InvalidDataError("Данные должны быть словарем.")

    for key, value in data.items():
        print(f"{key}: {value}")
