import os
import sys

# Vercel requires adding the root directory to the sys path so it can resolve portfolio_site and apps
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
