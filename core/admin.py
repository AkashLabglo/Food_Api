from django.contrib.admin import site
from core.models import (
    HOTEL_MODELS, models, order_payment, register_models
)
# -----------> HOTEL_MODELS
site.register(HOTEL_MODELS.PinCode)
site.register(HOTEL_MODELS.Hotel)
site.register(HOTEL_MODELS.Food)
site.register(HOTEL_MODELS.Cart)

# -----------> models_MODELS
site.register(models.User_Address)
#site.register(models.DateTimeUpdate)

# -----------> order_payment_MODELS
site.register(order_payment.Orderby)
site.register(order_payment.Payment)
site.register(order_payment.Deliver_Address)

# -----------> oregister_models_MODELS
site.register(register_models.Customer)
