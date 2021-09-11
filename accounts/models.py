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
    gender = models.CharField(max_length=6, choices=GENDER)
    birthday = models.DateField(default=timezone.now)
    following = models.ManyToManyField(Artist)

    def __str__(self):
        return self.user.username

    def account_image(self):
        return mark_safe('<img src="%s" width="60" height="60" />' % self.image.url)
