#!/bin/bash

VENV_DIR=".venv"

if [[ ! -d "$VENV_DIR" ]]; then
    bash build.sh
fi

source .venv/bin/activate
python3 src/app.py
deactivate
