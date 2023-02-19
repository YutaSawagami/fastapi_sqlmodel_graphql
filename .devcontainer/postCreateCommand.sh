#!/bin/bash
apt update
apt install -y git curl
pip install poetry
poetry install --no-root
