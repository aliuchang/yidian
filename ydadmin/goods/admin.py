from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ['name', 'ename', 'code', 'desc', 'sales', 'price', 'inventory', 'category', 'texture', 'style', 'fitpeople', 'materials', 'getColor', 'getImage','c_datetime', 'u_datetime', 'author']

    # Color
    def getColor(self, obj):
        color = obj.color.all()[0].title
        return color
    getColor.short_description = "getColor"

    # Image
    def getImage(self, obj):
        img = str(obj.img.all()[0].img)
        img = img.split("/")[-1]
        # print(img)
        return format_html('<img src="/media/%s" width="100px">' % img)

    getImage.short_description = "getImage"

    # 控制管理员“添加”和“更改”页面的布局
    fieldsets = (
        ("产品信息", {
            'fields': ('name', 'ename', 'code', 'desc', 'con'),
            # 'classes': ('', 'collapse'),
            # 'description': "这是标题"
        }),
        ("产品详细信息", {
            'fields': ('sales', 'price', 'inventory', 'content', 'author')
        }),
        ("产品属性", {
            'fields': ('img', 'category', 'texture', 'style', 'fitpeople', 'materials', 'color'),
            'classes': ('', 'collapse'),
        }),
    )

class GoodsInline(admin.StackedInline):
    model = Goods
    extra = 0   # 默认内联为0

@admin.register(Texture)
class TextureAdmin(admin.ModelAdmin):
    inlines = [GoodsInline]

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    inlines = [GoodsInline]

@admin.register(Fitpeople)
class FitpeopleAdmin(admin.ModelAdmin):
    inlines = [GoodsInline]

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    inlines = [GoodsInline]

class Colorinline(admin.StackedInline):
    model = Goods.color.through
    extra = 0  # 默认内联为0

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    inlines = [Colorinline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [GoodsInline]

class Imagesinline(admin.StackedInline):
    model = Goods.img.through
    extra = 0  # 默认内联为0

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    inlines = [Imagesinline]


