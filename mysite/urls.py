
from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    # path('polls/', views.index, name='index'),
    # path('polls/<int:question_id>/', views.detail, name='detail'),
    # path('polls/<int:question_id>/results/', views.results, name='results'),
    # path('polls/<int:question_id>/vote/', views.vote, name='vote'),

#    path('kdh/', views.index, name='index'),
#    path('kdh/', include('kdh.urls')),
    path('books/', include('books.urls')),
]
