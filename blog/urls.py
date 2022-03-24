
from django.contrib import admin
from django.urls import path, include
from blog import views


app_name = "blog"
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
]
