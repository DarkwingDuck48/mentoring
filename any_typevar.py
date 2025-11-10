from enum import Enum
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


class TaskTypes(Enum):
    BUY = 'BUY'
    SELL = 'hello'

    def print_name(self):
        print(f'My value is - {self.value}')

    @classmethod
    def validate(cls, value):
        print(f'{cls._member_names_=}')
        if value not in cls._member_names_:
            print('Not found')
            return False


class Task:
    def __init__(self, name: str, task_type: TaskTypes) -> None:
        self.name = name
        self.task_type: TaskTypes = task_type

    def validate(self):
        values = [t.value for t in TaskTypes]
        return self.task_type in values


task_new = Task('Hello', TaskTypes.BUY)


if __name__ == '__main__':
    TaskTypes.validate('HELLO')
    TaskTypes.BUY.print_name()
    TaskTypes.SELL.print_name()
