#!/usr/bin/env python3
"""Task 9 Adding annotation to function"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns an a list"""
    x = [(i, len(i)) for i in lst]
    return x
