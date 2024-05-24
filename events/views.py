from rest_framework import viewsets
from .models import Event
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer, ApplicationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationSerializer