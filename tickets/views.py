from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer