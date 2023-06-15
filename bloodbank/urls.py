from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('register',views.register),
    path('login',views.login),
    path('contact',views.contact),

    path('saveuser',views.saveuser),
    path('loginuser',views.loginuser),

    path('user/home',views.userhome),
    path('user/request',views.requestpage),    
    path('user/saverequest',views.saverequest),
    path('user/logout',views.logout),
    
]
