"""EX04 List Utils."""
__author__ = "730670116"


def all(num_list: list[int], int1: int) -> bool:
    """All function."""
    idx: int = 0
    if len(num_list) == 0:
        return False
    while idx < len(num_list):
        if num_list[idx] != int1:
            return False
        else:
            idx += 1
    return True


def max(input: list[int]) -> int:
    """Max function."""
    if len(input) == 0:
        raise ValueError("max() arg is and empty List")
    idx: int = 0
    max_num: int = input[0]
    while idx < len(input):
        if input[idx] > max_num:
            max_num = input[idx]
        idx += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Is equal function."""
    idx: int = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True


def extend(list_a: list[int], list_b: list[int]) -> None:
    """Extend function."""
    idx: int = 0
    while idx < len(list_b):
        list_a.append(list_b[idx])
        idx += 1
