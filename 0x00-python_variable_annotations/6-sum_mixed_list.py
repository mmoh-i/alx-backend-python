#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''function to accept a list with both
       int and float dat types and
       float sum of objects in mxd_lst
    '''
    return sum(mxd_lst)
