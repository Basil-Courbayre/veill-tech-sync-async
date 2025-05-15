import time

def say_hello(delay: int, what: str):
    time.sleep(delay)
    print(f"Hello {what}")

time_start = time.time()
say_hello(1, "world")
say_hello(2, "something else")
end_time = time.time()
print(f"exec time = {end_time - time_start}") # 3 seconds