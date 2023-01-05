#!/usr/bin/env python3
"""
Contains a function that takes a float multiplier
as argument and returns a function that multiplies
a float by multiplier
"""
from typing import Callable, Optional


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that takes a float multiplier
    as argument and returns a function that multiplies
    a float by multiplier"""
    def func_mult(n):
        y = n
        return y * n
    return func_mult