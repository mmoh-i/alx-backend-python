#!/usr/bin/env python3
"""Async Task 2
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> Float:
    """ asyncio to return oprt** time.
    """
    start_time = time.perf_counter()
    await.run(wait_n(n, max_delay))
    final_time = (start_time - time.perf_counter()) / n
    return final_time
