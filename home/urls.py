from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('studlogin/', views.studlogin, name='studlogin'),
    path('faclogin/', views.faclogin, name='faclogin'),
    path('admlogin/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('logout/', views.logout_user, name='logout'),
    path('changePasswd/', views.change_passwd, name='changepasswd'),
    path('getotp/', views.getOTP, name='getotp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('export/', views.exportCSV, name='exportCSV')


]
