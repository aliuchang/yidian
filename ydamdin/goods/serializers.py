from rest_framework.serializers import ModelSerializer
from .models import Goods,Image,Texture,FitPeople,Style,Materials,Color

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class GoodsSerializer(ModelSerializer):
    img = ImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = ['id','name','en_name','desc','price','texture','style','fit_people','materials','img']


class TextureSerializer(ModelSerializer):
    class Meta:
        model = Texture
        fields = '__all__'

class StyleSerializer(ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'

class FitPeopleSerializer(ModelSerializer):
    class Meta:
        model = FitPeople
        fields = '__all__'

class MaterialsSerializer(ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'
class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class GoodsDetailSerializer(ModelSerializer):
    img = ImageSerializer(many=True)
    color = ColorSerializer(many=True)
    class Meta:
        model = Goods
        exclude = ['texture','style','fit_people','materials']
