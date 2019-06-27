from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField



# Create your models here.


# 商品属性
class Texture(models.Model):
    title = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.title

class Style(models.Model):
    title = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.title
class FitPeople(models.Model):
    title = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.title
class Materials(models.Model):
    title = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=20,unique=True,verbose_name="描述")
    color = models.CharField(max_length=20,unique=True,verbose_name="色值")
    def __str__(self):
        return self.title

class Image(models.Model):
    img = models.ImageField(upload_to="./upload_img", verbose_name="产品图片")
    def __str__(self):
        return str(self.img)


class Goods(models.Model):
    class Meta:
        verbose_name='商品管理'
        verbose_name_plural = "商品管理"
        ordering = ['-c_datatime']
    #编码
    name = models.CharField(max_length=50,unique=True,verbose_name="产品名称")
    en_name = models.CharField(max_length=50, unique=True, verbose_name="英文名称")
    code = models.CharField(max_length=50,unique=True,verbose_name="产品编号")
    con = models.CharField(max_length=100, unique=True, verbose_name="内容")
    desc = models.CharField(max_length=50,unique=True,verbose_name="简介")
    sales = models.IntegerField(default=0,verbose_name='销量')
    price = models.FloatField(verbose_name="价格")
    texture = models.ForeignKey(to=Texture,on_delete=models.CASCADE,verbose_name="材质")
    style = models.ForeignKey(to=Style,on_delete=models.CASCADE,verbose_name="风格")
    fit_people = models.ForeignKey(to=FitPeople,on_delete=models.CASCADE,verbose_name="适用人群")
    materials = models.ForeignKey(to=Materials,on_delete=models.CASCADE,verbose_name="五星脚材料")
    color = models.ManyToManyField(to=Color,verbose_name='颜色')

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="分类")
    img = models.ManyToManyField(to=Image,verbose_name="产品图片")
    inventory = models.IntegerField(default=0,verbose_name='库存')
    content = RichTextField(verbose_name="商品详情")
    c_datatime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    u_datatime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.name













