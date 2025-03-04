"""
TODO:

Define a generic class that represents a stack.
It can be instantiated with a certain type, with method `push` accepting an object of the specified type,
and `pop` returning an object of the same type
"""
from typing import TypeVar, Generic
from typing import assert_type

TV = TypeVar('TV')

class Stack(Generic[TV]):
    def __init__(self) -> None:
        self.items = []

    def push(self, item: TV) -> None:
        self.items.append(item)

    def pop(self) -> TV:
        return self.items.pop()


s = Stack[int]()
s.push(1)
assert_type(s.pop(), int)
s.push("foo")  # expect-type-error
assert_type(s.pop(), str)  # expect-type-error
