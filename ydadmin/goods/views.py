from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .serializers import GoodsSerializer, TextureSerializer, StyleeSerializer, FitpeopleSerializer, MaterialsSerializer
from rest_framework.renderers import JSONRenderer
from .models import Goods, Texture, Style, Fitpeople, Materials

# Create your views here.
class Index(View):
    def post(self, request):
        data = Goods.objects.all()
        # print(data)
        res = GoodsSerializer(data, many=True)    # json数据，一个序列化对象
        # print(res)
        # res2 = JSONRenderer().render(res.data)
        # print(res2)
        res2 = res.data
        return HttpResponse(res2)

class Attr(View):
    def getJson(self, model, serializer):
        data = model.objects.all()
        ser = serializer(data, many=True)
        # res = JSONRenderer().render(ser.data)
        res = ser.data
        return res
    def get(self, request):
        TextureJson = self.getJson(Texture, TextureSerializer)
        StyleJson = self.getJson(Style, StyleeSerializer)
        FitpeopleJson = self.getJson(Fitpeople, FitpeopleSerializer)
        MaterialsJson = self.getJson(Materials, MaterialsSerializer)
        # print(TextureJson, StyleJson, FitpeopleJson, MaterialsJson)
        return JsonResponse({
            'texture': TextureJson,
            'style': StyleJson,
            'fitpeople': FitpeopleJson,
            'materials': MaterialsJson,
        })
