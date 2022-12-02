from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.viewsets import *
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from django.db.models import Q
# -------> App's Module
from ..serializers.order_payment_ser import *
from core.models.order_payment import *
from rest_framework.views import APIView


class Order_show(ListAPIView):
    queryset = Orderby.objects.all()
    serializer_class = Order_list_ser

    def get_queryset(self):
        return Orderby.objects.filter(customer =  self.request.user)


class Order_add(ModelViewSet):
    queryset = Orderby.objects.all()
    serializer_class = Order_Added
    def perform_create(self, serializer):
        opj = Cart.objects.filter(
            customer = self.request.user.username 
        ) # --------> Cart TB
        order_opj = Orderby.objects.create(
            customer = self.request.user.username            
        ) # --------> Orderby TB
        
        order_opj.ordered_things.add(
            *Cart.objects.filter(Q(customer = self.request.user.username) & Q(order_status = False))
        ) # --------> Add M2M Field's Value(Order TB)

        total = order_opj.ordered_things.filter(
            order_status = 0 #  Order TB's -> m2m Filed
            ) . aggregate(
                p_q = Sum(F('price') * F('quantity'))
            ) # p_q => prodect & quantity 
        tax =int(total['p_q']) * order_opj.delivery_charge  
        order_opj.total = total['p_q']+ int(tax)
        order_opj.save()
        
        serializer.save()
        print(">>>>>>>>>>> Order Added <<<<<<<<<<<<<")
    def get_queryset(self):
        return Orderby.objects.filter(customer = self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return Order_Added 
        return Order_list_ser 


        