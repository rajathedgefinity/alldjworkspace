from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    designation = models.CharField(max_length=255, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
