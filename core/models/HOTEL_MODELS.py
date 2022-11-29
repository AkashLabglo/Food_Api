from django.db.models import *



class PinCode(Model):
    state = CharField(max_length=30, null = False)
    district =  CharField(max_length=30, null = False)
    pincode = IntegerField(null = True)

    def __str__(self):
        return "{},{}".format(self.district,self.pincode)


   

class Food(Model):    
    VEG =   'v'
    None_VEG = 'n'
    FOOD_CHOICE = (
    (None_VEG, 'none_veg'), 
    (VEG, 'veg'),    
    )

    NOTADDED = False
    ADDED = True
    FOOD_STATUS = (
    (NOTADDED, 'Notadded_to_Cart'), 
    (ADDED, 'Added_to_Cart'),    
    )


    category = CharField(max_length=1,choices=FOOD_CHOICE, default='')
    recipes = CharField(max_length=150, null = False, blank = False)
    #hotel = ManyToManyField(Hotel)
    image = ImageField(upload_to = "Pictures", null = True)
    price = IntegerField()
    status = BooleanField(default=False, help_text = "0-Available, 1-Not Available")
    added = BooleanField(default=False, help_text = "0-Not Added , 1-Added", choices=FOOD_STATUS)
    def __str__(self):
        return "{}".format(self.recipes)

class Hotel(Model):
    hotel_name = CharField(max_length=120, null=True)
    Location = CharField(max_length=500, null=True)
    pincode = ForeignKey(PinCode, on_delete=CASCADE)
    address = TextField()
    foods = ManyToManyField(Food)
    def __str__(self):
        return self.hotel_name    

class Cart(Model):
    ORDERED = 1
    BENDING = 2 
    CANCEL = 3
    NOTORDER = 0
    CART_STATUS = (
    (ORDERED, 'Order Place'), 
    (BENDING, 'bending'), 
    (NOTORDER, 'not_order'), 
    (CANCEL, 'cancel order')
    )
    # ----------------> The Module used for only this TB     
    from django.contrib.auth.models import User

    image = ImageField(upload_to = "Pictures", null = True)
    customer = CharField(max_length=150, null = False, blank = False)
    #customer = ForeignKey(User, on_delete=CASCADE)
    recipes = ForeignKey(Food, on_delete=CASCADE)
    quantity = IntegerField(default = 1, null = False)
    price = IntegerField()
    order_status = IntegerField(default = 0, choices = CART_STATUS)# 0.not_order, 1.ordered, 2.bending 3.cancel_order  

    def __str__(self):
        return "{},{}".format(self.customer, self.recipes)


