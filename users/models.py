from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model for Daily Vlog Social Platform API.

    Extends Django's AbstractUser with additional fields:
    - bio: Optional text about the user
    - profile_picture: Optional URL for the user's profile image
    """
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return self.username
