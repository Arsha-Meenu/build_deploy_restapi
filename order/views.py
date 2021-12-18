from re import S
from typing import Generic
from django.shortcuts import get_object_or_404, render
from rest_framework import generics,status
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from order.models import Order
from . import serializers
from rest_framework.permissions import OR, IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth import get_user_model
 
User = get_user_model()

class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated,]
    # # fetch all orders details those are already created:
    def get(self,request):
        order = Order.objects.all()
        serializer = self.serializer_class(instance=order,many =True)        
        return Response(data =serializer.data,status = status.HTTP_200_OK) 
        
#   create a new order.:
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
    serializer_class = serializers.OrderDetailSerializer
    permission_class = [IsAdminUser,]

    # fetch the order's details  by order_id: 
    def get(self,request,order_id):
        order = get_object_or_404(Order,pk= order_id)
        serializer = self.serializer_class(instance = order)
        return Response(data = serializer.data,status=status.HTTP_200_OK)

    # update the order's details  by order_id: 
    def put(self,request,order_id):
        data = request.data
        order = get_object_or_404(Order,pk = order_id)
        serializer = self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data,status = status.HTTP_200_OK)
        return Response(data = serializers.errors,status = status.HTTP_400_BAD_REQUEST)

    # delete the order's details  by order_id: 
    def delete(self,request,order_id):
        order = get_object_or_404(Order,pk = order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusSerializer
    # change the status of order by order_id
    def put(self,request,order_id):
        data = request.data
        order = get_object_or_404(Order,pk = order_id)
        serializer = self.serializer_class(data = data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data,status=status.HTTP_200_OK)
        return Response(data = serializer.errors,status =status.HTTP_400_BAD_REQUEST)


class UserOrderListView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    # fetch the order list of specified user:
    def get(self,request,user_id):
        user = User.objects.get(pk=user_id)
        orders = Order.objects.all().filter(customer = user)
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserOrderDetail(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    # fetch the specific order of specified user by user_id and order_id:

    def get(self,request,user_id,order_id):
        user =User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer =user_id).get(pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data= serializer.data,status =status.HTTP_200_OK)
        