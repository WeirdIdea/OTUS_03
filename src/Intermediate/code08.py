"""
TODO:

The function `add` accepts one argument and returns a value, they all have the same type.
The type can only be int or subclasses of int.
"""
from typing import TypeVar
from typing import assert_type

Integer = TypeVar('Integer', bound=int)

def add(a: Integer) -> Integer:
    pass

class MyInt(int):
    pass

assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
assert_type(add("1"), str)  # expect-type-error
add(["1"], ["2"])  # expect-type-error
add("1", 2)  # expect-type-error