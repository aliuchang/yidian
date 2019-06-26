from rest_framework.serializers import ModelSerializer
from .models import Goods, Image, Texture, Style, Fitpeople, Materials

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class GoodsSerializer(ModelSerializer):
    img = ImageSerializer(many=True)
    class Meta:     # 元类
        model = Goods
        fields = ['name', 'ename', 'desc', 'price', 'texture', 'style', 'fitpeople', 'materials', 'img']

class TextureSerializer(ModelSerializer):
    class Meta:
        model = Texture
        fields = '__all__'

class StyleeSerializer(ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'

class FitpeopleSerializer(ModelSerializer):
    class Meta:
        model = Fitpeople
        fields = '__all__'

class MaterialsSerializer(ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'
