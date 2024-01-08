from django.urls import path
from user.views import *

urlpatterns = [
    path('register/',userRegister,name='register'),
    path('login/',userLogin,name='login'),
    path('profiles/',profiles,name='profiles'),
    path('create/',createProfil,name='create'),
] 