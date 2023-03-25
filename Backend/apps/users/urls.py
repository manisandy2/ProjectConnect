from django.urls import path
from .views import UserList,UserDetail,LogIn
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # path('exampleView', ExampleView.as_view()),
    path('login', LogIn.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

]

