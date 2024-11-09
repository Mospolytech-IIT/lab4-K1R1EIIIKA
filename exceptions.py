# Задание 6
class InvalidParameterError(Exception):
    """Выбрасывается, когда передается неверный параметр."""
    pass


class NegativeValueError(Exception):
    """Выбрасывается, когда значение отрицательное."""
    pass


class InvalidDataError(Exception):
    """Выбрасывается, когда данные некорректны."""
    pass
