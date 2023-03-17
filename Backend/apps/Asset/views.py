from django.shortcuts import render
from .models import *
from .serializers import *


from rest_framework import mixins
from rest_framework import generics

####################################### ** Status ** ####################################################################

# ** List ** #


class StatusList(mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Status.objects.all()
    serializer_class = SerializerListStatus

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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


######################################## *** Brand *** #################################################################


# ** List ** #

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


######################################## *** Brand Location *** ########################################################


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


######################################## *** Brand Type *** ############################################################


# ** List ** #

class BrandTypeList(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = BrandTypeManagement.objects.all()
    serializer_class = SerializerListBrandTypeManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# ** POST ** #
class BrandTypePost(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = BrandTypeManagement.objects.all()
    serializer_class = SerializerPostBrandTypeManagement

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ** Edit ** #
class BrandTypeEdit(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = BrandTypeManagement.objects.all()
    serializer_class = SerializerGetBrandTypeManagement

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


######################################## *** Brand Type *** ############################################################

# ** List ** #

class VendorList(mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = VendorManagement.objects.all()
    serializer_class = SerializerListVendorManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# ** POST ** #
class VendorPost(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = VendorManagement.objects.all()
    serializer_class = SerializerPostVendorManagement

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ** Edit ** #
class VendorEdit(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = VendorManagement.objects.all()
    serializer_class = SerializerGetVendorManagement

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


######################################## *** Material *** ##############################################################

# ** List ** #

class MaterialList(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = MaterialManagement.objects.all()
    serializer_class = SerializerListMaterialManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# ** POST ** #
class MaterialPost(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = MaterialManagement.objects.all()
    serializer_class = SerializerPostMaterialManagement

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ** Edit ** #
class MaterialEdit(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = MaterialManagement.objects.all()
    serializer_class = SerializerGetMaterialManagement

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


######################################## *** Light *** #################################################################

# ** List ** #

class LightList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = LightManagement.objects.all()
    serializer_class = SerializersListLightManagement

    def get(self, request, *args,**kwargs):
        return self.list(request,*args,**kwargs)

# ** POST ** #
class LightPost(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = LightManagement.objects.all()
    serializer_class = SerializersPostLightManagement

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ** Edit ** #
class LightEdit(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = LightManagement.objects.all()
    serializer_class = SerializersGetLightManagement

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


######################################## *** StatusManagement *** ######################################################

# ** List ** #

class StatusManagementList(mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = StatusManagement.objects.all()
    serializer_class = SerializerListStatusManagement

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# ** POST ** #
class StatusManagementPost(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = StatusManagement.objects.all()
    serializer_class = SerializerPostStatusManagement

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ** Edit ** #
class StatusManagementEdit(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = StatusManagement.objects.all()
    serializer_class = SerializerGetStatusManagement

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


######################################## *** Asset *** #################################################################


class AssetList(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = AssetManagement.objects.all()
    serializer_class = SerializersAssetManagement

    def get(self, request, *args,**kwargs):
        return self.list(request,*args,**kwargs)




