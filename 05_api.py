import json
from fastapi import FastAPI, Request
import time
from fastapi.responses import JSONResponse
import uvicorn
import asyncio
app = FastAPI()

@app.get("/ping_async")
async def ping_async(request: Request):
    print("Hello")
    time.sleep(5)
    print("bye")
    return "pong"

@app.get("/ping_sync")
def ping_sync(request: Request):
    print("Hello")
    time.sleep(5)
    print("bye")
    return "pong"

@app.get("/ping_asyncio")
async def ping_asyncio(request: Request):
    print("Hello")
    await asyncio.sleep(5)
    print("bye")
    return "pong"


@app.get("/ping_asyncio_no_wait")
async def ping_asyncio_no_wait(request: Request):
    print("Hello")
    asyncio.sleep(5)
    print("bye")
    return "pong"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8200)
