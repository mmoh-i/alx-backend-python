#!/usr/bin/env python3
""" asyncio 4-Task.
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks.py').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns task_wait_random n times.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)