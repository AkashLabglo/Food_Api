from rest_framework.serializers import *
from core.models.order_payment import *
from core.models.HOTEL_MODELS import *
from core.serializers.hotel_food_cart_ser import cart_ser

class Order_list_ser(ModelSerializer):
    class Meta:
        model = Orderby
        fields = "__all__"

class Order_Added(ModelSerializer):
    #ordered_things = ManyToManyField(Cart)
    ordered_things = HyperlinkedRelatedField(view_name='cartdetail',read_only = True)
    class Meta:
        model = Orderby
        fields = [
            'id', 'order_status','ordered_things'
        ]