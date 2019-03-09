from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('deleteall', views.deleteall, name='deleteall'),
    path('delete/<int:id>',views.delete,name='delete'),
    
]
