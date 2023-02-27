from django.urls import path
from .views import ClassList,LightList,AssetList
from rest_framework.routers import DefaultRouter
#
urlpatterns = [
    path('class/', ClassList.as_view()),
    path('light/',LightList.as_view()),
    path('asset/',AssetList.as_view()),

]
