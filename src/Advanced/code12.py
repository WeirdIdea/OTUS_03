"""
TODO:

Add type annotations to the class `Wrap`, so that it can be called with the
same arguments as the function it wraps.
"""
from typing import Callable, TypeVar, ParamSpec, Generic

TV = TypeVar('TV')
Par = ParamSpec('Par')

class Wrap(Generic[TV, Par]):
    def __init__(self, func: Callable[Par, TV]) -> None:
        self.func = func

    def __call__(self, *args: Par.args, **kwargs: Par.kwargs) -> TV:
        return self.func(*args, **kwargs)

from typing import assert_type

@Wrap
def add(a: int, b: int) -> int:
    return a + b

@Wrap
def replace_wildcard(string: str, replacement: str, *, count: int = -1) -> str:
    return string.replace("*", replacement, count)

assert_type(add(1, 2), int)
assert_type(replace_wildcard("Hello *", "World"), str)
assert_type(replace_wildcard("Hello *", "World", count=1), str)
replace_wildcard("Hello *", 1)  # expect-type-error
replace_wildcard("Hello *", "World", 1)  # expect-type-error