from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects_app.urls')),
    path('api/', include('api_app.urls')),
]
