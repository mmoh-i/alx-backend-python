#!/usr/bin/env python3
"""2. Run time for four
parallel comprehensions
"""
import asyncio
import random
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension
    four times in parallele.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(5)])
    end_time = asyncio.get_event_loop().time() - start_time
    return end_time
