#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''to_kv functioin to return tuple with variables
    :k: type str and
    :v: to accept type in or float
    '''
    return (k, (v)**2)
