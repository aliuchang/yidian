from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path("",views.Index.as_view(),name='index'),
    path("attr/", views.Attr.as_view(), name='attr'),
    path("goods/<int:id>",views.GoodsView.as_view(),name="goods")
]
