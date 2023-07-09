#!/bin/bash

VENV_DIR=".venv"

if [[ ! -d "$VENV_DIR" ]]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
pip3 install -r requirements.txt
deactivate
