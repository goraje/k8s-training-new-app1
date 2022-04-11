from typing import Optional

import typer
import uvicorn

from project_x.settings.base import SETTINGS

app = typer.Typer()

CFG_WATCH = typer.Option(False, help="Watch for config file changes.")


@app.command()
def serve(config_watch: bool = CFG_WATCH):
    """Start serving the application."""
    if config_watch:
        uvicorn.run(
            "project_x.main:app",
            host=SETTINGS.uvicorn_host,
            port=SETTINGS.uvicorn_port,
            log_level=SETTINGS.uvicorn_log_level,
            reload=True,
            reload_dirs="/project-x/config",
            reload_includes="*.toml",
        )
    else:
        uvicorn.run(
            "project_x.main:app",
            host=SETTINGS.uvicorn_host,
            port=SETTINGS.uvicorn_port,
            log_level=SETTINGS.uvicorn_log_level,
        )


@app.callback()
def dummy():
    """The command line interface for Project X."""
