from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .models import Event, Application
from stadiums.models import Seat
from .serializers import EventSerializer, ApplicationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    @action(detail=False, methods=['get'])
    def admin(self, request):
        admin_id = request.query_params.get('id')
        print(admin_id)
        
        if admin_id:
            data = self.queryset.filter(administrator=admin_id)
        else:
            data = self.queryset.all()
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        seat_ids = request.data.get('seats', [])

        seats = Seat.objects.filter(pk__in=seat_ids)

        application = serializer.instance
        application.seats.set(seats)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def event(self, request):
        event_id = request.query_params.get('id')
        
        if event_id:
            data = self.queryset.filter(event=event_id)
        else:
            data = self.queryset.all()
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)