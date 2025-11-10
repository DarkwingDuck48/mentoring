from turtle import circle
from typing import Protocol, TypeAlias, Union


# Протокол определяет интерфейс (как interface в других языках)
class HasArea(Protocol):
    @property
    def area(self) -> float: ...


class HasPerimeter(Protocol):
    def perimeter(self) -> float: ...


# Классы, реализующие протоколы
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14159 * self.radius**2


# Функции, работающие с протоколами
def print_area(shape: HasArea) -> None:
    print(f'Area: {shape.area}')


# В случае, если мы хотим, чтобы функция принимала оба протокола - создаем общий протокол
class ShapeProtocol(HasArea, HasPerimeter, Protocol):
    """Объединяет оба протокола"""

    pass


def print_shape_info(shape: ShapeProtocol) -> None:
    print(f'Area: {shape.area}, Perimeter: {shape.perimeter()}')


if __name__ == '__main__':
    rec = Rectangle(10, 10)
    print_shape_info(rec)
    circle = Circle(10)
    print_shape_info(circle)
