from django.urls import path
from .views import ClassList,ClassPost, LightList,AssetList,BrandList,BrandTypeList,VendorList,BrandLocationList,\
    MaterialList,StatusList,ClassEdit,StatusManagementList
from rest_framework.routers import DefaultRouter
#
urlpatterns = [
    path('classGet', ClassList.as_view()),
    path('classPost', ClassPost.as_view()),
    path('classGet/<int:pk>', ClassEdit.as_view()),
    path('asset', AssetList.as_view()),
    path('brand/', BrandList.as_view()),
    path('brandType', BrandTypeList.as_view()),
    path('lightType', LightList.as_view()),
    path('vendor', VendorList.as_view()),
    path('brandLocation', BrandLocationList.as_view()),
    path('material', MaterialList.as_view()),
    path('status', StatusList.as_view()),
    path('statusManagement', StatusManagementList.as_view()),

]
