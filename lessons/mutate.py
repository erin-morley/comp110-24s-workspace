"""Mutating functions."""

__author__ = "730670116"


def manual_append(list1: list[int], num: int) -> None:
    """Manual append function."""
    list1.append(num)


def double(list2: list[int]) -> None:
    """Double function."""
    index: int = 0
    while index < len(list2):
        list2[index] *= 2
        index += 1 