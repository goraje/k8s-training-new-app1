import asyncio
import json
import logging
import random
from functools import partial, wraps

import aiofiles
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, Response

app = FastAPI()
logger = logging.getLogger("uvicorn.error")


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_running_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run


async_json_loads = async_wrap(json.loads)


@app.get("/health")
async def perform_healthcheck():
    return Response(status_code=status.HTTP_200_OK)


@app.get("/greet")
async def greet_someone(name: str):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"greeting": f"Hello, {name}! Welcome to Project X."},
    )


@app.get("/quote")
async def send_some_quote():
    async with aiofiles.open("/mnt/quotes.json", mode="r") as f:
        quotes = await async_json_loads(await f.read())
    return JSONResponse(status_code=status.HTTP_200_OK, content=random.choices(quotes)[0])
