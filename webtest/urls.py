# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),

    path('hello',views.Hello,name='Hello Dipankar'),

    path('index',views.index,name='index'),

    path('services',views.services,name='services'),
    
    path('contact',views.contact,name='contact'),
    
    path('calender',views.calender,name='calender'),
    
    path('login',views.login,name='login'),
    
    path('signup',views.signup,name='signup'),
    
    path('reset_pass',views.reset_pass,name='reset_pass'),
    
    path('forgot-pass',views.forgot_pass,name='forgot-pass'),
    
    path('user_interface',views.user_interface,name='user_interface'),

    path('Signup_user_otp_validation',views.signup_user_otp_validation,name='signup_user_otp_validation'),

    path('otp_validation',views.otp_validation,name='otp_validation'),

    path('logout',views.logout,name='logout'),


]