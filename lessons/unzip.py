"""Splitting a dictionary into two lists."""
__author__ = "730670116"


def get_keys(dict1: dict[str, int]) -> list[str]:
    """Get keys function."""
    if len(dict1) == 0:
        return ([])
    list1: list[str] = []
    for key in dict1:
        list1.append(key)
    return list1


def get_values(dict1: dict[str, int]) -> list[int]:
    """Get values function."""
    if len(dict1) == 0:
        return ([])
    list2: list[int] = []
    for key in dict1:
        list2.append(dict1[key])
    return list2