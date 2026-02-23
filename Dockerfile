FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run collectstatic
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "portfolio_site.wsgi:application", "--bind", "0.0.0.0:8000"]
