#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Callable to return functioin when the make_multiplier
    function is called, it takes float multiplier as args
    :multiplier: float
    '''
    return lambda x: x*multiplier
