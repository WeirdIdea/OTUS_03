"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar

DecoratorType = TypeVar("DecoratorType", bound=Callable)

def decorator(func: DecoratorType) -> DecoratorType:
    return func

@decorator
def foo(a: int, *, b: str) -> None:
    pass

@decorator
def bar(c: int, d: str) -> None:
    pass

foo(1, b="2")
bar(c=1, d="2")
foo(1, "2")  # expect-type-error
foo(a=1, e="2")  # expect-type-error
decorator(1)  # expect-type-error