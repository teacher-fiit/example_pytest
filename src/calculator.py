def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел."""
    return a + b

def divide(a: float, b: float) -> float:
    """Возвращает результат деления. Вызывает ошибку при делении на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def sub(a: float, b: float) -> float:
    """Возвращает разность двух чисел."""
    return a - b