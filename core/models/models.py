from django.db.models import *
from core.models.HOTEL_MODELS import PinCode
# Order (AND) Payment_table:
SUCCESS = 1
PENDING = 2
FAILED = 0
ORDER_STATUS = (
    (SUCCESS, 'success'), 
    (PENDING, 'pending'), 
    (FAILED, 'cancel')
)

class DateTimeUpdate(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class User_Address(PinCode):
    username = CharField(max_length=120, default='')
    city = CharField(max_length=120, default='')
    address = TextField(null=False)
    
    def __str__(self):
        return self.username



