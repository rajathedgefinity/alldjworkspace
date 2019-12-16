# Creating a Custom User Model Extending AbstractUser

[![Generic badge](https://img.shields.io/badge/CODE-WORKED-GREEN.svg)](https://shields.io/)

## What is a Custom User Model Extending AbstractUser?
It is a new User model that inherit from AbstractUser. It requires a special care and to update some references through the settings.py. Ideally it should be done in the begining of the project, since it will dramatically impact the database schema. Extra care while implementing it.

## When should I use a Custom User Model Extending AbstractUser?
You should use it when you are perfectly happy with how Django handles the authentication process and you wouldn’t change anything on it. Yet, you want to add some extra information directly in the User model, without having to create an extra class.

It's Pretty Simple and Straight Forward where we can create our Custom User Model. That'll directly integrate with Authentication.

Straight and Custom User Built and Extended.

```
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    designation = models.CharField(max_length=255, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
```
