"""
Create a method that accepts a list and an item,
and returns true if the item belongs to the list, otherwise false.
"""
from typing import Any


def include(arr: list, item: Any) -> bool:
    return item in arr or False
