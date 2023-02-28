from rest_framework import serializers
from .models import ShowroomDetail


class SerializerShowRoomDetails(serializers.ModelSerializer):
    class Meta:
        model = ShowroomDetail
        fields = "__all__"
        depth = 1




