from users.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group, Permission
from roles.serializers import RoleSerializer

class UserTokenSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["role"] = RoleSerializer(instance.role).data
        return data

    class Meta:
        model = User
        fields = [ 'id', 'email', 'fullname', 'role' ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # These are claims, you can add custom claims
        token['email'] = user.email
        token['verified'] = user.profile.verified
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] =  UserTokenSerializer(self.user).data
    
        return data 
    
    
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename',)


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions',)
        

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'fullname', 'password', 'confirmPassword', 'role')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirmPassword']:
            raise serializers.ValidationError(
                {"password": "Password fields don't match."})

        return attrs

    def create(self, validated_data): 
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['email'],
            fullname = validated_data['fullname'],
            role = validated_data['role'],
            is_active = True
            # is_active = validated_data['role'].id == 1
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
