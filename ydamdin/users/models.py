from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    class Meta:
        verbose_name = "用户地址管理"
    addr = models.CharField(max_length=30,verbose_name="地址")
    name = models.CharField(max_length=10,verbose_name="联系人")
    phone = models.CharField(max_length=11,verbose_name="联系方式")

class UserInfo(models.Model):
    class Meta:
        verbose_name = "用户信息管理"
    u_id = models.OneToOneField(to=User,on_delete=models.CASCADE)
    nick = models.CharField(max_length=20,verbose_name='昵称')
    sex = models.IntegerField(choices=(
        (1,'男'),
        (0,'女')
    ),verbose_name="性别")
    phone = models.CharField(max_length=11,verbose_name="手机号")
    life = models.CharField(max_length=30,verbose_name="现居地")
    addrs = models.ManyToManyField(to=Address,verbose_name="地址管理")




