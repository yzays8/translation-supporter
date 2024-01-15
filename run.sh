#!/bin/bash

set -eu

readonly VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    bash build.sh
fi

source $VENV_DIR/bin/activate
python3 src/main.py
deactivate
