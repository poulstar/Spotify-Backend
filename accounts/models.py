from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from music.models import Artist


# Create your models here.
class Account(models.Model):
    GENDER = (
        ("female", "Female"),
        ("male", "Male")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="accounts/images", default="accounts/images/default.png")
    gender = models.CharField(max_length=6, choices=GENDER, default="male")
    birthday = models.DateField(default=timezone.now)
    following = models.ManyToManyField(Artist, blank=True)

    def __str__(self):
        return self.user.username

    def user_playlist(self):
        return self.user.playlist.all()

    def user_favourite(self):
        return self.user.favourite.all()

    def user_recent_musics(self):
        return self.user.recent_musics.all()

    def account_image(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.image.url)
