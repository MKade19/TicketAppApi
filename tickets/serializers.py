from rest_framework import serializers
from .models import Ticket
from applications.serializers import ApplicationSeatSerializer
from users.serializers import UserSerializer

class TicketSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["application_seat"] = ApplicationSeatSerializer(instance.application_seat).data
        data["customer"] = UserSerializer(instance.customer).data
        return data

    class Meta:
        model = Ticket
        fields = '__all__'