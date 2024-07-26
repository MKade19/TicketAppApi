from rest_framework import serializers
from .models import Event, Application, ApplicationSeat
from images.models import Image
from stadiums.models import Seat
from images.serializers import ImageSerializer
from stadiums.serializers import SeatSerializer, HallSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    seats = serializers.PrimaryKeyRelatedField(many=True, queryset=Seat.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["event"] = EventSerializer(instance.event).data
        data['seats'] = []
        for entry in instance.seats.all():
            seat = SeatSerializer(entry).data
            data['seats'].append(seat)
            
        return data
    
    class Meta:
        model = Application
        fields = '__all__'


class ApplicationTicketSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["event"] = EventSerializer(instance.event).data
            
        return data

    class Meta:
        model = Application
        fields = ('id', 'event',)


class EventSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["hall"] = HallSerializer(instance.hall).data
        data['images'] = []
        for entry in instance.images.all():
            image = ImageSerializer(entry).data
            data['images'].append(image)
        return data

    class Meta:
        model = Event
        fields = '__all__'

class EventImagesSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = []
        for entry in instance.images.all():
            image = ImageSerializer(entry).data
            data['images'].append(image)
        return data

    class Meta:
        model = Event
        fields = ('images',)


class ApplicationSeatSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["application"] = ApplicationSerializer(instance.application).data
        data["seat"] = SeatSerializer(instance.seat).data
        return data

    class Meta:
        model = ApplicationSeat
        fields = '__all__'