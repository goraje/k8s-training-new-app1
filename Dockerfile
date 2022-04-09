FROM python:3.10

RUN mkdir -p /project-x

COPY . /project-x

WORKDIR /project-x

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry install \
    && curl -sSL https://install.python-poetry.org | python3 - --uninstall

HEALTHCHECK --start-period=5s --interval=5s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "project_x.main:app", "--host", "0.0.0.0", "--port", "8000"]
