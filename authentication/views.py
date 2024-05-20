from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .serializers import MyTokenObtainPairSerializer, GroupSerializer, RegisterSerializer
from users.models import User
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