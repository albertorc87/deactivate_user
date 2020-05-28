from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    modified = models.DateTimeField(auto_now=True)