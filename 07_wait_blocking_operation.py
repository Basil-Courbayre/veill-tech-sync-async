import asyncio
from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
import uvicorn
import time
from functools import partial
app = FastAPI()

from loguru import logger


def cpu_bound_task():
    print("Hello\n")
    time.sleep(5)
    print("bye\n")
    return "After the call"


def cpu_bound_task_2(param):
    print(param)
    print("Hello\n")
    time.sleep(5)
    print("bye\n")
    return "returned value"

@app.post("/ping_threadpool")
async def ping_threadpool():
    print("Before the call")
    res = await run_in_threadpool(cpu_bound_task)
    return res


@app.post("/ping_run_in_executor")
async def ping_run_in_executor():
    print("Before the call")
    loop = asyncio.get_running_loop()
    res = await loop.run_in_executor(None, cpu_bound_task)
    return res

@app.post("/ping_run_in_executor_partial")
async def ping_run_in_executor_partial():
    print("Before the call")
    loop = asyncio.get_running_loop()
    res = await loop.run_in_executor(None, partial(cpu_bound_task_2, param="1"))
    print("After the call")
    return res


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8200)
