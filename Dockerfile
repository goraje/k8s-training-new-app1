FROM python:3.10

RUN mkdir -p /project-x

COPY . /project-x

WORKDIR /project-x

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry install \
    && curl -sSL https://install.python-poetry.org | python3 - --uninstall

CMD ["project-x", "serve"]
