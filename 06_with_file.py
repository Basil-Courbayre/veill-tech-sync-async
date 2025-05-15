import asyncio
from fastapi import Depends, FastAPI, File, Request, UploadFile
import time
import uvicorn
app = FastAPI()

@app.post("/ping_not_working")
async def ping_not_working(file: UploadFile = File(...)):
    print("Hello")
    try:
        contents = await file.read()
        time.sleep(5) # Or another cpu bound task
    finally:
        await file.close()
    print("bye")
    return "pong"


@app.post("/ping_bytes")
def ping_bytes(contents: bytes = File(...)):
    print("Hello")
    #contents = await file.read()
    time.sleep(5)
    #res = cpu_bound_task(contents)  # this would block the event loop
    print("bye")
    return "pong"


@app.post("/ping_no_await")
def ping_no_await(file: UploadFile = File(...)):
    print("Hello")
    try:
        contents = file.file.read()
        time.sleep(5)
        #res = cpu_bound_task(contents)  # this would block the event loop
    finally:
        file.file.close()
    print("bye")
    return "pong"


async def get_body(request: Request):
    print("Hello")
    return await request.body()

@app.post("/ping_with_await")
def ping_with_await(body: bytes = Depends(get_body)):
    print("New request arrived.")
    time.sleep(3)
    print("bye")
    return body[100:200]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8200)
