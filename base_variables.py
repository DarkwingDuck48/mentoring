from typing import List, Dict, Set, Tuple, Optional, Union, Any

# Аннотации переменных
name: str = 'Alice'
age: int = 25
is_student: bool = True
scores: list[float] = [95.5, 87.0, 92.3]

# Коллекции (старый стиль для Python < 3.9)
names: List[str] = ['Alice', 'Bob']
scores_2: Dict[str, float] = {'Alice': 95.5, 'Bob': 87.0}
unique_ids: Set[int] = {1, 2, 3}
coordinates: Tuple[float, float] = (10.5, 20.3)

# Новый стиль (Python 3.9+)
names: list[str] = ['Alice', 'Bob']
scores_2: dict[str, float] = {'Alice': 95.5, 'Bob': 87.0}
unique_ids: set[int] = {1, 2, 3}
coordinates: tuple[float, float] = (10.5, 20.3)


# Аннотации функций
def greet(name: str) -> str:
    return f'Hello, {name}'


def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0


# Optional[T] = Union[T, None]
def find_user(user_id: int) -> Optional[str]:
    """Возвращает имя пользователя или None если не найден"""
    users = {1: 'Alice', 2: 'Bob'}
    return users.get(user_id)


# Union - несколько возможных типов
def process_value(value: Union[int, str, list]) -> Union[int, str]:
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    else:
        return str(value)


# Новый синтаксис (Python 3.10+)
def process_value_new(value: int | str | list) -> int | str:
    # Та же логика
    ...


# Args и Kwargs аннотации
def foo(*args: int, **kwargs: str):
    # для args (позиционных аргументов) указывается только один тип, который ожидаем получать
    # для kwargs (именованых аргументов) указывается только тип значения аргумента. Ключ ВСЕГДА будет типа str
    pass
