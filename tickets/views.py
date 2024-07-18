from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from datetime import datetime
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.created_date = datetime.today()
        instance.save() 
        return instance

    @action(detail=False, methods=['get'])
    def application(self, request):
        application_id = request.query_params.get('id')
        
        if application_id:
            data = self.queryset.filter(application=application_id)
        else:
            return Response({'error': 'Application id was not provided.'}, status=status.HTTP_400_BAD_REQUEST) 
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)