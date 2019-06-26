from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
# 商品属性
class Texture(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="面料材质")
    def __str__(self):
        return self.title

class Style(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="风格")
    def __str__(self):
        return self.title

class Fitpeople(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="适用人数")
    def __str__(self):
        return self.title

class Materials(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="五星脚材料")
    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="描述")
    color = models.CharField(max_length=20, unique=True, verbose_name="色值")  # 书写时使用“#”
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="分类")
    def __str__(self):
        return self.title

class Image(models.Model):
    img = models.ImageField(upload_to='../upload_img', verbose_name="产品图片")

class Goods(models.Model):
    # 商品编码
    name = models.CharField(max_length=50, unique=True, verbose_name="产品名称")
    ename = models.CharField(max_length=50, unique=True, verbose_name="英文名称")
    code = models.CharField(max_length=50, unique=True, verbose_name="产品编码")
    con = models.CharField(max_length=100, unique=True, verbose_name="简介")
    desc = models.CharField(max_length=50, unique=True, verbose_name="描述")
    sales = models.IntegerField(default=0, verbose_name="销量")
    price = models.FloatField(verbose_name="价格")
    # texture = models.CharField() 材质，做一个外键
    texture = models.ForeignKey(to=Texture, on_delete=models.CASCADE, verbose_name="面料材质")
    style = models.ForeignKey(to=Style, on_delete=models.CASCADE, verbose_name="风格")
    fitpeople = models.ForeignKey(to=Fitpeople, on_delete=models.CASCADE, verbose_name="适用人数")
    materials = models.ForeignKey(to=Materials, on_delete=models.CASCADE, verbose_name="五星脚材料")
    color = models.ManyToManyField(to=Color, verbose_name="颜色")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="分类")
    img = models.ManyToManyField(to=Image, verbose_name="产品图片")
    # img = models.ImageField(upload_to='./upload_img', verbose_name="产品图片")
    inventory = models.IntegerField(default=0, verbose_name="库存")
    content = RichTextField(verbose_name="商品详情")
    c_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")   # auto_now_add添加创建时间
    u_datetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")   # auto_now更新时间
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="作者", default=1)
    def __str__(self):
        return self.name
