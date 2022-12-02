from django.contrib.admin import *
from grappelli.forms import GrappelliSortableHiddenMixin
from core.models import (
    HOTEL_MODELS, models, order_payment, register_models
)
# - - - - - - - - - - - - - - - - - - 
site.site_header = "Sky Akash"  #   |
# - - - - - - - - - - - - - - - - - - 
# -----------> HOTEL_MODELS # - - - -  
site.register(HOTEL_MODELS.PinCode)# |
site.register(HOTEL_MODELS.Hotel)#   |
#site.register(HOTEL_MODELS.Food)#   |
site.register(HOTEL_MODELS.Cart)#    |
# - - - - - - - - - - - - - - - - - - 
# -----------> models_MODELS
site.register(models.User_Address)#   |
#site.register(models.DateTimeUpdate)#|
# - - - - - - - - - - - - - - - - - - 
# -----------> order_payment_MODELS
site.register(order_payment.Orderby)# |
site.register(order_payment.Payment)# |
site.register(order_payment.Deliver_Address)
# - - - - - - - - - - - - - - - - - - 
# -----------> oregister_models_MODELS #|
site.register(register_models.Customer)#|
# - - - - - - - - - - - - - - - - - -  



class addedexradatas(StackedInline): # -----> Form Type View
    model = HOTEL_MODELS.Cart
class MyInlineModelOptions(TabularInline, GrappelliSortableHiddenMixin): # -----> Table Type View
    model = HOTEL_MODELS.Cart
    
class Foods(ModelAdmin):
    list_display = ('category', 'recipes','image', 'price', 'status', 'added')
    list_display_links = ('recipes', 'image')
    search_fields = ('category', 'price', 'recipes')
    list_editable = ('price', )
    inlines = [MyInlineModelOptions]
    list_filter = ('category', 'price', 'status')
    #sortable_field_name = ("customer")
    fieldsets = [
        ("Food", {'fields': ['category','recipes',] }),
        ('Service', {'fields': [ 'price', 'status', ]}),
        ('Detail', {'fields': ['image','added']}),

    ] # ---------- > Seperate The Fields with Heading
site.register(HOTEL_MODELS.Food, Foods)
# requestedby, noofcopies, additionalinfo, account, finishing, noofsides, requireddate, paper, color, requestdate, sided

# additionalinfo, finishing, sided, paper, color
