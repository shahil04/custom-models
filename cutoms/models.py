from django.db import models
from django.contrib.auth.models import AbstractUser

class Database(AbstractUser):
    phone_no=models.PositiveIntegerField(default=0)
    message=models.TextField(max_length='150')
    age=models.PositiveIntegerField(default=0)
