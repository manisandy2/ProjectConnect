from django.shortcuts import render
from .models import ShowroomDetail
from .serializers import SerializerShowRoomDetails
from rest_framework import mixins
from rest_framework import generics


class ShowRoomList(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = ShowroomDetail.objects.all()
    serializer_class = SerializerShowRoomDetails

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

