from django.contrib import admin
from .models import Goods,Texture,Style,FitPeople,Materials,Category,Image,Color
from django.utils.html import format_html

# Register your models here.

class Images_inline(admin.StackedInline):
    model = Goods.img.through
    extra = 0
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    inlines = [Images_inline]


class Color_inline(admin.StackedInline):
    model = Goods.color.through
    extra = 0
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    inlines = [Color_inline]


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name','en_name','desc','code','con','sales','price','inventory','category','texture','style','fit_people','materials','getColor','getImg','c_datatime','u_datatime']

    def getColor(self,obj):
        color = obj.color.all()[0].title
        return color
    getColor.short_description = "getColor"

    def getImg(self,obj):
        img = str(obj.img.all()[0].img)
        img = img.split("/")[-1]
        print(img)
        return format_html("<img src='/media/upload_img/%s' width='100'>"%img)
    getImg.short_description = "getImg"

    fieldsets = (
        ("产品信息",{
            'fields':('name','en_name','code','desc', 'con'),
            # 'description':"这是标题" 描述
        }),
        ("产品详细", {
            'fields': ('sales', 'price','inventory','content'),
            'classes': ('collapse',)
        }),
        ("产品属性", {
            'fields': ('img','category','texture', 'style', 'fit_people','materials','color'),
            'classes':('collapse',)
        }),


    )


class Goods_Inline(admin.StackedInline):
    model = Goods
    extra = 0  # 默认内联为0


@admin.register(Texture)
class TextureAdmin(admin.ModelAdmin):
    inlines = [Goods_Inline]

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    inlines = [Goods_Inline]

@admin.register(FitPeople)
class FitPeopleAdmin(admin.ModelAdmin):
    inlines = [Goods_Inline]

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    inlines = [Goods_Inline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [Goods_Inline]





