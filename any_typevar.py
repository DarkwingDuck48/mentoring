from typing import Any, TypeVar


# Any - любой тип (отключает проверку)
def log_anything(data: Any) -> None:
    print(f'Logging: {data}')


# TypeVar для generic функций
T = TypeVar('T')  # Любой тип
U = TypeVar('U')  # Другой любой тип


def first_item(items: list[T]) -> T:
    return items[0]


def pair_items(a: T, b: U) -> tuple[T, U]:
    return (a, b)


# TypeVar с ограничениями
Number = TypeVar('Number', int, float)


def double_number(x: Number) -> Number:
    return x * 2
