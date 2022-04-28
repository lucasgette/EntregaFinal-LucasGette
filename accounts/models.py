from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', default='default.jpg')
    description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=220, null=True, blank=True)

    def __str__(self):
        return self.user.username
