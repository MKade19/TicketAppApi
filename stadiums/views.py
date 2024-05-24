from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import City, Stadium
from .serializers import CitySerializer, StadiumSerializer

class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StadiumSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CitySerializer
