from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index),
    path("login/",views.login),
    path("form/",views.registration),
    path("welcome/",views.welcome),
    path("login_user/",views.user_login),
    path("data/",views.data),
   

    
]
