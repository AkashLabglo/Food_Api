from rest_framework.serializers import * 
from django.contrib.auth.models import User
from django.db import models
# -----> App'S Modules
from core.views.hotel_food_cart import *
from core.models.HOTEL_MODELS import *



class Food_ser(ModelSerializer):

    class Meta:
        model = Food
        fields = "__all__"




class PinCode_ser(ModelSerializer):
    class Meta:
        model = PinCode
        fields = "__all__"

        
class Hotel_ser(ModelSerializer):
    foods = Food_ser(many=True)
    class Meta:
        model = Hotel
        fields = "__all__"

class cart_ser(ModelSerializer):
    recipes = Food_ser()
    class Meta:
        model = Cart
        fields = "__all__"

        
class Add_To_Cart_ser(ModelSerializer):
    recipes = ForeignKey(Food,
    on_delete=models.CASCADE,)
        
    class Meta:
        model = Cart
        fields = [
           'id', 'recipes', 'quantity'
        ]
        read_only_field = ['price']
   
