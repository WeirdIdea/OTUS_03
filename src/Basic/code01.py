"""
TODO:

Modify `foo` so it takes an argument of arbitrary type.
"""

from typing import Union

def foo(x: Union[int, str]):
    """⬆️ Change me. No need to implement the function."""
    pass

foo(1)
foo("10")
foo(1, 2)  # expect-type-error
