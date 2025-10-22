# 1. Функции можно присваивать переменным
def greet(name):
    return f"Hello, {name}!"

my_function = greet  # Присваиваем функцию переменной
print(my_function("Alice"))  # "Hello, Alice!"

# 2. Функции можно передавать как аргументы
def call_twice(func, arg):
    """Вызывает функцию дважды с одним аргументом"""
    return func(arg) + " " + func(arg)

result = call_twice(greet, "Bob")
print(result)  # "Hello, Bob! Hello, Bob!"

# 3. Функции можно возвращать из функций
def create_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter  # Возвращаем функцию, а не результат!

hello = create_greeter("Hello")
print(hello("Charlie"))  # "Hello, Charlie!"



def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед вызовом функции")
        func()
        print("Что-то происходит после вызова функции")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Эквивалентно: say_hello = my_decorator(say_hello)

say_hello()