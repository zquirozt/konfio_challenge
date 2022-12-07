FROM python:3.10.5-slim as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10.5-slim

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN apt-get update && apt-get -y install libpq-dev gcc git

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .
