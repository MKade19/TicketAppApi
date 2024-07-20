from rest_framework import serializers
from .models import Ticket
from events.serializers import ApplicationTicketSerializer
from stadiums.serializers import SeatTicketSerializer
from authentication.serializers import UserTicketSerializer

class TicketSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["application"] = ApplicationTicketSerializer(instance.application).data
        data["seat"] = SeatTicketSerializer(instance.seat).data
        data["customer"] = UserTicketSerializer(instance.customer).data
        return data

    class Meta:
        model = Ticket
        fields = '__all__'