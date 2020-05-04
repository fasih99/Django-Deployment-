from django.contrib import admin
from django.urls import path,include
from basic_app import views

#template URLs
app_name='basic_app'

urlpatterns=[
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name="user_login"),
]
