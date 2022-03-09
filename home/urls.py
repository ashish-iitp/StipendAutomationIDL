from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('logout/', views.logout_user, name='logout'),
    path('changePasswd/', views.change_passwd, name='changepasswd'),
    path('getotp/', views.getOTP, name='getotp'),
]
