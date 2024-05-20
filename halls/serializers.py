from rest_framework import serializers
from .models import Hall
from stadiums.serializers import StadiumSerializer

class HallSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["stadium"] = StadiumSerializer(instance.stadium).data
        return data

    class Meta:
        model = Hall
        fields = '__all__'