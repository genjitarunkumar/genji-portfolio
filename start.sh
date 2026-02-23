#!/bin/bash
python manage.py migrate --noinput
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell
gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:8000
