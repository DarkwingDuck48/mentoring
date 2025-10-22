from functools import wraps


class CountCalls:
    """Декоратор как класс, который считает вызовы функции"""
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        wraps(func)(self)  # Сохраняем метаданные

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Вызов #{self.num_calls} функции {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Вызов #1 функции say_hello
say_hello()  # Вызов #2 функции say_hello
print(f"Всего вызовов: {say_hello.num_calls}")  # 2