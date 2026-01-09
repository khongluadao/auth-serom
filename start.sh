#!/bin/bash
set -e

echo "Pulling latest code..."
git pull

echo "Starting Python app..."
exec ./.venv/bin/python app.py
