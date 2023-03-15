from django.shortcuts import render
from .models import *
from .serializers import *


from rest_framework import mixins
from rest_framework import generics


####################################### ** Class ** ####################################################################


# ** List ** #


class ClassList(mixins.ListModelMixin,
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

# ** Edit ** #
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

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


######################################## *** Brand *** ################################################################


#* List *#

class BrandList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = BrandManagement.objects.all()
    serializer_class = SerializerListBrandManagement

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


# ** POST ** #
class BrandPost(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = BrandManagement.objects.all()
    serializer_class = SerializerPostBrandManagement

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ** Edit ** #
class BrandEdit(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = BrandManagement.objects.all()
    serializer_class = SerializerGetBrandManagement

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


######################################## *** Brand Location *** ################################################################


# ** List **#
class BrandLocationList(mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = BrandLocation.objects.all()
    serializer_class = SerializerListBrandLocation

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# ** POST ** #
class BrandLocationPost(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = BrandLocation.objects.all()
    serializer_class = SerializerPostBrandLocation

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ** Edit ** #
class BrandLocationEdit(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = BrandLocation.objects.all()
    serializer_class = SerializerGetBrandLocation

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




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


class StatusManagementList(mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = StatusManagement.objects.all()
    serializer_class = SerializerStatusManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)