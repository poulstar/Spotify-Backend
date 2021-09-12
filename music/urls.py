from django.urls import path
from rest_framework import routers

from music.views import *

router = routers.SimpleRouter()
router.register(r'user/playlist', PlaylistViewSet, basename="user_playlist")
router.register(r'user/liked/musics', FavouriteViewSet, basename="user_liked_musics")

urlpatterns = [
    path('list/', MusicList.as_view()),
    path('album/list/', AlbumList.as_view()),
    path('category/list', CategoryList.as_view()),
    path('artist/list', ArtistList.as_view()),
    path('recent/list', RecentList.as_view()),
]

urlpatterns += router.urls
