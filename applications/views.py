from rest_framework import viewsets
from .models import Event
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationSerializer