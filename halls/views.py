from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hall, Seat
from .serializers import HallSerializer, SeatSerializer

class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HallSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SeatSerializer