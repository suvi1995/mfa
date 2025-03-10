from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.signup, name='signup'),
    path ('login', views.login, name='login'),
    path('home', views.home, name='home'),
    #path('forgetpass_mail', views.forgetpass_mail, name='forgetpass_mail'),
    #path('forgetpassword/<token>', views.forgetpassword , name="forgetpassword"),
   # path('forgetpassword', views.forgetpassword, name='forgetpassword'),
    #path('mfa', views.mfa, name='mfa'),
    #path('qr', views.qr, name='qr'),
    #path('mfa_otp', views.mfa_otp, name='mfa_otp'),
    #path("verify-otp/", views.mfa_otp, name="verify_otp"),
]