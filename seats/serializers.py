from rest_framework import serializers
from .models import Seat
from halls.serializers import HallSerializer

class SeatSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["hall"] = HallSerializer(instance.hall).data
        return data

    class Meta:
        model = Seat
        fields = '__all__'