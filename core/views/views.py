from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.viewsets import *
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
# -------> App's Module
from core.serializers.reg_and_log_ser import Register_Serializers, Login_ser
from core.models.register_models import Customer






class Register(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Register_Serializers

class Login(APIView):
    Serializer_class = Login_ser
    permission_classes = [AllowAny, IsAuthenticated]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        # ------->
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        
        user_id = authenticate(username = username, password = password)
        if not user_id:
            return Response({'error': 'Invalid Credentials'})
        login(request, user_id)
        token, li = Token.objects.get_or_create(user=user_id)

        return Response({'token': token.key})
    
    