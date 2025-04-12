# forestguard_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ubicaciones.urls')),  # <-- aquí se incluye
]


#ging freecss pingo123