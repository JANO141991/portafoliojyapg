#!/usr/bin/env bash
# exit on error
set -o errexit
pip install -r requeriments.txt
poetry install

python manage.py collectstatict --no-input
python manage.py migrate 