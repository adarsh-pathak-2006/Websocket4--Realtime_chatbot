#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Run migrations to ensure the database is up to date
python manage.py migrate

# (Optional) Collect static files if you add them later
# python manage.py collectstatic --no-input
