from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import UserInfoSerializer
from rest_framework.renderers import JSONRenderer
# 显示登录



# Create your views here.

class Index(LoginRequiredMixin,View):
    def get(self,request):

        # print(dir(request.user.userinfo))
        ser = UserInfoSerializer(request.user.userinfo)
        res = JSONRenderer().render(ser.data)
        return HttpResponse(res)
        # return HttpResponse("ok")
