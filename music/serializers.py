from rest_framework.serializers import ModelSerializer, StringRelatedField, CurrentUserDefault
from music.models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'background_image',
            'image',
            'name',
            'about',
            'followers',
            'total_music'
        ]


class MusicSerializer(ModelSerializer):
    album = StringRelatedField()
    artist = ArtistSerializer()
    category = CategorySerializer()

    class Meta:
        model = Music
        fields = [
            'id',
            'cover',
            'name',
            'album',
            'artist',
            'category',
            'file',
            'release_year',
            'duration',
            'likes'
        ]


class AlbumSerializer(ModelSerializer):
    artist = ArtistSerializer()
    category = CategorySerializer()
    musics = MusicSerializer(many=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'cover',
            'name',
            'artist',
            'category',
            'musics',
            'release_year',
            'total_music'
        ]


class PlaylistSerializer(ModelSerializer):
    user = StringRelatedField(default=CurrentUserDefault())
    musics = MusicSerializer(many=True)

    class Meta:
        model = Playlist
        fields = [
            'id',
            'user',
            'cover',
            'name',
            'musics',
            'total_music'
        ]


class FavouriteSerializer(ModelSerializer):
    user = StringRelatedField(default=CurrentUserDefault())
    music = MusicSerializer()

    class Meta:
        model = Favourite
        fields = [
            'id',
            'user',
            'music',
            'is_fav',
        ]


class RecentSerializer(ModelSerializer):
    user = StringRelatedField(default=CurrentUserDefault())
    music = MusicSerializer()

    class Meta:
        model = Recent
        fields = '__all__'
