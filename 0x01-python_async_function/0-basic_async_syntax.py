import asyncio
import random


async def wait_random(max_delay=10):
    i = random.uniform(0, max_delay + 1)
    await asyncio.sleep(i)
    #print(max_delay)

async def main():
    return await wait_random()

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{elapsed:.15f}")
