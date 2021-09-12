from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from accounts.models import Account
from music.serializers import PlaylistSerializer, FavouriteSerializer, RecentSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class AccountSerializer(ModelSerializer):
    user = UserSerializer(default=CurrentUserDefault())
    following = StringRelatedField(many=True)
    user_playlist = PlaylistSerializer(many=True)
    user_favourite = StringRelatedField()
    user_recent_musics = RecentSerializer(many=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'user',
            'image',
            'gender',
            'birthday',
            'following',
            'user_playlist',
            'user_favourite',
            'user_recent_musics',
        ]
