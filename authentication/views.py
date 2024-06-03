from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .serializers import MyTokenObtainPairSerializer, GroupSerializer, RegisterSerializer, UserSerializer, RoleFormSerializer, RoleSerializer
from .models import User, Role
from django.contrib.auth.models import Group, Permission

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(generics.CreateAPIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if user == None:
            return Response("user: User does not exist.", status=404)
        
        if not user.check_password(request.data['oldPassword']):
            return Response("Old password is not correct.", status=400)
        
        if request.data['newPassword'] != request.data['confirmPassword']:
            return Response("Passwords don't match.", status=400)
        
        user.set_password(request.data['newPassword'])
        user.save()

        return Response()
    

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = GroupSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
        queryset = Role.objects.exclude(id=1).order_by('id')
        serializer = RoleFormSerializer(queryset, many=True)
        return Response(serializer.data)