from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from . import serializers
from .models import User

class HelloView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'msg':'hello auth !'},status = status.HTTP_200_OK)

# signup
class UserCreationView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer   

    def post(self,request):
        data = request.data       
        serializer = self.serializer_class(data = data)     
        if serializer.is_valid():
            serializer.save(is_active = 1)
            return Response(data = serializer.data,status= status.HTTP_201_CREATED)
        return Response(data =  serializer.data,status = status.HTTP_400_BAD_REQUEST)
# fetch all users list:
class UserListView(generics.GenericAPIView):
    serializer_class = serializers.UserDetailSerializer
    def get(self,request):
        user = User.objects.all()
        print(user)
        serializer =self.serializer_class(instance=user,many=True)
        return Response(data = serializer.data,status = status.HTTP_200_OK)
