from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]


class LogInSerializer(TokenObtainPairSerializer):
    # class Meta:
        # model = User
        # fields = "__all__"
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        # token['password'] = user.password
        # token['is staff'] = user.is_staff
        # token['is active'] = user.is_active
        # token['is superuser'] = user.is_superuser
        # token['Group'] = user.groups

        return token

  # is_staff = False
  #   is_active = False
  #   is_superuser = False


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         token['username'] = user.name
#
#         return token