from rest_framework import serializers
from .models import ClassManagement,LightManagement,AssetManagement


class SerializersClassManagement(serializers.ModelSerializer):
    class Meta:
        model = ClassManagement
        fields = ["id","name",'status']
        depth = 1


class SerializersLightManagement(serializers.ModelSerializer):
    class Meta:
        model = LightManagement
        fields = ['id','name','status']
        depth = 1


class SerializersAssetManagement(serializers.ModelSerializer):
    class Meta:
        model = AssetManagement
        fields = "__all__"

        depth = 2
