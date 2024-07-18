from rest_framework import serializers
from .models import Stadium, City, Hall, Seat
from images.serializers import ImageSerializer
from authentication.serializers import UserSerializer

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["stadium"] = StadiumSerializer(instance.stadium).data
        return data

    class Meta:
        model = Hall
        fields = '__all__'


class StadiumSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = ImageSerializer(instance.image).data
        data["city"] = CitySerializer(instance.city).data
        return data    

    class Meta:
        model = Stadium
        fields = ('id', 'name', 'image', 'description', 'city', 'administrator')
        

class SeatSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["hall"] = HallSerializer(instance.hall).data
        return data
    
    class Meta:
        model = Seat
        fields = '__all__'



class SeatTicketSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Seat
        fields = ('id', 'number', 'row', 'sector',)