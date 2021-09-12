from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from music.models import *
from music.serializers import *


# Create your views here.
class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArtistList(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class MusicList(ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class AlbumList(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PlaylistViewSet(ModelViewSet):
    # queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class FavouriteViewSet(ModelViewSet):
    # queryset = Playlist.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)


class RecentList(ListAPIView):
    queryset = Recent.objects.all()
    serializer_class = RecentSerializer
    permission_classes = (IsAuthenticated, )
