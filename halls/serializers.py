from rest_framework import serializers
from .models import Hall, Seat
from stadiums.serializers import StadiumSerializer

class HallSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["stadium"] = StadiumSerializer(instance.stadium).data
        return data

    class Meta:
        model = Hall
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["hall"] = HallSerializer(instance.hall).data
        return data

    class Meta:
        model = Seat
        fields = '__all__'