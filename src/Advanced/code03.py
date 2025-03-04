"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""
from collections.abc import Callable
from typing import TypeVar

TV = TypeVar("TV", bound=Callable)

def decorator(message: str) -> Callable[[TV], TV]:
    ...

@decorator(message="x")
def foo(a: int, *, b: str) -> None:
    ...

@decorator  # expect-type-error
def bar(a: int, *, b: str) -> None:
    ...

foo(1, b="2")
foo(1, "2")  # expect-type-error
foo(a=1, e="2")  # expect-type-error
decorator(1)  # expect-type-error