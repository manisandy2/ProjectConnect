from django.shortcuts import render
from .models import ClassManagement,LightManagement,AssetManagement,BrandManagement,BrandTypeManagement,\
    VendorManagement,BrandLocation,MaterialManagement,Status
from .serializers import SerializersGetClassManagement,SerializersPostClassManagement,SerializersLightManagement,\
    SerializersAssetManagement,\
    SerializerBrandManagement,SerializerBrandTypeManagement,SerializerVendorManagement,SerializerBrandLocation,\
    SerializerMaterialManagement,SerializerStatus,SerializersListClassManagement


from rest_framework import mixins
from rest_framework import generics


####################################### ** Class ** ####################################################################


# ** List ** #


class ClassList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = ClassManagement.objects.all()
    serializer_class = SerializersListClassManagement

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

# ** POST ** #


class ClassPost(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = ClassManagement.objects.all()
    serializer_class = SerializersPostClassManagement

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClassEdit(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = ClassManagement.objects.all()
    serializer_class = SerializersGetClassManagement

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

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


class StatusList(mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Status.objects.all()
    serializer_class = SerializerStatus

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
