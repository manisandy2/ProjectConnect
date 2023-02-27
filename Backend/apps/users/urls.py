from django.urls import path
from .views import UserList,UserDetail,UserViewSet
from rest_framework.routers import DefaultRouter
#
urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

router = DefaultRouter()
router.register('login', UserViewSet,basename='login')
urlpatterns += router.urls
