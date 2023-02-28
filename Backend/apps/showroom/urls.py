from django.urls import path
from .views import ShowRoomList

urlpatterns = [
    path('showroom/', ShowRoomList.as_view()),
]
