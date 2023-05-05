#!/usr/bin/env python3
"""Task 1 module"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async function that spawns n tasks of the wait_random function with the
    specified max_delay and returns a list of
    all the delays in ascending order.

    Parameters:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum number of seconds to delay.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = []
    # spawn n tasks that each call wait_random with max_delay as an argument
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    delays = []
    # wait for each task to complete and append the resulting delay to the delays list
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    # return the delays list in ascending order
    return sorted(delays)
