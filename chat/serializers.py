from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'username', 'sender', 'roomname', 'content', 'timestamp')
        read_only_fields = ('id', 'timestamp')