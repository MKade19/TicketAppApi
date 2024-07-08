from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    # @action(detail=False, methods=['get'])
    # def application_seat(self, request):
    #     event_id = request.query_params.get('id')
        
    #     if event_id:
    #         data = self.queryset.filter(event=event_id)
    #     else:
    #         data = self.queryset.all()
        
    #     serializer = self.serializer_class(data, many=True)
    #     return Response(serializer.data)