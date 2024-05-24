from rest_framework import serializers
from .models import Application, ApplicationSeat
from events.serializers import EventSerializer
from seats.serializers import SeatSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["event"] = EventSerializer(instance.event).data
        data["seats"] = SeatSerializer(instance.seats).data
        return data

    class Meta:
        model = Application
        fields = ('id', 'event', 'seats')
        extra_kwargs = {'seats': {'required': True}}


class ApplicationSeatSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["application"] = ApplicationSerializer(instance.application).data
        data["seat"] = SeatSerializer(instance.seat).data
        return data

    class Meta:
        model = ApplicationSeat
        fields = '__all__'