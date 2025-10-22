from functools import wraps

def cache(func):
    """Декоратор для кэширования результатов функции"""
    cache_dict = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache_dict:
            print(f"Возвращаем кэшированный результат для {args}")
            return cache_dict[args]
        else:
            print(f"Вычисляем результат для {args}")
            result = func(*args)
            cache_dict[args] = result
            return result
    return wrapper

@cache
def fibonacci(n):
    """Вычисляет n-ное число Фибоначчи"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))