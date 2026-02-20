import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'tarunkumargenji@gmail.com', 'Tarun@94')
    print("Superuser 'admin' created with password 'Tarun@94'")
else:
    u = User.objects.get(username='admin')
    u.set_password('Tarun@94')
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print("Superuser 'admin' password updated to 'Tarun@94'")
