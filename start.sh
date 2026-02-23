#!/bin/bash
python manage.py migrate --noinput
gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:8000
