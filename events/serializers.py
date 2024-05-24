from rest_framework import serializers
from .models import Event, Application, ApplicationSeat
from halls.serializers import HallSerializer
from images.serializers import ImageSerializer
from halls.serializers import SeatSerializer

class EventSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["hall"] = HallSerializer(instance.hall).data
        data["images"] = ImageSerializer(instance.images).data
        return data

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'begin', 'end', 'images', 'hall')
        extra_kwargs = {'images': {'required': True}}


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