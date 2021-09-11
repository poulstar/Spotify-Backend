from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from mutagen.mp3 import MP3


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to="categories/covers")

    def __str__(self):
        return self.title

    def category_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)

    class Meta:
        verbose_name_plural = "Categories"


class Artist(models.Model):
    image = models.ImageField(upload_to="artists/covers", default="artists/cover/default.png")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def followers(self):
        return self.account_set.all().count()

    def artist_image(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.image.url)


class Music(models.Model):
    cover = models.ImageField(upload_to="musics/covers", default="musics/covers/default.png")
    name = models.CharField(max_length=255)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="musics", null=True, blank=True)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    file = models.FileField(upload_to='musics/files')
    release_year = models.DateField(default=timezone.now)

    def __str__(self):
        if self.album:
            return '%s-%s' % (self.name, self.album.name)
        return self.name

    def duration(self):
        song = MP3(self.file)
        song_info = song.info
        length = song_info.length
        m = length // 60
        length %= 60
        s = length
        return '%s:%s' % (int(m), '0{}'.format(int(s)) if length < 10 else int(s))

    def music_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)

    class Meta:
        ordering = ["-release_year"]


class Album(models.Model):
    cover = models.ImageField(upload_to="albums/covers", default="albums/covers/default.png")
    name = models.CharField(max_length=255)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    release_year = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s-%s' % (self.name, self.artist.name)

    def total_music(self):
        count = 0
        for i in self.musics.all():
            count += 1
        return count

    def album_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="playlists/covers",  default="playlists/covers/default.png")
    name = models.CharField(max_length=255)
    musics = models.ManyToManyField("Music")

    def __str__(self):
        return self.name

    def total_music(self):
        count = 0
        for i in self.musics.all():
            count += 1
        return count

    def playlist_cover(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.cover.url)


class Favourite(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    musics = models.ForeignKey("Music", on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return '%s-%s' % (self.user.username, self.musics.name)


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey("Music", on_delete=models.CASCADE)
