#!/usr/bin/env python3
"""
Contains a function that takes a list of mixed
integers and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """function that takes a list of mixed
    integers and floats and returns their sum as a float"""
    sum_of_mxd_list: float = 0.0

    for n in mxd_lst:
        sum_of_mxd_list += n

    return sum_of_mxd_list
