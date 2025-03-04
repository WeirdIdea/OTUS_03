"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""
from typing import TypeVar
from typing import List
from typing import assert_type

TV = TypeVar('TV')

def add(a: TV, b: TV) -> TV:
    pass

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
assert_type(add(1, "2"), int)  # expect-type-error