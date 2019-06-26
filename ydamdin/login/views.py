from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# FBT
# CBT

# Create your views here.

class Login(View):
    def post(self,request):
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print(username,password)
        user =  authenticate(request,username=username,password=password)
        print(User.objects.all())
        print(user)

        if username!=None and password !=None:
            user = authenticate(request, username=username,password=password)

            if user:
                login(request,user)
                return JsonResponse({'code':'ok','message':'登录成功'})
            else:
                return JsonResponse({'code':'no','message':'没有此用户'})
        else:
            return JsonResponse({'code':'no','message':'用户名或密码不能为空'})


class Register(View):
    def post(self, request):
        try:
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            user = User.objects.create_user(username=username,password=password)
            user.save()
        except:
            return JsonResponse({'code':'no','message':'注册失败'})

        return JsonResponse({'code':'ok','message':'注册成功'})

class Index(View):
    pass
