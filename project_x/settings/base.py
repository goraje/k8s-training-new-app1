import os
import pathlib

import tomlkit
from pydantic import BaseSettings, Field


class ProjectXSettings(BaseSettings):
    uvicorn_host: str = Field(default="127.0.0.1", env="PROJECT_X_UVICORN_HOST")
    uvicorn_port: int = Field(default=8000, env="PROJECT_X_UVICORN_PORT")
    uvicorn_log_level: str = Field(default="info", env="PROJECT_X_UVICORN_LOG_LEVEL")


if os.environ.get("PROJECT_X_CONFIG_PATH"):
    with pathlib.Path(str(os.environ.get("PROJECT_X_CONFIG_PATH"))).open("r") as f:
        cfg = tomlkit.parse(f.read())
    SETTINGS = ProjectXSettings(
        uvicorn_host=cfg["project-x"]["uvicorn"]["host"],  # type: ignore
        uvicorn_port=cfg["project-x"]["uvicorn"]["port"],  # type: ignore
        uvicorn_log_level=cfg["project-x"]["uvicorn"]["log-level"],  # type: ignore
    )
else:
    SETTINGS = ProjectXSettings()
