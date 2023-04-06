#!/usr/bin/env python3
"""0. Async Generator
"""
import asyncio
import random


async def async_generator():
    """Coroutine that takes
    no arguments
    """
    for i in random.randint(0, 10):
        await.sleep(1)
        yield i
