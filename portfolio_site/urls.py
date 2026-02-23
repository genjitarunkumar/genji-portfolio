from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects_app.urls')),
    path('accounts/', include('accounts_app.urls')),
    path('contact/', include('contact_app.urls')),
    path('api/', include('api_app.urls')),
]
