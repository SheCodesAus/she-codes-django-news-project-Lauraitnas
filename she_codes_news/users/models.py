from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.URLField(("profile picture"), blank = True, null = True)
    bio = models.TextField(max_length=500, blank = True, null = True)
    linkedin = models.URLField(("linkedin"), blank = True, null = True)
    github = models.URLField(("github"), blank = True, null = True)



    def __str__(self):
        return self.username


