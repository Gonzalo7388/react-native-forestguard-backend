# ubicaciones/views.py
from rest_framework import generics
from .models import Ubicacion
from .serializers import UbicacionSerializer

class UbicacionListCreateView(generics.ListCreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
