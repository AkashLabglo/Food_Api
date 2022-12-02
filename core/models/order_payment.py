from django.db.models import *
from core.models.models import DateTimeUpdate, ORDER_STATUS, User_Address
from core.models.HOTEL_MODELS import Cart


def tax():
    return (18/100)
class Orderby(DateTimeUpdate):
    customer = CharField(max_length = 30 ) 
    ordered_things =  ManyToManyField(Cart)
    order_status = IntegerField(default = 2, choices = ORDER_STATUS)
    delivery_charge = FloatField(default = tax())
    total = IntegerField(default = 1)
    '''
    1.success, 2.bending, 0.cancel
    '''
    def __str__(self):
        return self.customer
    
class Payment(DateTimeUpdate):
    transection_id = CharField(max_length = 150)
    order_status = IntegerField(default = 2, choices = ORDER_STATUS) #  1.success, 2.bending, 0.cancel
    order = ForeignKey(Orderby, on_delete = CASCADE)

    def __str__(self):
        return self.order.customer


class Deliver_Address(User_Address):
    phone =     IntegerField()

    def __str__(self): 
        return self.username 