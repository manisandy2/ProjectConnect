from rest_framework import serializers
from .models import ClassManagement,LightManagement,AssetManagement,\
    BrandManagement,BrandTypeManagement,VendorManagement,BrandLocation,MaterialManagement


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


class SerializerBrandManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandManagement
        fields = "__all__"
        depth = 1


class SerializerBrandTypeManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandTypeManagement
        fields = "__all__"
        depth = 1


class SerializerVendorManagement(serializers.ModelSerializer):
    class Meta:
        model = VendorManagement
        fields = "__all__"
        depth = 1


class SerializerBrandLocation(serializers.ModelSerializer):
    class Meta:
        model = BrandLocation
        fields = "__all__"
        depth = 1


class SerializerMaterialManagement(serializers.ModelSerializer):
    class Meta:
        model = MaterialManagement
        fields = "__all__"
        depth = 1