FROM ghcr.io/astral-sh/uv:python3.11-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update
RUN apk add --no-cache \
    bash \
    postgresql-client \
    postgresql-dev \
    pkgconfig \
    git \
    gcc \
    libcurl \
    python3-dev \
    gpgme-dev \
    libc-dev

WORKDIR /caballus

COPY ./ ./

RUN uv sync --frozen

EXPOSE 8000
