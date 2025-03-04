"""
TODO:

foo should accept a list argument, whose elements are string.
"""
from typing import List

def foo(x: List[str]):
    pass

foo(["foo", "bar"])
foo(["foo", 1])  # expect-type-error