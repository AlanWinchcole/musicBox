from django.urls import path
from musicboxapp import views
from django.conf import settings
from django.conf.urls.static import static
from musicboxapp.views import HomepageView, BrowseView, BrowseGenresView, AlbumView, \
                            AddReviewView, AddCommentView, PopularPageView, DeleteReviewView, \
                            SurprisePageView, TrendingPageView, SearchView

app_name = 'musicboxapp'

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('browse/', BrowseView.as_view(), name='browse'),
    path('genres/', BrowseGenresView.as_view(), name='genres'),
    path('trending/', TrendingPageView.as_view(), name='trending'),
    path('popular/', PopularPageView.as_view(), name='popular'),
    path('surprise/', SurprisePageView.as_view(), name='surprise_me'),
    path('album/<slug:album_name_slug>', AlbumView.as_view(), name='album'),
    path('album/<slug:album_name_slug>/add_review/', AddReviewView.as_view(), name='add_review'),
    path('album/<slug:album_name_slug>/delete_review/', DeleteReviewView.as_view(), name='delete_review'),
    path('musicboxapp/search/', SearchView.as_view(), name='search'),
]
