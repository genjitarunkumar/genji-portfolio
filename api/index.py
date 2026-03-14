import os
import sys
import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# Vercel requires adding the root directory to the sys path so it can resolve portfolio_site and apps
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")

django.setup()

# Run migrations at startup to ensure /tmp/db.sqlite3 is initialized in every cold start
try:
    call_command("migrate", interactive=False)
except Exception as e:
    print(f"Migration error during startup: {e}")

app = get_wsgi_application()
