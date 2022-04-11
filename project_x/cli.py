import typer
import uvicorn

from project_x.settings.base import SETTINGS

app = typer.Typer()


@app.command()
def serve():
    """Start serving the application."""
    uvicorn.run(
        "project_x.main:app",
        host=SETTINGS.uvicorn_host,
        port=SETTINGS.uvicorn_port,
        log_level=SETTINGS.uvicorn_log_level,
    )


@app.callback()
def dummy():
    """The command line interface for Project X."""
