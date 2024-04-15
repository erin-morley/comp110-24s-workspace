"""Recursion CQ."""


def f(n: int, k: int) -> int:
    """Recursion function."""
    if n == 0: 
        return 0
    else: 
        return f(n - 1, k) + k