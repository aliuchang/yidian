from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .serializers import GoodsSerializer,StyleSerializer,TextureSerializer,FitPeopleSerializer,MaterialsSerializer
from rest_framework.renderers import JSONRenderer
from .models import Goods,Texture,FitPeople,Style,Materials

# Create your views here.

class Index(View):
    def post(self,request):
        data = Goods.objects.all()
        res = GoodsSerializer(data,many=True)
        res2 = res.data
        return HttpResponse(res2)

class Attr(View):

    def getJson(self,model,serializer):
        data = model.objects.all()
        ser = serializer(data,many=True)
        res = ser.data
        return res
    def get(self,request):
        TextureJson = self.getJson(Texture,TextureSerializer)
        StyleJson = self.getJson(Style,StyleSerializer)
        FitPeopleJson = self.getJson(FitPeople,FitPeopleSerializer)
        MaterialsJson = self.getJson(Materials,MaterialsSerializer)
        print(TextureJson,StyleJson,FitPeopleJson,MaterialsJson)
        return JsonResponse({
            'textrue':TextureJson,
            'style':StyleJson,
            'fitPeople':FitPeopleJson,
            'materials':MaterialsJson
        })
