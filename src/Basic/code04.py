"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""
from typing import Union

def foo(**kwargs: Union[int, str]):
    pass

foo(a=1, b="2")
foo(a=[1])  # expect-type-error