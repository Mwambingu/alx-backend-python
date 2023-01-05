#!/usr/bin/env python3
"""
Contains a function that takes a list of mixed
integers and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function that takes a list of mixed
    integers and floats and returns their sum as a float"""

    return float(sum(mxd_lst))
