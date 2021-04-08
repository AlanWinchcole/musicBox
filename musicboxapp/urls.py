from django.urls import path
from musicboxapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'musicboxapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('browse/', views.browse, name='browse'),
    path('genres/', views.browse_genres, name='genres'),
    path('trending/', views.trending_page, name='trending'),
    path('popular/', views.popular_page, name='popular'),
    path('surprise/', views.surprise_me, name='surprise_me'),
    path('album/<slug:album_name_slug>', views.album, name='album'),
    path('album/<slug:album_name_slug>/add_review/', views.add_review, name='add_review'),
    path('album/<slug:album_name_slug>/edit_review/', views.edit_review, name='edit_review'),
    path('album/<slug:album_name_slug>/delete_review/', views.delete_review, name='delete_review'),
    path('musicboxapp/search/', views.search, name='search'),
]
