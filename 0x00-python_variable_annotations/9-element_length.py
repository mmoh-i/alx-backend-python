#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''element_lenght funtion takes in list arguments
    and returns list annotations
    '''
    return [(i, len(i)) for i in lst]
