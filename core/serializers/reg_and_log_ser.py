from rest_framework.serializers import * 
from django.contrib.auth.models import User
# -----> App'S Modules
from core.views.views import *
from core.models.register_models import *



class Login_ser(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'password'
        ]
   
            

'''[
            'id', 'username', 'password', 'email'
            ]'''

class Register_Serializers(ModelSerializer):
    class Meta:
        model = User
        fields = [
        'id', 
        'username', 
        'password', 
        'email'
        'phone'
        ]
    write_only_fields = ('password')
    read_only_fields = ('id')
    
    def create(self, validated_data):
        user = User.objects.create_superuser(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user 