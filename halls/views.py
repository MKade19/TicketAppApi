from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Hall, Seat
from .serializers import HallSerializer, SeatSerializer

class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HallSerializer

    @action(detail=False, methods=['get'])
    def stadium(self, request):
        stadium_id = request.query_params.get('id')
        
        if stadium_id:
            data = self.queryset.filter(stadium=stadium_id)
        else:
            data = self.queryset.all()
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SeatSerializer

    @action(detail=False, methods=['get'])
    def hall(self, request):
        hall_id = request.query_params.get('id')
        
        if hall_id:
            data = self.queryset.filter(hall=hall_id)
        else:
            data = self.queryset.all()
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
