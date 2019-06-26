from rest_framework.serializers import ModelSerializer
from .models import Goods,Image
class GoodsSerializer(ModelSerializer):
    class Meta:
        model = Goods
        fields = ("name","en_name","desc","price","texture","style","fit_people","materials","img")
