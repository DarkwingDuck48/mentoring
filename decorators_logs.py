from functools import wraps

def logger(func):
    """Декоратор для логирования вызовов функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def calculate(a, b, operation='add'):
    if operation == 'add':
        return a + b
    elif operation == 'multiply':
        return a * b

calculate(5, 3, operation='multiply')
# Вывод:
# Вызов функции: calculate
# Аргументы: args=(5, 3), kwargs={'operation': 'multiply'}
# Результат: 15