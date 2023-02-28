from django.urls import path
from .views import ClassList,LightList,AssetList,BrandList,BrandTypeList,VendorList,BrandLocationList,MaterialList
from rest_framework.routers import DefaultRouter
#
urlpatterns = [
    path('class/', ClassList.as_view()),
    path('light/', LightList.as_view()),
    path('asset/', AssetList.as_view()),
    path('brand/', BrandList.as_view()),
    path('brandType/', BrandTypeList.as_view()),
    path('vendor/', VendorList.as_view()),
    path('brandLocation/', BrandLocationList.as_view()),
    path('material/', MaterialList.as_view()),

]
