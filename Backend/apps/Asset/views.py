from django.shortcuts import render
from .models import ClassManagement,LightManagement,AssetManagement,BrandManagement,BrandTypeManagement,\
    VendorManagement,BrandLocation,MaterialManagement
from .serializers import SerializersClassManagement,SerializersLightManagement,SerializersAssetManagement,\
    SerializerBrandManagement,SerializerBrandTypeManagement,SerializerVendorManagement,SerializerBrandLocation,\
    SerializerMaterialManagement


from rest_framework import mixins
from rest_framework import generics

########################################################################################################################


class ClassList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = ClassManagement.objects.all()
    serializer_class = SerializersClassManagement

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



########################################################################################################################


class LightList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = LightManagement.objects.all()
    serializer_class = SerializersLightManagement

    def get(self, request, *args,**kwargs):
        return self.list(request,*args,**kwargs)

########################################################################################################################


class AssetList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = AssetManagement.objects.all()
    serializer_class = SerializersAssetManagement

    def get(self, request, *args,**kwargs):
        return self.list(request,*args,**kwargs)


########################################################################################################################

class BrandList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = BrandManagement.objects.all()
    serializer_class = SerializerBrandManagement

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


########################################################################################################################

class BrandTypeList(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = BrandTypeManagement.objects.all()
    serializer_class = SerializerBrandTypeManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


########################################################################################################################

class VendorList(mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = VendorManagement.objects.all()
    serializer_class = SerializerVendorManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

########################################################################################################################


class BrandLocationList(mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = BrandLocation.objects.all()
    serializer_class = SerializerBrandLocation

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


########################################################################################################################


class MaterialList(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = MaterialManagement.objects.all()
    serializer_class = SerializerMaterialManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
