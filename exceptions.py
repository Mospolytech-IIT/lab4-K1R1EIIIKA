"""Модуль с пользовательскими исключениями."""


# Задание 6
class InvalidParameterError(Exception):
    """Выбрасывается, когда передается неверный параметр."""


class NegativeValueError(Exception):
    """Выбрасывается, когда значение отрицательное."""


class InvalidDataError(Exception):
    """Выбрасывается, когда данные некорректны."""
