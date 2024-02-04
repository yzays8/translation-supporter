#!/bin/bash

set -eu
cd "$(dirname "$0")"

readonly VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    bash setup.sh
fi

source $VENV_DIR/bin/activate
cd src
python3 main.py
deactivate
