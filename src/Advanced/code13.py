"""
TODO:
    Define a protocol for class `SupportsQuack` that supports a "quack" method.
"""
from typing import Protocolcode13.py

class SupportsQuack(Protocol):
    def quack(self) -> None:
        pass

class Duck:
    def quack(self) -> None:
        print("quack!")

class Dog:
    def bark(self) -> None:
        print("bark!")

duck: SupportsQuack = Duck()
dog: SupportsQuack = Dog()  # expect-type-error
