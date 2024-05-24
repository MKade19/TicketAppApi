from rest_framework import viewsets
from .models import Hall
from .serializers import HallSerializer

class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = HallSerializer
