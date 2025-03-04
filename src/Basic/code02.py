"""
TODO:

foo should accept a dict argument, both keys and values are string.
"""
from typing import Dict

def foo(x: Dict[str, str]):
    pass

foo({"foo": "bar"})
foo({"foo": 1})  # expect-type-error

