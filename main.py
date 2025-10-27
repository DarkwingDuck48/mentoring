import sys

from utils import format_name, get_component, use_me

print(format_name('hello'))

print(use_me())


component = get_component()

for obj in sys.path:
    print(obj)
