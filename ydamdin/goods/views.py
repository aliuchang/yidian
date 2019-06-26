from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
# Create your views here.
from rest_framework.renderers import JSONRenderer
from .serializers import GoodsSerializer
from .models import Goods

class Index(View):
    def get(self,request):
        data = Goods.objects.all()
        res = GoodsSerializer(data,many=True)
        print(res.data)
        res2 = JSONRenderer().render(res.data)
        print(res2)
        return HttpResponse(res)

