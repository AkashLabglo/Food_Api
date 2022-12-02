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
        return Cart.objects.filter(customer =  self.request.user)

        
class Cart_Detail_Delete(RetrieveDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = cart_ser

    def get_queryset(self):
        #user = User.objects.get(user = self.request.user)
        return Cart.objects.filter(customer =  self.request.user)  


        
from django.db.models import Q
class Add_Cart(ModelViewSet):
    queryset = Cart.objects.all()   
    def perform_create(self, serializer):
        my_dict = dict(self.request.data)
        get_food_id = my_dict['recipes'][0]
        quantity = my_dict['quantity'][0]
        get_food_opj = Food.objects.get(id = int(get_food_id))
        try:
            var = Cart.objects.get(recipes =get_food_opj.id) 
            var.quantity = int(quantity)
            #var.price = get_food_opj.price
            var.save()
            print(">>>>>>>>>>> Update <<<<<<<<<<<<<")
        except:
            var = Cart.objects.create(
                customer = self.request.user.username,
                recipes = get_food_opj, 
                quantity = quantity, 
                price = get_food_opj.price, 
                image =get_food_opj.image
            )
            print(">>>>>>>>>>> Create <<<<<<<<<<<<<")
            
        
    def get_queryset(self):
        return Cart.objects.filter(customer = self.request.user)
    
   
    def get_serializer_class(self):
        if self.request.method == "POST":
            return Add_To_Cart_ser 
        return cart_ser
    
       