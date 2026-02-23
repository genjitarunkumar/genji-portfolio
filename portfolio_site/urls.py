from django.contrib import admin
from django.urls import path, include

from projects_app.views import projects_list

urlpatterns = [
    path('', projects_list, name='home'),
    path('admin/', admin.site.urls),
    path('projects/', include('projects_app.urls')),
    path('api/', include('api_app.urls')),
]

