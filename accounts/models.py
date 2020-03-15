from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_image', blank=True)
    banner = models.ImageField(upload_to='accounts/images/banner', default='/static/accounts/avatar1.png')

    def __str__(self):
        return self.user







