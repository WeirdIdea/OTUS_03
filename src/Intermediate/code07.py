"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""
from typing import TypeVar
from typing import assert_type

TV = TypeVar('TV', int, str)

def add(a: TV, b: TV) -> TV:
    pass

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"])  # expect-type-error
add("1", 2)  # expect-type-error