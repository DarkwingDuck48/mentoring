def format_name(name: str) -> str:
    return f'{name}'


def use_me():
    return 42


def some_private() -> bool:
    return True


__all__ = ['format_name', 'use_me']
