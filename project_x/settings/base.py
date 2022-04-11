from pydantic import BaseSettings, Field


class ProjectXSettings(BaseSettings):
    uvicorn_host: str = Field(default="127.0.0.1", env="PROJECT_X_UVICORN_HOST")
    uvicorn_port: int = Field(default=8000, env="PROJECT_X_UVICORN_PORT")
    uvicorn_log_level: str = Field(default="info", env="PROJECT_X_UVICORN_LOG_LEVEL")


SETTINGS = ProjectXSettings()
