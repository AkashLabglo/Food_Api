from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views.views import *
from core.views.hotel_food_cart import *
var = DefaultRouter()
var.register(r'register', Register)
var.register(r'addcart', Add_Cart, basename='addcart')
#var.register(r'authlogin', Login, basename='addcart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('rest_framework.urls')),
    path('authlogin/', Login.as_view()),
    
    # --------> Hotel & Food
        #Detail_view Urls
    path('foods/<int:pk>/', Food_detail_view.as_view(), name="foods_detail"),    
    path('pincodes/<int:pk>/', Pincode_Detail_view.as_view(), name="pincodes_detail"),
    path('hotels/<int:pk>/', Hotel_detail_view.as_view(), name="hotels_detail"),
        #List_view Urls
    path('hotels/', Hotel_List_view.as_view(), name="hotels"),
    path('cartlist/', Cart_List.as_view(), name='cartlist')
]

urlpatterns += var.urls
