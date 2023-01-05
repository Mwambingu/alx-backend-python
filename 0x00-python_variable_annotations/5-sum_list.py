#!/usr/bin/env python3
"""
Contains function that takes a list of floats and
returns the sum of the floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function that takes a list of floats and
    returns the sum of the floats."""
    sum_of_n: float = 0.0
    for n in input_list:
        sum_of_n += n

    return sum_of_n
