# Extending User Model with One-To-One Link

[![Generic badge](https://img.shields.io/badge/CODE-WORKED-GREEN.svg)](https://shields.io/)

## What is a One-To-One Link?

It is a regular Django model that’s gonna have it’s own database table and will hold a One-To-One relationship with the existing User Model through a OneToOneField.

## When should I use a One-To-One Link?

You should use a One-To-One Link when you need to store extra information about the existing User Model that’s not related to the authentication process. We usually call it a User Profile.

This goes into models.py of your App

```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
"""We're adding other 3 fields to the existing user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    class Meta:
    """We're Ordering the table in terms of salary in ascending change 'salary' to '-salary' for descending order"""
        ordering = ('salary',)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
```

Here we're just adding extra information to the existing user by creating a seperate table.
