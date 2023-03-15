from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
#
urlpatterns = [
    path('classGet', ClassList.as_view()),
    path('classPost', ClassPost.as_view()),
    path('classGet/<int:pk>', ClassEdit.as_view()),

    path('brandGet', BrandList.as_view()),
    path('brandPost', BrandPost.as_view()),
    path('brandGet/<int:pk>', BrandEdit.as_view()),

    path('brandLocationGet', BrandLocationList.as_view()),
    path('brandLocationPost', BrandLocationPost.as_view()),
    path('brandLocationGet/<int:pk>', BrandLocationEdit.as_view()),

    path('materialGet', MaterialList.as_view()),


    path('asset', AssetList.as_view()),
    path('brandType', BrandTypeList.as_view()),
    path('lightType', LightList.as_view()),
    path('vendor', VendorList.as_view()),
    path('status', StatusList.as_view()),
    path('statusManagement', StatusManagementList.as_view()),

]
