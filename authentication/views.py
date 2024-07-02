from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .serializers import MyTokenObtainPairSerializer, GroupSerializer, RegisterSerializer, UserSerializer, RoleFormSerializer, RoleSerializer
from .models import User, Role
from django.contrib.auth.models import Group, Permission
from rest_framework.decorators import action
import requests

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


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
    
    @action(detail=False, methods=['get'])
    def user(self, request):
        email = request.query_params.get('email')
        
        if email:
            data = self.queryset.filter(event=email)
        else:
            data = self.queryset.all()
        
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)



class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
        queryset = Role.objects.exclude(id=1).order_by('id')
        serializer = RoleFormSerializer(queryset, many=True)
        return Response(serializer.data)

class GoogleLogin(SocialLoginView):
    permission_classes = (permissions.AllowAny,)
    adapter_class = GoogleOAuth2Adapter
    
    def get(self, request):
        response = requests.get("https://www.googleapis.com/oauth2/v3/userinfo?access_token=" + request.query_params.get('access_token'))
        if response.status_code != 200:
            return Response(response.reason, status=response.status_code)
        guser = response.json()
        user = User.objects.filter(email__iexact=guser["email"]).first()
        if user == None:
            return Response("user: User does not exist.", status=404)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

class GoogleSignUpView(generics.CreateAPIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        role = Role.objects.filter(id=request.data['role']).first()
        if user == None:
            return Response("user: User does not exist.", status=404)
        if role == None:
            return Response("role: Role does not exist.", status=404)            
        if user.fullname == '':
            user.fullname = user.first_name + ' ' + user.last_name
        user.role = role
        user.save()
        user = User.objects.filter(email=request.data['email']).first()

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)