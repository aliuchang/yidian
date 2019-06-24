from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
# FBT
# CBT

# Create your views here.

class Login(View):
    def post(self,request):

        return HttpResponse()


class Register(View):
    def post(self, request):
        try:
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            user = User.objects.create(username=username,password=password)
            user.save()
        except:
            return JsonResponse({'code':'no','message':'注册失败'})

        return JsonResponse({'code':'ok','message':'注册成功'})

class Index(View):
    pass
