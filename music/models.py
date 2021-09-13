from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from mutagen.mp3 import MP3


# ------------------------------------ Category Model
class Category(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to="categories/covers")

    def __str__(self):
        return self.title

    def category_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)

    class Meta:
        verbose_name_plural = "Categories"


# ------------------------------------ Artist Model
class Artist(models.Model):
    background_image = models.ImageField(upload_to="artists/backgrounds", default="artists/backgrounds/default.png")
    image = models.ImageField(upload_to="artists/covers", default="artists/covers/default.png")
    name = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def followers(self):
        return self.account_set.all().count()

    def artist_image(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.image.url)

    def total_music(self):
        return self.music.all().count()


def validate_file_extension(value):
    if not value.name.endswith('.mp3'):
        raise ValidationError("Choose a standard extension, please")


# ------------------------------------ Music Model
class Music(models.Model):
    cover = models.ImageField(upload_to="musics/covers", default="musics/covers/default.png")
    name = models.CharField(max_length=255)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="musics", null=True, blank=True)
    artist = models.ManyToManyField("Artist", related_name="music")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    file = models.FileField(upload_to='musics/files', validators=[validate_file_extension])
    release_year = models.DateField(default=timezone.now)

    def __str__(self):
        if self.album:
            return '%s-%s' % (self.name, self.album.name)
        return '%s-%s' % (self.name, 'single')

    def duration(self):
        song = MP3(self.file)
        song_info = song.info
        length = song_info.length
        m = length // 60
        length %= 60
        s = length
        return '%s:%s' % (int(m), '0{}'.format(int(s)) if length < 10 else int(s))

    def likes(self):
        return self.is_fav.all().count()

    def music_artist(self):
        singer = ""
        for artist in self.artist.all():
            if artist == self.artist.all().reverse()[0]:
                singer += artist.name
            else:
                singer += ", " + artist.name
        return singer

    def music_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)

    class Meta:
        ordering = ["-release_year"]


# ------------------------------------ Album Model
class Album(models.Model):
    cover = models.ImageField(upload_to="albums/covers", default="albums/covers/default.png")
    name = models.CharField(max_length=255)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    release_year = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def total_music(self):
        return self.musics.all().count()

    def album_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)


# ------------------------------------ Playlist Model
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlist')
    cover = models.ImageField(upload_to="playlists/covers", default="playlists/covers/default.png")
    name = models.CharField(max_length=255)
    musics = models.ManyToManyField("Music")

    def __str__(self):
        return self.name

    def total_music(self):
        return self.musics.all().count()

    def playlist_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)


# ------------------------------------ Favourite Model
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite')
    image = models.ImageField(default="favourite/images/default.png")
    musics = models.ManyToManyField("Music", related_name="is_fav")

    # is_fav = models.BooleanField(default=True)

    def __str__(self):
        return '%s-%s' % (self.user.username, "favourite")

    def favourite_image(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.image.url)


# ------------------------------------ Recent Model
class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recent_musics')
    music = models.ForeignKey("Music", on_delete=models.CASCADE)
