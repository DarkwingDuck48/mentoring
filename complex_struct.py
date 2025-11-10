from typing import NamedTuple, TypedDict


# TypedDict для словарей с фиксированными ключами
class UserProfile(TypedDict):
    name: str
    age: int
    email: str
    is_active: bool


def create_user_profile() -> UserProfile:
    return {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'is_active': True}


# NamedTuple для именованных кортежей
class Point(NamedTuple):
    x: float
    y: float
    z: float = 0.0  # Значение по умолчанию


def calculate_distance(p1: Point, p2: Point) -> float:
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
