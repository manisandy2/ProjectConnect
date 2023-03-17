from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
#
urlpatterns = [
    path('status', StatusList.as_view()),

    path('classGet', ClassList.as_view()),
    path('classPost', ClassPost.as_view()),
    path('classGet/<int:pk>', ClassEdit.as_view()),

    path('brandGet', BrandList.as_view()),
    path('brandPost', BrandPost.as_view()),
    path('brandGet/<int:pk>', BrandEdit.as_view()),

    path('brandLocationGet', BrandLocationList.as_view()),
    path('brandLocationPost', BrandLocationPost.as_view()),
    path('brandLocationGet/<int:pk>', BrandLocationEdit.as_view()),

    path('brandTypeGet', BrandTypeList.as_view()),
    path('brandTypePost', BrandTypePost.as_view()),
    path('brandTypeGet/<int:pk>', BrandTypeEdit.as_view()),

    path('vendorGet', VendorList.as_view()),
    path('vendorPost', VendorPost.as_view()),
    path('vendorGet/<int:pk>', VendorEdit.as_view()),

    path('materialGet', MaterialList.as_view()),
    path('materialPost', MaterialPost.as_view()),
    path('materialGet/<int:pk>', MaterialEdit.as_view()),

    path('lightTypeGet', LightList.as_view()),
    path('lightTypePost', LightPost.as_view()),
    path('lightTypeGet/<int:pk>', LightEdit.as_view()),


    path('statusManagementGet', StatusManagementList.as_view()),
    path('statusManagementPost', StatusManagementPost.as_view()),
    path('statusManagementGet/<int:pk>', StatusManagementEdit.as_view()),

    path('assetGet', AssetList.as_view()),

]
