"""Functions that implement sorting algorithms."""

__author__ = "730670116"

import numpy as np
import timeit
import tracemalloc

MAX_VAL: int = 10 ** 5

def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for idx in range(len(x)):
        min_idx = idx
        for elem in range(idx + 1, len(x)):
            if x[elem] < x[min_idx]:
                min_idx = elem
        x[idx], x[min_idx] = x[min_idx], x[idx]
    return None


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm
    Insert into an already sorted list."""
    for sorted_idx in range(1, len(x)): # start loop from second index
        current_elem = x[sorted_idx]
        unsorted_idx = sorted_idx
        while unsorted_idx > 0 and x[unsorted_idx - 1] > current_elem:
            x[unsorted_idx] = x[unsorted_idx - 1]
            unsorted_idx -= 1
        x[unsorted_idx] = current_elem
    return None

