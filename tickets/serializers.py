from rest_framework import serializers
from .models import Ticket
from events.serializers import ApplicationSerializer
from stadiums.serializers import SeatSerializer
from authentication.serializers import UserSerializer

class TicketSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["application"] = ApplicationSerializer(instance.application).data
        data["seat"] = SeatSerializer(instance.seat).data
        data["customer"] = UserSerializer(instance.customer).data
        return data

    class Meta:
        model = Ticket
        fields = '__all__'