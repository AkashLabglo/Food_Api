from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.viewsets import *
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import csrf_exempt
# -------> App's Module
from core.serializers.hotel_food_cart_ser import *
from core.models.HOTEL_MODELS import *
from rest_framework.views import APIView


class Pincode_List_view(ListAPIView):
    queryset = PinCode.objects.all()
    serializer_class = PinCode_ser 

class Pincode_Detail_view(RetrieveAPIView):
    queryset = PinCode.objects.all()
    serializer_class = PinCode_ser

#_____________________________________
class Hotel_List_view(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = Hotel_ser

class Hotel_detail_view(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = Hotel_ser

#_____________________________________
class Food_List(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = Food_ser

class Food_detail_view(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = Food_ser
#_____________________________________


class Cart_List(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = cart_ser

    def get_queryset(self):
        #user = User.objects.get(user = self.request.user)
        return Cart.objects.filter(customer =  self.request.user)
    

class Add_Cart(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = cart_ser
    
    def perform_create(self, serializer):
           print(">>>>>>>>>>>>>", self.request.user.username)
           serializer.save(customer =str(self.request.user.username))
        
    def get_queryset(self):
        return Cart.objects.filter(customer = self.request.user)
    
   
    def get_serializer_class(self):
        if self.request.method == "POST":
            return Add_To_Cart_ser 
        return cart_ser
    # def perform_update(self, serializer):
    #     print(self.request.user)    
    #     ak = serializer.save(customer = self.request.user)
    #     print('}}}}}}}}}}}}}}}}}}}}}}}}}',ak)
    #     return ak
       