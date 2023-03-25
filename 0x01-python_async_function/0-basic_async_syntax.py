#!/usr/bin/env python3
""" Async Task 0.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds.
    """
    wait_time = random.randint(0, max_delay + 1)
    await asyncio.sleep(wait_time)
    return wait_time
