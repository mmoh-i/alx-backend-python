#!/usr/bin/env python3
"""0. Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """Coroutine that takes
    no arguments
    """
    for i in range(10):

        await asyncio.sleep(1)
        yield random.uniform(0, 10)
