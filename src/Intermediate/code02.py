"""
TODO:

Define a callable type that accepts a string argument and returns None.
*The parameter name can be arbitrary.*
"""
from collections.abc import Callable # вызываемый

SingleStringInput = Callable[[str], None]

def accept_single_string_input(func: SingleStringInput) -> None:
    pass

def string_name(name: str) -> None:
    pass

def string_value(value: str) -> None:
    pass

def int_value(value: int) -> None:
    pass

def new_name(name: str) -> str:
    return name

accept_single_string_input(string_name)
accept_single_string_input(string_value)
accept_single_string_input(int_value)  # expect-type-error
accept_single_string_input(new_name)  # expect-type-error
