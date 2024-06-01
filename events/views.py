from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Event, Application
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

    @action(detail=False, methods=['get'])
    def event(self, request):
        event_id = request.query_params.get('id')
        print(event_id)
        
        if event_id:
            data = self.queryset.filter(event=event_id)
        else:
            data = self.queryset.all()
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
