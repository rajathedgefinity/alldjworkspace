from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(User):
    """Here I'm Just Creating a Person Model Which is Just Extending from User Model"""

    class Meta:
        """It's making a proxy to User App"""
        proxy = True

    def company(self):
        """Added a Method called Company to the User Model via Person Model"""
        return "Edgefinity"

    def givememailid(self,usr):
        """Added a Method called givememailid to the User Model along with the Username via Person Model"""
        self.temp_usr_var = Person.objects.get(username=usr)
        return self.temp_usr_var.email
