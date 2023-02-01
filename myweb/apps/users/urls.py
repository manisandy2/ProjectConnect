from django.urls import path
from .views import UserList,UserDetail,LoginView

urlpatterns = [

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path("login",LoginView.as_view()),
]
