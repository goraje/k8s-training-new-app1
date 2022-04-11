import logging

import aiofiles
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, Response

app = FastAPI()
logger = logging.getLogger("uvicorn.error")


@app.get("/health")
async def perform_healthcheck():
    return Response(status_code=status.HTTP_200_OK)


@app.get("/greet")
async def greet_someone(name: str):
    logger.debug("Greeting request received for name: %s", name)
    async with aiofiles.open("/mnt/greet_command.log", "a") as f:
        await f.write(f"Greeting for {name}.\n")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"greeting": f"Hello, {name}! Welcome to Project X."},
    )
