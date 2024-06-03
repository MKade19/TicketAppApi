from rest_framework import serializers
from .models import Stadium, City
from images.serializers import ImageSerializer
from authentication.serializers import UserSerializer

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

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