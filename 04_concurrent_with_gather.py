import asyncio
import time
async def say_hello(delay: int, what: str):
    await asyncio.sleep(delay)
    print(f"Hello {what}")

async def main():
    time_start = time.time()
    await asyncio.gather(
        say_hello(1, "world"),
        say_hello(2, "something else"),
    )

    end_time = time.time()
    print(f"exec time = {end_time - time_start}")  # 2 seconds

asyncio.run(main())