#!/bin/bash

set -eu
cd "$(dirname "$0")"

readonly VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv .venv
fi

source $VENV_DIR/bin/activate
pip3 install -r requirements.txt
deactivate
