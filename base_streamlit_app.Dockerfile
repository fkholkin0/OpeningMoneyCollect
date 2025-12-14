FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=off \
    PIP_DEFAULT_TIMEOUT=10 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8


WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pipenv && \
    pipenv install --deploy --system --ignore-pipfile && \
    pipenv clean && \
    pip uninstall pipenv -y && \
    rm -f Pipfile.lock  

