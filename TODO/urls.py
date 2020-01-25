from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
    path('deleteall', views.deleteall, name='deleteall'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]
