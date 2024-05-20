from rest_framework import serializers
from .models import Stadium
from images.serializers import ImageSerializer
from cities.serializers import CitySerializer
from users.serializers import UserSerializer

class StadiumSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = ImageSerializer(instance.image).data
        data["city"] = CitySerializer(instance.city).data
        data["administrator"] = UserSerializer(instance.administrator).data
        return data

    class Meta:
        model = Stadium
        fields = '__all__'