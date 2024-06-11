from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Prefetch
from .models import City, Stadium, Hall, Seat
from events.serializers import ApplicationSerializer
from events.models import Event, Application
from authentication.models import User
from .serializers import CitySerializer, StadiumSerializer, SeatSerializer, HallSerializer


class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StadiumSerializer

    @action(detail=False, methods=['get'])
    def admin_applications(self, request):
        admin_id = request.query_params.get('adminId')
        
        if admin_id:
            h_qs = Hall.objects.prefetch_related(Prefetch('stadium', queryset=Stadium.objects.filter(administrator=admin_id)))
            e_ls = Event.objects.prefetch_related(Prefetch('hall', queryset=h_qs)).values_list('pk', flat=True)
            data = []

            for application in Application.objects.filter(event_id__in=e_ls):
                data.append(application)
        else:
            data = self.queryset.all()
        
        serializer = ApplicationSerializer(data, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CitySerializer


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
