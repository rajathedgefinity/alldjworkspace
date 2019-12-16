from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('salary',)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
