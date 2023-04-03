from PIL.ImageWin import HDC
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,LogInSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse
from django.shortcuts import redirect
import jwt
import datetime
import json
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import mixins,generics
from rest_framework.authentication import BaseAuthentication,SessionAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class LogIn(TokenObtainPairView,
            generics.GenericAPIView):
    serializer_class = LogInSerializer
    queryset = get_user_model().objects.all()


# class UserList(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()