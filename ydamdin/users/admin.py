from django.contrib import admin
from .models import  UserInfo,Address

# Register your models here.



@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass


class UserInfoInline(admin.StackedInline):
    model = UserInfo.addrs.through
    extra = 0


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    inlines = [UserInfoInline]

