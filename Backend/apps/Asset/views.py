from django.shortcuts import render
from .models import ClassManagement,LightManagement,AssetManagement
from .serializers import SerializersClassManagement,SerializersLightManagement,SerializersAssetManagement

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