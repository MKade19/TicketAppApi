from rest_framework import serializers
from .models import Event
from halls.serializers import HallSerializer
from images.serializers import ImageSerializer

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