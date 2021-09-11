from django.contrib import admin
from music.models import Category, Artist, Music, Album, Playlist, Favourite, Recent


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_cover', 'title',)
    search_fields = ('title', )


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_image', 'name', 'followers')
    search_fields = ('name', )


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('music_cover', 'name', 'album', 'artist', 'category', 'release_year')
    search_fields = ('name', 'artist')
    list_filter = ('category', 'artist', 'release_year')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_cover', 'name', 'artist', 'category', 'total_music', 'release_year')
    search_fields = ('name', 'artist')
    list_filter = ('category', 'artist', 'release_year')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('playlist_cover', 'name', 'user', 'total_music')
    search_fields = ('name', 'user')
    list_filter = ('user', )


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_fav')
    search_fields = ('user', )
    list_filter = ('user', )


@admin.register(Recent)
class RecentAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', )
    list_filter = ('user', )

