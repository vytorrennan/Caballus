#!/usr/bin/env bash

scripts/wait-for-it.sh db:5432 -t 30
uv run manage.py migrate --no-input
uv run manage.py collectstatic --no-input
uv run createSuperUser.py
uv run manage.py runserver 0.0.0.0:8000
