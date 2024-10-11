#!/bin/sh
set -x

export SIMPLE_SETTINGS=settings

poetry run python graph_processing/app.py worker --web-port=$WORKER_PORT