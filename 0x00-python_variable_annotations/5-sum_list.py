#!/usr/bin/env python3
""" 5. Complex types - list of floats """
from typing import List


def sum_list(inputlist: List[float]) -> float:
    """
    performs a sum operation
    Args:
        input_list (list[float]): Takes in a list of floating numbers

    Returns:
        float: returns floats as the result
    """
    return sum(inputlist)
