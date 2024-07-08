from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from datetime import date
from django.db.models import Prefetch

from .models import Event, Application
from stadiums.models import Seat, Stadium, Hall, City
from stadiums.serializers import HallSerializer, StadiumSerializer, CitySerializer
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
    

    @action(detail=False, methods=['get'])
    def recent_by_city(self, request):
        city_name = request.query_params.get('city')
        current_date = date.today()
        
        if city_name:
            st_ls = Stadium.objects.select_related('city').filter(city__name=city_name).values_list('pk')
            h_ls = Hall.objects.select_related('stadium').filter(stadium__in=st_ls).values_list('pk')

            e_qs = Event.objects.select_related('hall').filter(hall__in=h_ls)
            e_qs = e_qs.filter(date__gt=current_date).order_by('date')

            a_ls = Application.objects.filter(status='approved').values('event')
            data = []

            for event in e_qs.filter(pk__in=a_ls):
                data.append(event)
        else:
            e_qs = self.queryset.all().filter(date__gt=current_date).order_by('date')
            a_ls = Application.objects.filter(status='approved').values('event')
            data = []

            for event in e_qs.filter(pk__in=a_ls):
                data.append(event)
        
        serializer = EventSerializer(data, many=True)
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
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.created_date = date.today()
        instance.save() 
        return instance

    @action(detail=False, methods=['get'])
    def event(self, request):
        event_id = request.query_params.get('id')
        
        if event_id:
            data = self.queryset.filter(event=event_id)
        else:
            data = self.queryset.all()
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def approved_event(self, request):
        event_id = request.query_params.get('id')
        
        if event_id:
            data = self.queryset.filter(event=event_id, status='approved').first()
        else:
            return Response({'error': 'Event id was not provided.'}, status=status.HTTP_400_BAD_REQUEST) 
        
        serializer = self.serializer_class(data, many=False)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve object using `get_object`

        if ('status' in request.data):
            if (request.data['status'] == 'approved'):
                approved_application = Application.objects.filter(status='approved').values().first()
                
                if (approved_application != None):
                    return Response({'error': 'Some application for this event has been already approved.'}, status=status.HTTP_400_BAD_REQUEST) 
            
            if (request.data['status'] == 'denied'):
                if (instance.__dict__['status'] == 'approved'):
                    return Response({'error': 'You can not deny approved application.'}, status=status.HTTP_400_BAD_REQUEST) 

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)  # Raise for invalid data

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 