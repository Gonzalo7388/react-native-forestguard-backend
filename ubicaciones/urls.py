# ubicaciones/urls.py
from django.urls import path
from .views import UbicacionListCreateView

urlpatterns = [
    path('ubicaciones/', UbicacionListCreateView.as_view(), name='ubicaciones-list-create'),
]
