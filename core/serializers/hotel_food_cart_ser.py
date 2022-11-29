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
    #customer = CharField(source="user.username", read_only=True)
    
    class Meta:
        model = Cart
        fields = [
           'id','recipes', 'quantity', 
        ]
        
    def save(self, **kwargs):
        food = self.validated_data['recipes']
        quantity = self.validated_data['quantity']

        try:
            #foods = Food.objects.get(id = food.id)
            var = Cart.objects.get(recipes =food.id) 
            var.quantity = quantity
            #var.price = foods.price
            var.save()
            print("Update on Serializer")
           
            self.instance = var
        except:
            #pass
            foods = Food.objects.get(id = food.id)
            #for i in foods:
            self.instance = Cart.objects.create(recipes = foods, quantity = quantity, price = foods.price, image =foods.image) 
            print("Create on Serializer")        
        return self.instance  
      
