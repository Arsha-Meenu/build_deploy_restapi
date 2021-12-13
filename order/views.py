from re import S
from typing import Generic
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from order.models import Order
from .serializers import OrderCreationSerializer
from rest_framework.permissions import IsAuthenticated

class OrderCreateListView(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        order = Order.objects.all()
        serializer = self.serializer_class(instance=order,many =True)
        print(serializer.data)
        return Response(data =serializer.data,status = status.HTTP_200_OK) 
        
  
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data = data)
        user = request.user
        print(user)
        if serializer.is_valid():
            serializer.save(customer = user)
            return Response(data = serializer.data,status = status.HTTP_201_CREATED)
        return Response(data = serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    def get(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass