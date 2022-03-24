
from django.contrib import admin
from django.urls import path, include
from bookmark.views import BookmarkDV, BookmarkLV

app_name = "bookmark"
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
