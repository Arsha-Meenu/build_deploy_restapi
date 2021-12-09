from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import User

class HelloView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'msg':'hello auth !'},status = status.HTTP_200_OK)


class UserCreationView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
