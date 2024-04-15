"""Summing the elements of a list using different loops."""
__author__ = "730670116"


def w_sum(vals: list[float]) -> float:
    """While loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1 
    return (sum)


def f_sum(vals: list[float]) -> float:
    """For loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return (sum)


def f_range_sum(vals: list[float]) -> float:
    """For loop with range."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return (sum)