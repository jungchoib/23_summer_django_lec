from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('main/', views.mainmain),
    path('login/', views.login),
    path('login_new/', views.login_new),
    path('login_ser/', views.login_search),
    path('item1/', views.item1),
    path('item2/', views.item2),


]