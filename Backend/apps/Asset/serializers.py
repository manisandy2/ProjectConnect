from rest_framework import serializers
from .models import *


########################################## *** Status *** ##############################################################

class SerializerListStatus(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id","name"]
        # depth = 1

########################################## *** Class Management *** ####################################################


class SerializersListClassManagement(serializers.ModelSerializer):

    class Meta:
        model = ClassManagement
        fields = ("id","name","status")
        depth = 1


class SerializersGetClassManagement(serializers.ModelSerializer):

    class Meta:
        model = ClassManagement
        fields = ("id","name","status")
        # depth = 1


class SerializersPostClassManagement(serializers.ModelSerializer):

    class Meta:
        model = ClassManagement
        fields = ("id","name","status")
        # depth = 1


########################################## *** Brand Management *** ####################################################


class SerializerListBrandManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandManagement
        fields = "__all__"
        depth = 1


class SerializerGetBrandManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandManagement
        fields = "__all__"
        # depth = 1


class SerializerPostBrandManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandManagement
        fields = "__all__"
        # depth = 1


########################################## *** Brand Location *** ######################################################

# Advertisement Location navbar name &  Brand Locations header name

class SerializerListBrandLocation(serializers.ModelSerializer):
    class Meta:
        model = BrandLocation
        fields = "__all__"
        depth = 1


class SerializerGetBrandLocation(serializers.ModelSerializer):
    class Meta:
        model = BrandLocation
        fields = "__all__"
        # depth = 1


class SerializerPostBrandLocation(serializers.ModelSerializer):
    class Meta:
        model = BrandLocation
        fields = "__all__"
        # depth = 1


########################################## *** Brand Type Management *** ###############################################


class SerializerListBrandTypeManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandTypeManagement
        fields = "__all__"
        depth = 1


class SerializerGetBrandTypeManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandTypeManagement
        fields = "__all__"
        # depth = 1


class SerializerPostBrandTypeManagement(serializers.ModelSerializer):
    class Meta:
        model = BrandTypeManagement
        fields = "__all__"
        # depth = 1


########################################## *** Vendor Management *** ###################################################


class SerializerListVendorManagement(serializers.ModelSerializer):
    class Meta:
        model = VendorManagement
        fields = "__all__"
        depth = 1


class SerializerGetVendorManagement(serializers.ModelSerializer):
    class Meta:
        model = VendorManagement
        fields = "__all__"
        # depth = 1


class SerializerPostVendorManagement(serializers.ModelSerializer):
    class Meta:
        model = VendorManagement
        fields = "__all__"
        # depth = 1


########################################## *** Material Management *** #################################################


class SerializerListMaterialManagement(serializers.ModelSerializer):
    class Meta:
        model = MaterialManagement
        fields = "__all__"
        depth = 1


class SerializerGetMaterialManagement(serializers.ModelSerializer):
    class Meta:
        model = MaterialManagement
        fields = "__all__"
        # depth = 1


class SerializerPostMaterialManagement(serializers.ModelSerializer):
    class Meta:
        model = MaterialManagement
        fields = "__all__"
        # depth = 1


########################################## *** Light Type List*** ######################################################

class SerializersListLightManagement(serializers.ModelSerializer):
    class Meta:
        model = LightManagement
        fields = ['id','name','status']
        depth = 1


class SerializersGetLightManagement(serializers.ModelSerializer):
    class Meta:
        model = LightManagement
        fields = ['id','name','status']
        depth = 1


class SerializersPostLightManagement(serializers.ModelSerializer):
    class Meta:
        model = LightManagement
        fields = ['id','name','status']
        depth = 1

########################################## *** Status Management *** ###################################################


class SerializerListStatusManagement(serializers.ModelSerializer):
    class Meta:
        model = StatusManagement
        fields = "__all__"
        depth = 1


class SerializerGetStatusManagement(serializers.ModelSerializer):
    class Meta:
        model = StatusManagement
        fields = "__all__"
        depth = 1


class SerializerPostStatusManagement(serializers.ModelSerializer):
    class Meta:
        model = StatusManagement
        fields = "__all__"
        depth = 1


########################################## *** Asset Management *** ###################################################


class SerializersAssetManagement(serializers.ModelSerializer):
    class Meta:
        model = AssetManagement
        fields = "__all__"
        depth = 2