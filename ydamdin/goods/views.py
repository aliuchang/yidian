from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .serializers import GoodsSerializer,StyleSerializer,TextureSerializer,FitPeopleSerializer,MaterialsSerializer,GoodsDetailSerializer
from rest_framework.renderers import JSONRenderer
from .models import Goods,Texture,FitPeople,Style,Materials

# Create your views here.

class Index(View):
    def post(self,request):
        t = request.POST.get('t_id',None)
        s = request.POST.get('s_id',None)
        f = request.POST.get('f_id',None)
        m = request.POST.get('m_id',None)

        obj = Goods.objects
        if t:
            obj = obj.filter(texture__id=t)
        if s:
            obj = obj.filter(style__id=s)
        if f:
            obj = obj.filter(fit_people__id=f)
        if m:
            obj = obj.filter(materials__id=m)

        queryset = obj.all()


        res = GoodsSerializer(queryset,many=True)
        res2 = JSONRenderer().render(res.data)
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

class GoodsView(View):
    def get(self,request,id):
        res = Goods.objects.filter(id=id).first()
        res = GoodsDetailSerializer(res)
        res2 = JSONRenderer().render(res.data)
        print(res2)
        return HttpResponse(res2)
