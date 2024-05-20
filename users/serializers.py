from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from roles.serializers import RoleSerializer

class UserSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["role"] = RoleSerializer(instance.role).data
        return data
    
    password = serializers.CharField(write_only=True, validators=[validate_password], required=False)

    class Meta:
        model = User
        fields = ('id', 'fullname', 'email', 'role', 'password')

    def create(self, validated_data):
        if not 'password' in validated_data:
            raise serializers.ValidationError('Password can not be empty')

        user = User.objects.create(
            email = validated_data['email'],
            fullname = validated_data['fullname'],
            role = validated_data['role'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.fullname = validated_data.get("fullname", instance.fullname)
        instance.role = validated_data.get("role", instance.role)

        if (validated_data.get("password", instance.password) != ''):
            instance.set_password(validated_data.get("password", instance.password))

        instance.save()
        return instance
        