from rest_framework import viewsets
from .models import City
from .serializers import CitySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = CitySerializer