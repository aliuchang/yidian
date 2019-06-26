from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Texture(models.Model):
    title = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.title
class Style(models.Model):
    title = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.title
class Fit_people(models.Model):
    title = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.title
class Materials(models.Model):
    title = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=50,unique=True,verbose_name="描述",default="")
    color = models.CharField(max_length=20,unique=True,verbose_name="色值",default="")
    def __str__(self):
        return self.title
class Image(models.Model):
    img = models.ImageField(upload_to="./upload_img", verbose_name="产品图片")

#商品属性
class Goods(models.Model):
    #编码
    name = models.CharField(max_length=20,unique=True,verbose_name="产品名称")
    en_name = models.CharField(max_length=20,unique=True,verbose_name="英文名称")
    code = models.CharField(max_length=20,unique=True,verbose_name="产品编号")
    con = models.CharField(max_length=20,unique=True,verbose_name="内容")
    desc = models.CharField(max_length=20,unique=True,verbose_name="简介")
    sales = models.IntegerField(default=0,verbose_name="销量")
    price = models.FloatField(verbose_name="价格")
    title = models.CharField(max_length=20, unique=True)
    texture = models.ForeignKey(to=Texture, on_delete=models.CASCADE, verbose_name="面料材质")
    style = models.ForeignKey(to=Style, on_delete=models.CASCADE, verbose_name="风格")
    fit_people = models.ForeignKey(to=Fit_people, on_delete=models.CASCADE, verbose_name="适用人群")
    materials = models.ForeignKey(to=Materials, on_delete=models.CASCADE, verbose_name="五星角材质")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="分类")
    img = models.ManyToManyField(to=Image,verbose_name="产品图片",)
    inventory = models.IntegerField(default=0, verbose_name="库存")
    color = models.ManyToManyField(to=Color,verbose_name="颜色")
    content = RichTextField(verbose_name="商品详情")
    c_datatime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    u_datatime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
