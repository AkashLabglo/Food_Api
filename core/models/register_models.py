from django.db.models import *
from core.models.models import DateTimeUpdate
from django.contrib.auth.models import User

class Customer(DateTimeUpdate):
    user = OneToOneField(User, on_delete=CASCADE, related_name='customer')
    email = EmailField(max_length=30, null = False)
    phone = IntegerField(null = False)
    iflogged = BooleanField(default = False)
    token = CharField(max_length=150, null = True, default = '')

    def __str__(self):
        return "{} -{}".format(self.user, self.email)

     