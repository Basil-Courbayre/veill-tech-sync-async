
from fastapi import Depends, FastAPI, Request
from fastapi.responses import StreamingResponse

import uvicorn
import time
app = FastAPI()

from loguru import logger

def log_and_yield(message: str, level: str = "info") -> str:
    getattr(logger, level)(message)
    return message

async def ping():
    yield log_and_yield("Hello\n")
    time.sleep(2)
    yield log_and_yield("bye\n")


@app.post("/ping")
async def refresh_executions() -> StreamingResponse:
    return StreamingResponse(
        ping(),
        media_type="text/event-stream",
        headers={
            "Transfer-Encoding": "chunked",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8200)

executions_router = FastAPI()


@executions_router.post("/refresh")
async def refresh_executions() -> StreamingResponse:
    return StreamingResponse()