from PIL.ImageWin import HDC
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import redirect
import jwt
import datetime
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self,request):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User Not Found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password!")

        refresh = RefreshToken.for_user(User)
        access = AccessToken.for_user(User)

        print("Refresh", refresh)
        print("Access", access)
        # return Response({
        #     "Message": "Success",
        #     "Access":AccessToken.for_user(User)
        # })
        return HttpResponse("Login success full")