FROM python:3.10-slim-buster

WORKDIR /app

COPY ./src /app
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry 
RUN poetry install
