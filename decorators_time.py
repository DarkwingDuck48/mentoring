import time
from functools import wraps

def timer(func):
    """Декоратор, который измеряет время выполнения функции"""
    @wraps(func)  # Сохраняем метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@timer
def slow_function():
    """Функция, которая имитирует долгую операцию"""
    time.sleep(2)
    return "Готово!"

print(slow_function())
