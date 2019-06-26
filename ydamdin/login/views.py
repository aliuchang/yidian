from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

class Login(View):
    def post(self,request):
        try:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            obj = auth.authenticate(request,username=username,password=password)
            if obj:
                return JsonResponse({'code':'ok','message':'验证成功'})
            else:
                return JsonResponse({'code':'no','message':'账号或者密码错误'})
        except:
            return JsonResponse({'code':'no','message':'验证失败'})
class Register(View):
    def post(self, request):
        try:
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            print(username,password)
            user = User.objects.create_user(username=username,password=password)
            print(user)
            user.save()
        except:
            return JsonResponse({'code':'no','message':'注册失败'})
        return JsonResponse({'code':'ok','message':'注册成功'})

class Index(View):
    pass
