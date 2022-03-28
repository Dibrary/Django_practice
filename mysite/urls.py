
from django.contrib import admin
from django.urls import path, include
from polls import views

from bookmark.views import BookmarkLV, BookmarkDV
from mysite.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('polls/', include('polls.urls')),
    # path('polls/', views.index, name='index'),
    # path('polls/<int:question_id>/', views.detail, name='detail'),
    # path('polls/<int:question_id>/results/', views.results, name='results'),
    # path('polls/<int:question_id>/vote/', views.vote, name='vote'),

#    path('kdh/', views.index, name='index'),
#    path('kdh/', include('kdh.urls')),
    path('books/', include('books.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]
