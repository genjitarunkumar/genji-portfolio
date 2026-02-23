#!/bin/bash
python manage.py migrate --noinput
python seed_data.py
gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:8000
