
from django.shortcuts import render
from django.http import HttpResponse

from . import views
from django.urls import path,include

urlpatterns=[
    
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("buyinguide/",views.buyinguide,name="buyinguide"),
    path("more/",views.more,name="more"),
    path("login1/",views.login1,name="lohin1"),
    path("signup1/",views.Signedup.as_view(),name="signup1"),
    path("logout/",views.logout,name="logout"),
    path("forgot/",views.forgot),
    path("send_otp/",views.send_otp,name='send_otp'),
    path("verify_otp/",views.verify_otp,name='verify_otp'),
    path("change_pass/",views.change_pass,name='change_pass'),
    path("verify_pass/",views.verify_pass,name='verify_pass'),
    path("trylogout/",views.tryout,name="tryout"),
    path("account/",views.account,name="account"),
    path("bluesapphire/",views.bluesapphire,name=""),
    path("emerald/",views.emerald,name=""),
    path("opal/",views.opal,name=""),
    path("ruby/",views.ruby,name=""),
    ]