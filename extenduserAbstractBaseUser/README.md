
# Creating Custom User Model for Authentication

## What is a Custom User Model Extending AbstractBaseUser?
It is an entirely new User model that inherit from AbstractBaseUser. It requires a special care and to update some references through the settings.py. Ideally it should be done in the begining of the project, since it will dramatically impact the database schema. Extra care while implementing it.

## When should I use a Custom User Model Extending AbstractBaseUser?
You should use a Custom User Model when your application have specific requirements in relation to the authentication process. For example, in some cases it makes more sense to use an email address as your identification token instead of a username.

Below code reference for the Model Creation for Custom User Model Always a Model Requires Model Manager for Making Model to Work.

```

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an Username")

        user = self.model(
                email = self.normalize_email(email),
                username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email = self.normalize_email(email),
                password = password,
                username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
```

Below is the Code to add Search functionality into django admin.
It helps to make our password not to seen.

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined','last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
```
