#!/usr/bin/python3 env 
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """asynchronous function
    wait to delay randomly base on
    the range of arg passed
    """
    rndm_time = random.random() * max_delay
    await asyncio.sleep(rndm_time)
    
    return rndm_time
