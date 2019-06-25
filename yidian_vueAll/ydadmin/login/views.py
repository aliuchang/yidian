from django.shortcuts import render
# 继承已有的基本视图(通用视图)：比如有一些网页就是做表单验证的...
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


"""
 django里有两种定义视图的方法
 FBT ：function base template
 CBT ：class base template
"""

# Create your views here.
# 还要把视图函数放到urls中
class Login(View):
    # def get(self,requests):
        # return HttpResponse("123")
    def post(self,request):
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        # print(username,password)
        # user = authenticate(request,username=username,password=password)
        # print(User.objects.all())
        # print(user)

        if username != None and password != None:
            user = authenticate(request, username=username,password=password)
            if user:
                # print(user)
                login(request,user)
                return JsonResponse({'code':'ok','message':'登录成功'})
            else:
                return JsonResponse({'code': 'no', 'message': '没有此用户'})
        else:
            return JsonResponse({'code':'no','message':'用户名或密码不能为空'})


# 注册是否成功，去admin里看一下
class Register(View):
    def post(self,request):
        try:
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            # print(username,password)
            user = User.objects.create_user(username=username,password=password)
            user.save()
        except:
            return JsonResponse({'code':'no','messager':'注册失败'})
        return JsonResponse({'code':'ok','messager':'注册成功'})

class Index(View):
    pass