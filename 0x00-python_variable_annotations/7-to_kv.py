#!/usr/bin/env python3
"""
Contains function to_kv that takes a string k and an int OR float v as arguments and returns a tuple
"""
from typing import Union, Optional


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """Function to_kv that takes a string k and an int OR float v as arguments and returns a tuple"""
    return (k, v * v)
